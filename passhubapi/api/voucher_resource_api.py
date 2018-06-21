# coding: utf-8

"""
    PassHub API

    PassHub API documentation  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from passhubapi.api_client import ApiClient


class VoucherResourceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cancel_validation(self, transaction_tag, **kwargs):  # noqa: E501
        """[V2] Cancel validation for the voucher  # noqa: E501

        Required permissions: CAN_CANCEL_VALIDATION  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_validation(transaction_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str transaction_tag: the transaction tag of validation (required)
        :param str reason: the reason of validation
        :param OrderNoteParamDTO note: the validation note dto
        :return: GenericStatusDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.cancel_validation_with_http_info(transaction_tag, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_validation_with_http_info(transaction_tag, **kwargs)  # noqa: E501
            return data

    def cancel_validation_with_http_info(self, transaction_tag, **kwargs):  # noqa: E501
        """[V2] Cancel validation for the voucher  # noqa: E501

        Required permissions: CAN_CANCEL_VALIDATION  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_validation_with_http_info(transaction_tag, async=True)
        >>> result = thread.get()

        :param async bool
        :param str transaction_tag: the transaction tag of validation (required)
        :param str reason: the reason of validation
        :param OrderNoteParamDTO note: the validation note dto
        :return: GenericStatusDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_tag', 'reason', 'note']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_validation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transaction_tag' is set
        if ('transaction_tag' not in params or
                params['transaction_tag'] is None):
            raise ValueError("Missing the required parameter `transaction_tag` when calling `cancel_validation`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'transaction_tag' in params:
            query_params.append(('transactionTag', params['transaction_tag']))  # noqa: E501
        if 'reason' in params:
            query_params.append(('reason', params['reason']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'note' in params:
            body_params = params['note']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/voucher/validate/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GenericStatusDTO',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_voucher(self, order_id, **kwargs):  # noqa: E501
        """cancelVoucher  # noqa: E501

        Required permissions: CAN_CANCEL_ORDER  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_voucher(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int order_id: the internal id of order (required)
        :param str voucher_id: the voucher id
        :param OrderNoteParamDTO note: the voucher note dto
        :return: GenericStatusDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.cancel_voucher_with_http_info(order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.cancel_voucher_with_http_info(order_id, **kwargs)  # noqa: E501
            return data

    def cancel_voucher_with_http_info(self, order_id, **kwargs):  # noqa: E501
        """cancelVoucher  # noqa: E501

        Required permissions: CAN_CANCEL_ORDER  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.cancel_voucher_with_http_info(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int order_id: the internal id of order (required)
        :param str voucher_id: the voucher id
        :param OrderNoteParamDTO note: the voucher note dto
        :return: GenericStatusDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'voucher_id', 'note']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_voucher" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `cancel_voucher`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))  # noqa: E501
        if 'voucher_id' in params:
            query_params.append(('voucherId', params['voucher_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'note' in params:
            body_params = params['note']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/voucher/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GenericStatusDTO',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def convert_voucher(self, old_voucher_id, new_voucher_id, **kwargs):  # noqa: E501
        """convertVoucher  # noqa: E501

        Required permissions: CAN_CONVERT_VOUCHER  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.convert_voucher(old_voucher_id, new_voucher_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str old_voucher_id: the old voucher id (required)
        :param str new_voucher_id: the new voucher id (required)
        :return: JSONObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.convert_voucher_with_http_info(old_voucher_id, new_voucher_id, **kwargs)  # noqa: E501
        else:
            (data) = self.convert_voucher_with_http_info(old_voucher_id, new_voucher_id, **kwargs)  # noqa: E501
            return data

    def convert_voucher_with_http_info(self, old_voucher_id, new_voucher_id, **kwargs):  # noqa: E501
        """convertVoucher  # noqa: E501

        Required permissions: CAN_CONVERT_VOUCHER  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.convert_voucher_with_http_info(old_voucher_id, new_voucher_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str old_voucher_id: the old voucher id (required)
        :param str new_voucher_id: the new voucher id (required)
        :return: JSONObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['old_voucher_id', 'new_voucher_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method convert_voucher" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'old_voucher_id' is set
        if ('old_voucher_id' not in params or
                params['old_voucher_id'] is None):
            raise ValueError("Missing the required parameter `old_voucher_id` when calling `convert_voucher`")  # noqa: E501
        # verify the required parameter 'new_voucher_id' is set
        if ('new_voucher_id' not in params or
                params['new_voucher_id'] is None):
            raise ValueError("Missing the required parameter `new_voucher_id` when calling `convert_voucher`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'old_voucher_id' in params:
            query_params.append(('oldVoucherId', params['old_voucher_id']))  # noqa: E501
        if 'new_voucher_id' in params:
            query_params.append(('newVoucherId', params['new_voucher_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/voucher/convert', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JSONObject',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_voucher(self, validation_id, vendor_id, **kwargs):  # noqa: E501
        """[V2] Validates voucher which represents single order item or group of them.  # noqa: E501

        Required permissions: CAN_VALIDATE;  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.validate_voucher(validation_id, vendor_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str validation_id: the voucher validation id (required)
        :param int vendor_id: the internal id of vendor (required)
        :param str product_tag: the product tag
        :param list[int] order_item_ids: the array of order item ids
        :param bool skip_expiry_check: flag to skip expiry check within strategy
        :param ExtraValidationParamDTO extra_param_dto: the validation extra params dto
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.validate_voucher_with_http_info(validation_id, vendor_id, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_voucher_with_http_info(validation_id, vendor_id, **kwargs)  # noqa: E501
            return data

    def validate_voucher_with_http_info(self, validation_id, vendor_id, **kwargs):  # noqa: E501
        """[V2] Validates voucher which represents single order item or group of them.  # noqa: E501

        Required permissions: CAN_VALIDATE;  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.validate_voucher_with_http_info(validation_id, vendor_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str validation_id: the voucher validation id (required)
        :param int vendor_id: the internal id of vendor (required)
        :param str product_tag: the product tag
        :param list[int] order_item_ids: the array of order item ids
        :param bool skip_expiry_check: flag to skip expiry check within strategy
        :param ExtraValidationParamDTO extra_param_dto: the validation extra params dto
        :return: ValidationResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['validation_id', 'vendor_id', 'product_tag', 'order_item_ids', 'skip_expiry_check', 'extra_param_dto']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_voucher" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'validation_id' is set
        if ('validation_id' not in params or
                params['validation_id'] is None):
            raise ValueError("Missing the required parameter `validation_id` when calling `validate_voucher`")  # noqa: E501
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params or
                params['vendor_id'] is None):
            raise ValueError("Missing the required parameter `vendor_id` when calling `validate_voucher`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'validation_id' in params:
            query_params.append(('validationId', params['validation_id']))  # noqa: E501
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))  # noqa: E501
        if 'product_tag' in params:
            query_params.append(('productTag', params['product_tag']))  # noqa: E501
        if 'order_item_ids' in params:
            query_params.append(('orderItemIds', params['order_item_ids']))  # noqa: E501
            collection_formats['orderItemIds'] = 'csv'  # noqa: E501
        if 'skip_expiry_check' in params:
            query_params.append(('skipExpiryCheck', params['skip_expiry_check']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'extra_param_dto' in params:
            body_params = params['extra_param_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Api-Key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/voucher/validate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ValidationResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
