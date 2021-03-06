# coding: utf-8

"""
    PassHub API

    PassHub API documentation  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from sightseeingtech_passhub_api.models.product_suggestion import ProductSuggestion  # noqa: F401,E501
from sightseeingtech_passhub_api.models.recharge_prompt import RechargePrompt  # noqa: F401,E501
from sightseeingtech_passhub_api.models.suggested_order import SuggestedOrder  # noqa: F401,E501
from sightseeingtech_passhub_api.models.universal_attribute import UniversalAttribute  # noqa: F401,E501
from sightseeingtech_passhub_api.models.validation_result_entry import ValidationResultEntry  # noqa: F401,E501


class ValidationResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_skip_expiry_check': 'bool',
        'contract_holder_id': 'str',
        'contract_holder_name': 'str',
        'error_code': 'str',
        'extra': 'dict(str, str)',
        'meta': 'list[UniversalAttribute]',
        'print_status': 'str',
        'recharge': 'RechargePrompt',
        'status': 'str',
        'suggested_order_items': 'list[SuggestedOrder]',
        'suggested_products': 'list[ProductSuggestion]',
        'transaction_tag': 'str',
        'validation': 'list[ValidationResultEntry]',
        'validation_date': 'str',
        'voucher_id': 'str',
        'waiting_period_pending': 'int'
    }

    attribute_map = {
        'can_skip_expiry_check': 'canSkipExpiryCheck',
        'contract_holder_id': 'contractHolderId',
        'contract_holder_name': 'contractHolderName',
        'error_code': 'errorCode',
        'extra': 'extra',
        'meta': 'meta',
        'print_status': 'printStatus',
        'recharge': 'recharge',
        'status': 'status',
        'suggested_order_items': 'suggestedOrderItems',
        'suggested_products': 'suggestedProducts',
        'transaction_tag': 'transactionTag',
        'validation': 'validation',
        'validation_date': 'validationDate',
        'voucher_id': 'voucherId',
        'waiting_period_pending': 'waitingPeriodPending'
    }

    def __init__(self, can_skip_expiry_check=None, contract_holder_id=None, contract_holder_name=None, error_code=None, extra=None, meta=None, print_status=None, recharge=None, status=None, suggested_order_items=None, suggested_products=None, transaction_tag=None, validation=None, validation_date=None, voucher_id=None, waiting_period_pending=None):  # noqa: E501
        """ValidationResult - a model defined in Swagger"""  # noqa: E501

        self._can_skip_expiry_check = None
        self._contract_holder_id = None
        self._contract_holder_name = None
        self._error_code = None
        self._extra = None
        self._meta = None
        self._print_status = None
        self._recharge = None
        self._status = None
        self._suggested_order_items = None
        self._suggested_products = None
        self._transaction_tag = None
        self._validation = None
        self._validation_date = None
        self._voucher_id = None
        self._waiting_period_pending = None
        self.discriminator = None

        if can_skip_expiry_check is not None:
            self.can_skip_expiry_check = can_skip_expiry_check
        if contract_holder_id is not None:
            self.contract_holder_id = contract_holder_id
        if contract_holder_name is not None:
            self.contract_holder_name = contract_holder_name
        if error_code is not None:
            self.error_code = error_code
        if extra is not None:
            self.extra = extra
        if meta is not None:
            self.meta = meta
        if print_status is not None:
            self.print_status = print_status
        if recharge is not None:
            self.recharge = recharge
        if status is not None:
            self.status = status
        if suggested_order_items is not None:
            self.suggested_order_items = suggested_order_items
        if suggested_products is not None:
            self.suggested_products = suggested_products
        if transaction_tag is not None:
            self.transaction_tag = transaction_tag
        if validation is not None:
            self.validation = validation
        if validation_date is not None:
            self.validation_date = validation_date
        if voucher_id is not None:
            self.voucher_id = voucher_id
        if waiting_period_pending is not None:
            self.waiting_period_pending = waiting_period_pending

    @property
    def can_skip_expiry_check(self):
        """Gets the can_skip_expiry_check of this ValidationResult.  # noqa: E501


        :return: The can_skip_expiry_check of this ValidationResult.  # noqa: E501
        :rtype: bool
        """
        return self._can_skip_expiry_check

    @can_skip_expiry_check.setter
    def can_skip_expiry_check(self, can_skip_expiry_check):
        """Sets the can_skip_expiry_check of this ValidationResult.


        :param can_skip_expiry_check: The can_skip_expiry_check of this ValidationResult.  # noqa: E501
        :type: bool
        """

        self._can_skip_expiry_check = can_skip_expiry_check

    @property
    def contract_holder_id(self):
        """Gets the contract_holder_id of this ValidationResult.  # noqa: E501


        :return: The contract_holder_id of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._contract_holder_id

    @contract_holder_id.setter
    def contract_holder_id(self, contract_holder_id):
        """Sets the contract_holder_id of this ValidationResult.


        :param contract_holder_id: The contract_holder_id of this ValidationResult.  # noqa: E501
        :type: str
        """

        self._contract_holder_id = contract_holder_id

    @property
    def contract_holder_name(self):
        """Gets the contract_holder_name of this ValidationResult.  # noqa: E501


        :return: The contract_holder_name of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._contract_holder_name

    @contract_holder_name.setter
    def contract_holder_name(self, contract_holder_name):
        """Sets the contract_holder_name of this ValidationResult.


        :param contract_holder_name: The contract_holder_name of this ValidationResult.  # noqa: E501
        :type: str
        """

        self._contract_holder_name = contract_holder_name

    @property
    def error_code(self):
        """Gets the error_code of this ValidationResult.  # noqa: E501


        :return: The error_code of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ValidationResult.


        :param error_code: The error_code of this ValidationResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["VALIDATION_ID_NOT_FOUND", "REQUESTED_PRODUCT_NOT_FOUND", "REQUESTED_PRODUCT_USED", "VALIDATION_FAILED", "INSUFFICIENT_CURRENCY_AMOUNT", "NOT_VALIDATABLE_PRODUCT", "MAX_NUMBER_OF_USES_REACHED", "VOUCHER_EXPIRED", "VALIDATION_BLOCKED_DATES", "VALIDATION_BLOCKED_TIME", "VALIDATION_BLOCKED_DAYS", "SYSTEMS_SYNC_FAILED", "VALIDATIONS_PER_DAY_EXCEEDED", "WAITING_PERIOD_NOT_EXPIRED"]  # noqa: E501
        if error_code not in allowed_values:
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(error_code, allowed_values)
            )

        self._error_code = error_code

    @property
    def extra(self):
        """Gets the extra of this ValidationResult.  # noqa: E501


        :return: The extra of this ValidationResult.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this ValidationResult.


        :param extra: The extra of this ValidationResult.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra = extra

    @property
    def meta(self):
        """Gets the meta of this ValidationResult.  # noqa: E501


        :return: The meta of this ValidationResult.  # noqa: E501
        :rtype: list[UniversalAttribute]
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ValidationResult.


        :param meta: The meta of this ValidationResult.  # noqa: E501
        :type: list[UniversalAttribute]
        """

        self._meta = meta

    @property
    def print_status(self):
        """Gets the print_status of this ValidationResult.  # noqa: E501


        :return: The print_status of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._print_status

    @print_status.setter
    def print_status(self, print_status):
        """Sets the print_status of this ValidationResult.


        :param print_status: The print_status of this ValidationResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["NOT_PRINTABLE", "PRINTED", "NEED_PRINTING"]  # noqa: E501
        if print_status not in allowed_values:
            raise ValueError(
                "Invalid value for `print_status` ({0}), must be one of {1}"  # noqa: E501
                .format(print_status, allowed_values)
            )

        self._print_status = print_status

    @property
    def recharge(self):
        """Gets the recharge of this ValidationResult.  # noqa: E501


        :return: The recharge of this ValidationResult.  # noqa: E501
        :rtype: RechargePrompt
        """
        return self._recharge

    @recharge.setter
    def recharge(self, recharge):
        """Sets the recharge of this ValidationResult.


        :param recharge: The recharge of this ValidationResult.  # noqa: E501
        :type: RechargePrompt
        """

        self._recharge = recharge

    @property
    def status(self):
        """Gets the status of this ValidationResult.  # noqa: E501


        :return: The status of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ValidationResult.


        :param status: The status of this ValidationResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUCCESS", "CLARIFY", "FAILURE", "CLARIFY_ORDER", "CLARIFY_ITEM"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def suggested_order_items(self):
        """Gets the suggested_order_items of this ValidationResult.  # noqa: E501


        :return: The suggested_order_items of this ValidationResult.  # noqa: E501
        :rtype: list[SuggestedOrder]
        """
        return self._suggested_order_items

    @suggested_order_items.setter
    def suggested_order_items(self, suggested_order_items):
        """Sets the suggested_order_items of this ValidationResult.


        :param suggested_order_items: The suggested_order_items of this ValidationResult.  # noqa: E501
        :type: list[SuggestedOrder]
        """

        self._suggested_order_items = suggested_order_items

    @property
    def suggested_products(self):
        """Gets the suggested_products of this ValidationResult.  # noqa: E501


        :return: The suggested_products of this ValidationResult.  # noqa: E501
        :rtype: list[ProductSuggestion]
        """
        return self._suggested_products

    @suggested_products.setter
    def suggested_products(self, suggested_products):
        """Sets the suggested_products of this ValidationResult.


        :param suggested_products: The suggested_products of this ValidationResult.  # noqa: E501
        :type: list[ProductSuggestion]
        """

        self._suggested_products = suggested_products

    @property
    def transaction_tag(self):
        """Gets the transaction_tag of this ValidationResult.  # noqa: E501


        :return: The transaction_tag of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._transaction_tag

    @transaction_tag.setter
    def transaction_tag(self, transaction_tag):
        """Sets the transaction_tag of this ValidationResult.


        :param transaction_tag: The transaction_tag of this ValidationResult.  # noqa: E501
        :type: str
        """

        self._transaction_tag = transaction_tag

    @property
    def validation(self):
        """Gets the validation of this ValidationResult.  # noqa: E501


        :return: The validation of this ValidationResult.  # noqa: E501
        :rtype: list[ValidationResultEntry]
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this ValidationResult.


        :param validation: The validation of this ValidationResult.  # noqa: E501
        :type: list[ValidationResultEntry]
        """

        self._validation = validation

    @property
    def validation_date(self):
        """Gets the validation_date of this ValidationResult.  # noqa: E501


        :return: The validation_date of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._validation_date

    @validation_date.setter
    def validation_date(self, validation_date):
        """Sets the validation_date of this ValidationResult.


        :param validation_date: The validation_date of this ValidationResult.  # noqa: E501
        :type: str
        """

        self._validation_date = validation_date

    @property
    def voucher_id(self):
        """Gets the voucher_id of this ValidationResult.  # noqa: E501


        :return: The voucher_id of this ValidationResult.  # noqa: E501
        :rtype: str
        """
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, voucher_id):
        """Sets the voucher_id of this ValidationResult.


        :param voucher_id: The voucher_id of this ValidationResult.  # noqa: E501
        :type: str
        """

        self._voucher_id = voucher_id

    @property
    def waiting_period_pending(self):
        """Gets the waiting_period_pending of this ValidationResult.  # noqa: E501


        :return: The waiting_period_pending of this ValidationResult.  # noqa: E501
        :rtype: int
        """
        return self._waiting_period_pending

    @waiting_period_pending.setter
    def waiting_period_pending(self, waiting_period_pending):
        """Sets the waiting_period_pending of this ValidationResult.


        :param waiting_period_pending: The waiting_period_pending of this ValidationResult.  # noqa: E501
        :type: int
        """

        self._waiting_period_pending = waiting_period_pending

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValidationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
