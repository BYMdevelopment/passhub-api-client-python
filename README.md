# PassHub API Client

PassHub API documentation

Access PassHub with Python. This module offers high level and low level calls to the API.


## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install sightseeingtech_passhub_api
```
(you may need to run `pip` with root permission: `sudo pip install sightseeingtech_passhub_api`)

Then import the package:
```python
import sightseeingtech_passhub_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sightseeingtech_passhub_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import sightseeingtech_passhub_api
from sightseeingtech_passhub_api.rest import ApiException
from pprint import pprint

configuration = Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
configuration.host = 'YOUR_HOST'
configuration.verify_ssl = False

client = ApiClient(configuration)

try:
    productResourceApi = sightseeingtech_passhub_api.ProductResourceApi(client)

    print('Loading products...')

    products = productResourceApi.get_all_products()

    print('Product %d products is/are loaded.\n' % len(products))
except ApiException as e:
    print("Exception when calling ProductResourceApi->get_all_products: %s\n" % e)

```

## Documentation for API Endpoints


Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OrderRecordResourceApi* | **createOrderRecord** | **POST** /api/v1/orderRecords | createOrderRecord
*OrderRecordResourceApi* | **getAllOrderRecords** | **GET** /api/v2/orderRecords | getAllOrderRecords
*OrderRecordResourceApi* | **getOrderRecord** | **GET** /api/v1/orderRecords/{id} | getOrderRecord
*OrderRecordResourceApi* | **mergeVouchers** | **POST** /api/v1/orderRecords/mergeVouchers | mergeVouchers
*OrderRecordResourceApi* | **updateOrderRecord**) | **PUT** /api/v1/orderRecords | updateOrderRecord
*ProductResourceApi* | **findProductsByVendor** | **GET** /api/v1/products/vendor/{vendorId} | findProductsByVendor
*ProductResourceApi* | **getAllProducts** | **GET** /api/v2/products | getAllProducts
*VendorResourceApi* | **getAllVendors** | **GET** /api/v2/vendors | getAllVendors
*VoucherResourceApi* | **cancelValidation** | **POST** /api/v2/voucher/validate/cancel | V2 Cancel validation for the voucher
*VoucherResourceApi* | **cancelVoucher** | **POST** /api/v1/voucher/cancel | cancelVoucher
*VoucherResourceApi* | **convertVoucher** | **POST** /api/v1/voucher/convert | convertVoucher
*VoucherResourceApi* | **validateVoucher** | **POST** /api/v2/voucher/validate | [V2 Validates voucher which represents single order item or group of them.


## Documentation For Authorization


## X-Api-Key

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header

