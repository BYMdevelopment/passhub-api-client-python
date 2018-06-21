# passhubapi.VendorResourceApi

All URIs are relative to *https://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_vendors**](VendorResourceApi.md#get_all_vendors) | **GET** /api/v2/vendors | getAllVendors


# **get_all_vendors**
> list[VendorDetailDTO] get_all_vendors(query=query, size=size, page=page, sort_by=sort_by, sort_order=sort_order)

getAllVendors

Required permissions: CAN_GET_VENDORS

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
api_instance = passhubapi.VendorResourceApi(passhubapi.ApiClient(configuration))
query = 'query_example' # str | query text (optional)
size = 56 # int | quantity of listed records on page (optional)
page = 56 # int | listing starts from page value (optional)
sort_by = 'sort_by_example' # str | sort by (optional)
sort_order = 'sort_order_example' # str | sort order (optional)

try:
    # getAllVendors
    api_response = api_instance.get_all_vendors(query=query, size=size, page=page, sort_by=sort_by, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorResourceApi->get_all_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| query text | [optional] 
 **size** | **int**| quantity of listed records on page | [optional] 
 **page** | **int**| listing starts from page value | [optional] 
 **sort_by** | **str**| sort by | [optional] 
 **sort_order** | **str**| sort order | [optional] 

### Return type

[**list[VendorDetailDTO]**](VendorDetailDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

