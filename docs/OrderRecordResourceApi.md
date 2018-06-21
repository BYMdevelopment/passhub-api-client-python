# passhubapi.OrderRecordResourceApi

All URIs are relative to *https://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_order_record**](OrderRecordResourceApi.md#create_order_record) | **POST** /api/v1/orderRecords | createOrderRecord
[**get_all_order_records**](OrderRecordResourceApi.md#get_all_order_records) | **GET** /api/v2/orderRecords | getAllOrderRecords
[**get_order_record**](OrderRecordResourceApi.md#get_order_record) | **GET** /api/v1/orderRecords/{id} | getOrderRecord
[**merge_vouchers**](OrderRecordResourceApi.md#merge_vouchers) | **POST** /api/v1/orderRecords/mergeVouchers | mergeVouchers
[**update_order_record**](OrderRecordResourceApi.md#update_order_record) | **PUT** /api/v1/orderRecords | updateOrderRecord


# **create_order_record**
> OrderRecordDTO create_order_record(order_record_dto)

createOrderRecord

1) Cellphone number must be in E.164 format;<br/>2) «PricePaid» is a price for 1 product;<br/>3) Required permissions: CAN_CREATE_ORDER.

### Example
```python
from __future__ import print_function
import time
import passhubapi
from passhubapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Api-Key
configuration = passhubapi.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = passhubapi.OrderRecordResourceApi(passhubapi.ApiClient(configuration))
order_record_dto = passhubapi.OrderRecordDTO() # OrderRecordDTO | the OrderRecord Dto

try:
    # createOrderRecord
    api_response = api_instance.create_order_record(order_record_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderRecordResourceApi->create_order_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_record_dto** | [**OrderRecordDTO**](OrderRecordDTO.md)| the OrderRecord Dto | 

### Return type

[**OrderRecordDTO**](OrderRecordDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_order_records**
> list[OrderRecordExtendDTO] get_all_order_records(query=query, _from=_from, till=till, time_zone=time_zone, delivery_method=delivery_method, delivery_status=delivery_status, size=size, page=page, sort_by=sort_by, sort_order=sort_order)

getAllOrderRecords

Required permissions: CAN_GET_ORDERS

### Example
```python
from __future__ import print_function
import time
import passhubapi
from passhubapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Api-Key
configuration = passhubapi.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = passhubapi.OrderRecordResourceApi(passhubapi.ApiClient(configuration))
query = 'query_example' # str | query text (optional)
_from = '_from_example' # str | Begin the of date range, format: YYYY-MM-DD (e.g. 2016-01-25) (optional)
till = 'till_example' # str | End the of date range, format: YYYY-MM-DD (e.g. 2016-01-25) (optional)
time_zone = 'time_zone_example' # str | A timezone for date/time representation. Example: America/Chicago or EST. If zone is not set, then UTC timezone will be used. (optional)
delivery_method = 'delivery_method_example' # str | delivery method (optional)
delivery_status = 'delivery_status_example' # str | status of delivery (optional)
size = 56 # int | quantity of listed records on page (optional)
page = 56 # int | listing starts from page value (optional)
sort_by = 'sort_by_example' # str | sort by (optional)
sort_order = 'sort_order_example' # str | sort order (optional)

try:
    # getAllOrderRecords
    api_response = api_instance.get_all_order_records(query=query, _from=_from, till=till, time_zone=time_zone, delivery_method=delivery_method, delivery_status=delivery_status, size=size, page=page, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderRecordResourceApi->get_all_order_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query text | [optional] 
 **_from** | **str**| Begin the of date range, format: YYYY-MM-DD (e.g. 2016-01-25) | [optional] 
 **till** | **str**| End the of date range, format: YYYY-MM-DD (e.g. 2016-01-25) | [optional] 
 **time_zone** | **str**| A timezone for date/time representation. Example: America/Chicago or EST. If zone is not set, then UTC timezone will be used. | [optional] 
 **delivery_method** | **str**| delivery method | [optional] 
 **delivery_status** | **str**| status of delivery | [optional] 
 **size** | **int**| quantity of listed records on page | [optional] 
 **page** | **int**| listing starts from page value | [optional] 
 **sort_by** | **str**| sort by | [optional] 
 **sort_order** | **str**| sort order | [optional] 

### Return type

[**list[OrderRecordExtendDTO]**](OrderRecordExtendDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_record**
> OrderRecordExtendDTO get_order_record(id)

getOrderRecord

Required permissions: CAN_GET_ORDERS

### Example
```python
from __future__ import print_function
import time
import passhubapi
from passhubapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Api-Key
configuration = passhubapi.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = passhubapi.OrderRecordResourceApi(passhubapi.ApiClient(configuration))
id = 789 # int | the internal id of order

try:
    # getOrderRecord
    api_response = api_instance.get_order_record(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderRecordResourceApi->get_order_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| the internal id of order | 

### Return type

[**OrderRecordExtendDTO**](OrderRecordExtendDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_vouchers**
> GenericStatusDTO merge_vouchers(order_id, new_voucher_id)

mergeVouchers

Replaces voucher IDs of order items with new voucher ID in the specified order. All groups are merged to one 'MergedGroup'.<br/>Required permissions: CAN_EDIT_ORDER

### Example
```python
from __future__ import print_function
import time
import passhubapi
from passhubapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Api-Key
configuration = passhubapi.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = passhubapi.OrderRecordResourceApi(passhubapi.ApiClient(configuration))
order_id = 789 # int | the internal id of order
new_voucher_id = 'new_voucher_id_example' # str | newVoucherId

try:
    # mergeVouchers
    api_response = api_instance.merge_vouchers(order_id, new_voucher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderRecordResourceApi->merge_vouchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| the internal id of order | 
 **new_voucher_id** | **str**| newVoucherId | 

### Return type

[**GenericStatusDTO**](GenericStatusDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_record**
> OrderRecordDTO update_order_record(order_record_dto)

updateOrderRecord

1) Cellphone number must be in E.164 format;<br/>2) «PricePaid» is a price for 1 product;<br/>3) Required permissions: CAN_EDIT_ORDER.

### Example
```python
from __future__ import print_function
import time
import passhubapi
from passhubapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: X-Api-Key
configuration = passhubapi.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = passhubapi.OrderRecordResourceApi(passhubapi.ApiClient(configuration))
order_record_dto = passhubapi.OrderRecordDTO() # OrderRecordDTO | the OrderRecord Dto

try:
    # updateOrderRecord
    api_response = api_instance.update_order_record(order_record_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrderRecordResourceApi->update_order_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_record_dto** | [**OrderRecordDTO**](OrderRecordDTO.md)| the OrderRecord Dto | 

### Return type

[**OrderRecordDTO**](OrderRecordDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

