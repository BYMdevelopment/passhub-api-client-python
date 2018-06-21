# passhubapi.VoucherResourceApi

All URIs are relative to *https://localhost:8090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_validation**](VoucherResourceApi.md#cancel_validation) | **POST** /api/v2/voucher/validate/cancel | [V2] Cancel validation for the voucher
[**cancel_voucher**](VoucherResourceApi.md#cancel_voucher) | **POST** /api/v1/voucher/cancel | cancelVoucher
[**convert_voucher**](VoucherResourceApi.md#convert_voucher) | **POST** /api/v1/voucher/convert | convertVoucher
[**validate_voucher**](VoucherResourceApi.md#validate_voucher) | **POST** /api/v2/voucher/validate | [V2] Validates voucher which represents single order item or group of them.


# **cancel_validation**
> GenericStatusDTO cancel_validation(transaction_tag, reason=reason, note=note)

[V2] Cancel validation for the voucher

Required permissions: CAN_CANCEL_VALIDATION

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
api_instance = passhubapi.VoucherResourceApi(passhubapi.ApiClient(configuration))
transaction_tag = 'transaction_tag_example' # str | the transaction tag of validation
reason = 'reason_example' # str | the reason of validation (optional)
note = passhubapi.OrderNoteParamDTO() # OrderNoteParamDTO | the validation note dto (optional)

try:
    # [V2] Cancel validation for the voucher
    api_response = api_instance.cancel_validation(transaction_tag, reason=reason, note=note)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoucherResourceApi->cancel_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_tag** | **str**| the transaction tag of validation | 
 **reason** | **str**| the reason of validation | [optional] 
 **note** | [**OrderNoteParamDTO**](OrderNoteParamDTO.md)| the validation note dto | [optional] 

### Return type

[**GenericStatusDTO**](GenericStatusDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_voucher**
> GenericStatusDTO cancel_voucher(order_id, voucher_id=voucher_id, note=note)

cancelVoucher

Required permissions: CAN_CANCEL_ORDER

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
api_instance = passhubapi.VoucherResourceApi(passhubapi.ApiClient(configuration))
order_id = 789 # int | the internal id of order
voucher_id = 'voucher_id_example' # str | the voucher id (optional)
note = passhubapi.OrderNoteParamDTO() # OrderNoteParamDTO | the voucher note dto (optional)

try:
    # cancelVoucher
    api_response = api_instance.cancel_voucher(order_id, voucher_id=voucher_id, note=note)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoucherResourceApi->cancel_voucher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| the internal id of order | 
 **voucher_id** | **str**| the voucher id | [optional] 
 **note** | [**OrderNoteParamDTO**](OrderNoteParamDTO.md)| the voucher note dto | [optional] 

### Return type

[**GenericStatusDTO**](GenericStatusDTO.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **convert_voucher**
> JSONObject convert_voucher(old_voucher_id, new_voucher_id)

convertVoucher

Required permissions: CAN_CONVERT_VOUCHER

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
api_instance = passhubapi.VoucherResourceApi(passhubapi.ApiClient(configuration))
old_voucher_id = 'old_voucher_id_example' # str | the old voucher id
new_voucher_id = 'new_voucher_id_example' # str | the new voucher id

try:
    # convertVoucher
    api_response = api_instance.convert_voucher(old_voucher_id, new_voucher_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoucherResourceApi->convert_voucher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_voucher_id** | **str**| the old voucher id | 
 **new_voucher_id** | **str**| the new voucher id | 

### Return type

[**JSONObject**](JSONObject.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_voucher**
> ValidationResult validate_voucher(validation_id, vendor_id, product_tag=product_tag, order_item_ids=order_item_ids, skip_expiry_check=skip_expiry_check, extra_param_dto=extra_param_dto)

[V2] Validates voucher which represents single order item or group of them.

Required permissions: CAN_VALIDATE;

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
api_instance = passhubapi.VoucherResourceApi(passhubapi.ApiClient(configuration))
validation_id = 'validation_id_example' # str | the voucher validation id
vendor_id = 789 # int | the internal id of vendor
product_tag = 'product_tag_example' # str | the product tag (optional)
order_item_ids = [56] # list[int] | the array of order item ids (optional)
skip_expiry_check = true # bool | flag to skip expiry check within strategy (optional)
extra_param_dto = passhubapi.ExtraValidationParamDTO() # ExtraValidationParamDTO | the validation extra params dto (optional)

try:
    # [V2] Validates voucher which represents single order item or group of them.
    api_response = api_instance.validate_voucher(validation_id, vendor_id, product_tag=product_tag, order_item_ids=order_item_ids, skip_expiry_check=skip_expiry_check, extra_param_dto=extra_param_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoucherResourceApi->validate_voucher: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_id** | **str**| the voucher validation id | 
 **vendor_id** | **int**| the internal id of vendor | 
 **product_tag** | **str**| the product tag | [optional] 
 **order_item_ids** | [**list[int]**](int.md)| the array of order item ids | [optional] 
 **skip_expiry_check** | **bool**| flag to skip expiry check within strategy | [optional] 
 **extra_param_dto** | [**ExtraValidationParamDTO**](ExtraValidationParamDTO.md)| the validation extra params dto | [optional] 

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

