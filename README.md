## Quickstart

### For Users

**How to set up**

1. Go to [package repository](https://github.com/knightzhang1314/ecommerce-test) and download preferred verion of the application.

2. Install the wheel package into your environment.

```
$ pip install ds-(version)-py3-none-any.whl
```
### Final table structure

column name | type | describe | sample
--- | --- | --- | ---
order_id | STRING | Unique identifier for the order | "8272b63d03f5f79c56e9e4120aec44ef"
order_item_id | INT | Sequential number identifying the order item | 1
product_id | STRING | Unique identifier for the product | "50ba38c4dc467baab1ea2c8c7747934d"
product_category_name | STRING | Name of the product category | "perfumery"
payment_value | DOUBLE | Value of the payment for the order | 124.90
payment_type | STRING | Payment method used for the order | "credit_card"
customer_id | STRING | Unique identifier for the customer | "b7aafc6ed8380bb86f57c1a4606fccc7"
order_status | STRING | Current status of the order | "delivered"
order_purchase_timestamp | TIMESTAMP | Date and time when the order was made | "2017-02-13 22:07:15"
order_approved_at | TIMESTAMP | Date and time when the order was approved by the seller | "2017-02-13 22:22:46"
order_delivered_carrier_date | TIMESTAMP | Date and time when the carrier received the order | "2017-03-09 14:17:59"
order_delivered_customer_date | TIMESTAMP | Date and time when the order was delivered to the customer | "2017-03-16 13:19:19"
order_estimated_delivery_date | TIMESTAMP | Estimated date when the order was supposed to be delivered | "2017-03-21 00:00:00"

### For Developers

You can use any preferred virtual environment.

Here is the instruction with [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

```sh
# create a virtual environment
$ conda create -y --name=ds python=3.9
# activate it
$ conda activate ds
# upgrade your pip installation
pip install --upgrade pip
# install required libraries for production
pip install -r requirements.txt
```

#### How to execute it locally

```sh
# move to src folder
$ cd src
# you can add or delete the config yaml, if you have different scope then add after config
# you can change the platform in the entrypoint.
# execute
$ python entrypoint.py
```

#### How to run in notebook, you can check the [notebook](https://github.com/knightzhang1314/ecommerce-test/blob/dev/notebook/sales_predict.ipynb)


#### How to deploy the package

```sh
# pull the latest code into local
$ git pull origin develop
# merge this to main branch
$ git merge main
# create the tag on main branch
$ git tag vX.X.X (e.g. git tag v0.0.1)
# push the tag to GitHub
$ git push origin vX.X.X (e.g. git push origin v0.0.1)
```

GitHub Actions run after the pushing and request the approval from code owner automatically. Once it is approved, the package will be automatically released.
