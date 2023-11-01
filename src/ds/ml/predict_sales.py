from typing import Generator

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMAResultsWrapper
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.holtwinters.results import HoltWintersResultsWrapper

from ds.schema.sales import SalesObject


def preprocessing(sales: SalesObject) -> pd.DataFrame:
    df = sales.df[["order_purchase_timestamp", "product_id", "sales", "order_item_id"]]

    # group sales by product and week
    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])
    df = df.set_index("order_purchase_timestamp")

    grouped_sales = df.groupby(["product_id", pd.Grouper(freq="W")]).sum()
    return grouped_sales


def resample(grouped_sales: pd.DataFrame) -> pd.DataFrame:
    grouped_sales = grouped_sales.pivot(
        index="order_purchase_timestamp", columns="product_id", values="sales"
    )
    grouped_sales = grouped_sales.resample("W").sum().fillna(0)
    return grouped_sales


def train_sample(grouped_sales: pd.DataFrame) -> Generator:
    train_size = int(len(grouped_sales) * 0.8)
    train_set = grouped_sales.iloc[:train_size].values
    test_set = grouped_sales.iloc[train_size:].values
    yield train_set
    yield test_set


def visualize_plt(train_set: np.ndarray) -> None:
    plt.plot(train_set)
    plt.show()


def train(train_set: np.ndarray) -> Generator:
    # ARIMA Model
    model_arima = ARIMA(train_set, order=(5, 1, 0))
    model_arima_fit = model_arima.fit(disp=0)

    # Exponential Smoothing Model
    model_es = ExponentialSmoothing(train_set)
    model_es_fit = model_es.fit()
    yield model_arima_fit
    yield model_es_fit


def predict(
    grouped_sales: pd.DataFrame,
    model_arima_fit: ARIMAResultsWrapper,
    model_es_fit: HoltWintersResultsWrapper,
    train_set: np.ndarray,
    test_set: np.ndarray,
) -> None:
    arima_predicted = model_arima_fit.forecast(steps=len(test_set))[0]
    arima_mse = mean_squared_error(test_set, arima_predicted)

    # Exponential Smoothing Prediction
    es_predicted = model_es_fit.predict(
        start=len(train_set), end=len(grouped_sales) - 1
    )
    es_mse = mean_squared_error(test_set, es_predicted.values)

    print("ARIMA Mean Squared Error:", arima_mse)
    print("Exponential Smoothing Mean Squared Error:", es_mse)
