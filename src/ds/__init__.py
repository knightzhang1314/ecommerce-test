from importlib.metadata import PackageNotFoundError, version

try:
    # Read version from PKG metadata
    __version__ = version("ds")
except PackageNotFoundError:
    __version__ = "0.0.0"  # fall-back version
