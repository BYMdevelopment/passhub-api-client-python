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

from sightseeingtech_passhub_api.models.simple_metadata import SimpleMetadata  # noqa: F401,E501
from sightseeingtech_passhub_api.models.simple_product_dto import SimpleProductDTO  # noqa: F401,E501
from sightseeingtech_passhub_api.models.user_dto import UserDTO  # noqa: F401,E501


class OrderItem(object):
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
        'alias_voucher_ids': 'list[str]',
        'contract_holder_id': 'str',
        'contract_holder_name': 'str',
        'customer_company': 'str',
        'customer_email': 'str',
        'customer_name': 'str',
        'customer_uid': 'str',
        'expire_date': 'str',
        'expiry_date_before_validtion': 'str',
        'group_name': 'str',
        'id': 'int',
        'init_voucher_id': 'str',
        'is_canceled': 'bool',
        'is_validated': 'bool',
        'metadata': 'SimpleMetadata',
        'originator_voucher_id': 'str',
        'price_paid': 'float',
        'product': 'SimpleProductDTO',
        'quantity': 'int',
        'sku': 'str',
        'tour_date': 'str',
        'updated': 'str',
        'updated_by': 'UserDTO',
        'validation_id': 'str',
        'vendor_voucher_id': 'str',
        'voucher_id': 'str'
    }

    attribute_map = {
        'alias_voucher_ids': 'aliasVoucherIds',
        'contract_holder_id': 'contractHolderId',
        'contract_holder_name': 'contractHolderName',
        'customer_company': 'customerCompany',
        'customer_email': 'customerEmail',
        'customer_name': 'customerName',
        'customer_uid': 'customerUid',
        'expire_date': 'expireDate',
        'expiry_date_before_validtion': 'expiryDateBeforeValidtion',
        'group_name': 'groupName',
        'id': 'id',
        'init_voucher_id': 'initVoucherId',
        'is_canceled': 'isCanceled',
        'is_validated': 'isValidated',
        'metadata': 'metadata',
        'originator_voucher_id': 'originatorVoucherId',
        'price_paid': 'pricePaid',
        'product': 'product',
        'quantity': 'quantity',
        'sku': 'sku',
        'tour_date': 'tourDate',
        'updated': 'updated',
        'updated_by': 'updatedBy',
        'validation_id': 'validationId',
        'vendor_voucher_id': 'vendorVoucherId',
        'voucher_id': 'voucherId'
    }

    def __init__(self, alias_voucher_ids=None, contract_holder_id=None, contract_holder_name=None, customer_company=None, customer_email=None, customer_name=None, customer_uid=None, expire_date=None, expiry_date_before_validtion=None, group_name=None, id=None, init_voucher_id=None, is_canceled=None, is_validated=None, metadata=None, originator_voucher_id=None, price_paid=None, product=None, quantity=None, sku=None, tour_date=None, updated=None, updated_by=None, validation_id=None, vendor_voucher_id=None, voucher_id=None):  # noqa: E501
        """OrderItem - a model defined in Swagger"""  # noqa: E501

        self._alias_voucher_ids = None
        self._contract_holder_id = None
        self._contract_holder_name = None
        self._customer_company = None
        self._customer_email = None
        self._customer_name = None
        self._customer_uid = None
        self._expire_date = None
        self._expiry_date_before_validtion = None
        self._group_name = None
        self._id = None
        self._init_voucher_id = None
        self._is_canceled = None
        self._is_validated = None
        self._metadata = None
        self._originator_voucher_id = None
        self._price_paid = None
        self._product = None
        self._quantity = None
        self._sku = None
        self._tour_date = None
        self._updated = None
        self._updated_by = None
        self._validation_id = None
        self._vendor_voucher_id = None
        self._voucher_id = None
        self.discriminator = None

        if alias_voucher_ids is not None:
            self.alias_voucher_ids = alias_voucher_ids
        if contract_holder_id is not None:
            self.contract_holder_id = contract_holder_id
        if contract_holder_name is not None:
            self.contract_holder_name = contract_holder_name
        if customer_company is not None:
            self.customer_company = customer_company
        if customer_email is not None:
            self.customer_email = customer_email
        if customer_name is not None:
            self.customer_name = customer_name
        if customer_uid is not None:
            self.customer_uid = customer_uid
        if expire_date is not None:
            self.expire_date = expire_date
        if expiry_date_before_validtion is not None:
            self.expiry_date_before_validtion = expiry_date_before_validtion
        if group_name is not None:
            self.group_name = group_name
        if id is not None:
            self.id = id
        if init_voucher_id is not None:
            self.init_voucher_id = init_voucher_id
        if is_canceled is not None:
            self.is_canceled = is_canceled
        if is_validated is not None:
            self.is_validated = is_validated
        if metadata is not None:
            self.metadata = metadata
        if originator_voucher_id is not None:
            self.originator_voucher_id = originator_voucher_id
        if price_paid is not None:
            self.price_paid = price_paid
        if product is not None:
            self.product = product
        if quantity is not None:
            self.quantity = quantity
        if sku is not None:
            self.sku = sku
        if tour_date is not None:
            self.tour_date = tour_date
        if updated is not None:
            self.updated = updated
        if updated_by is not None:
            self.updated_by = updated_by
        if validation_id is not None:
            self.validation_id = validation_id
        if vendor_voucher_id is not None:
            self.vendor_voucher_id = vendor_voucher_id
        if voucher_id is not None:
            self.voucher_id = voucher_id

    @property
    def alias_voucher_ids(self):
        """Gets the alias_voucher_ids of this OrderItem.  # noqa: E501


        :return: The alias_voucher_ids of this OrderItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._alias_voucher_ids

    @alias_voucher_ids.setter
    def alias_voucher_ids(self, alias_voucher_ids):
        """Sets the alias_voucher_ids of this OrderItem.


        :param alias_voucher_ids: The alias_voucher_ids of this OrderItem.  # noqa: E501
        :type: list[str]
        """

        self._alias_voucher_ids = alias_voucher_ids

    @property
    def contract_holder_id(self):
        """Gets the contract_holder_id of this OrderItem.  # noqa: E501


        :return: The contract_holder_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._contract_holder_id

    @contract_holder_id.setter
    def contract_holder_id(self, contract_holder_id):
        """Sets the contract_holder_id of this OrderItem.


        :param contract_holder_id: The contract_holder_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._contract_holder_id = contract_holder_id

    @property
    def contract_holder_name(self):
        """Gets the contract_holder_name of this OrderItem.  # noqa: E501


        :return: The contract_holder_name of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._contract_holder_name

    @contract_holder_name.setter
    def contract_holder_name(self, contract_holder_name):
        """Sets the contract_holder_name of this OrderItem.


        :param contract_holder_name: The contract_holder_name of this OrderItem.  # noqa: E501
        :type: str
        """

        self._contract_holder_name = contract_holder_name

    @property
    def customer_company(self):
        """Gets the customer_company of this OrderItem.  # noqa: E501


        :return: The customer_company of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._customer_company

    @customer_company.setter
    def customer_company(self, customer_company):
        """Sets the customer_company of this OrderItem.


        :param customer_company: The customer_company of this OrderItem.  # noqa: E501
        :type: str
        """

        self._customer_company = customer_company

    @property
    def customer_email(self):
        """Gets the customer_email of this OrderItem.  # noqa: E501


        :return: The customer_email of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        """Sets the customer_email of this OrderItem.


        :param customer_email: The customer_email of this OrderItem.  # noqa: E501
        :type: str
        """

        self._customer_email = customer_email

    @property
    def customer_name(self):
        """Gets the customer_name of this OrderItem.  # noqa: E501


        :return: The customer_name of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this OrderItem.


        :param customer_name: The customer_name of this OrderItem.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def customer_uid(self):
        """Gets the customer_uid of this OrderItem.  # noqa: E501


        :return: The customer_uid of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._customer_uid

    @customer_uid.setter
    def customer_uid(self, customer_uid):
        """Sets the customer_uid of this OrderItem.


        :param customer_uid: The customer_uid of this OrderItem.  # noqa: E501
        :type: str
        """

        self._customer_uid = customer_uid

    @property
    def expire_date(self):
        """Gets the expire_date of this OrderItem.  # noqa: E501


        :return: The expire_date of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this OrderItem.


        :param expire_date: The expire_date of this OrderItem.  # noqa: E501
        :type: str
        """

        self._expire_date = expire_date

    @property
    def expiry_date_before_validtion(self):
        """Gets the expiry_date_before_validtion of this OrderItem.  # noqa: E501


        :return: The expiry_date_before_validtion of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date_before_validtion

    @expiry_date_before_validtion.setter
    def expiry_date_before_validtion(self, expiry_date_before_validtion):
        """Sets the expiry_date_before_validtion of this OrderItem.


        :param expiry_date_before_validtion: The expiry_date_before_validtion of this OrderItem.  # noqa: E501
        :type: str
        """

        self._expiry_date_before_validtion = expiry_date_before_validtion

    @property
    def group_name(self):
        """Gets the group_name of this OrderItem.  # noqa: E501


        :return: The group_name of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this OrderItem.


        :param group_name: The group_name of this OrderItem.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def id(self):
        """Gets the id of this OrderItem.  # noqa: E501


        :return: The id of this OrderItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderItem.


        :param id: The id of this OrderItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def init_voucher_id(self):
        """Gets the init_voucher_id of this OrderItem.  # noqa: E501


        :return: The init_voucher_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._init_voucher_id

    @init_voucher_id.setter
    def init_voucher_id(self, init_voucher_id):
        """Sets the init_voucher_id of this OrderItem.


        :param init_voucher_id: The init_voucher_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._init_voucher_id = init_voucher_id

    @property
    def is_canceled(self):
        """Gets the is_canceled of this OrderItem.  # noqa: E501


        :return: The is_canceled of this OrderItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_canceled

    @is_canceled.setter
    def is_canceled(self, is_canceled):
        """Sets the is_canceled of this OrderItem.


        :param is_canceled: The is_canceled of this OrderItem.  # noqa: E501
        :type: bool
        """

        self._is_canceled = is_canceled

    @property
    def is_validated(self):
        """Gets the is_validated of this OrderItem.  # noqa: E501


        :return: The is_validated of this OrderItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_validated

    @is_validated.setter
    def is_validated(self, is_validated):
        """Sets the is_validated of this OrderItem.


        :param is_validated: The is_validated of this OrderItem.  # noqa: E501
        :type: bool
        """

        self._is_validated = is_validated

    @property
    def metadata(self):
        """Gets the metadata of this OrderItem.  # noqa: E501


        :return: The metadata of this OrderItem.  # noqa: E501
        :rtype: SimpleMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this OrderItem.


        :param metadata: The metadata of this OrderItem.  # noqa: E501
        :type: SimpleMetadata
        """

        self._metadata = metadata

    @property
    def originator_voucher_id(self):
        """Gets the originator_voucher_id of this OrderItem.  # noqa: E501


        :return: The originator_voucher_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._originator_voucher_id

    @originator_voucher_id.setter
    def originator_voucher_id(self, originator_voucher_id):
        """Sets the originator_voucher_id of this OrderItem.


        :param originator_voucher_id: The originator_voucher_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._originator_voucher_id = originator_voucher_id

    @property
    def price_paid(self):
        """Gets the price_paid of this OrderItem.  # noqa: E501


        :return: The price_paid of this OrderItem.  # noqa: E501
        :rtype: float
        """
        return self._price_paid

    @price_paid.setter
    def price_paid(self, price_paid):
        """Sets the price_paid of this OrderItem.


        :param price_paid: The price_paid of this OrderItem.  # noqa: E501
        :type: float
        """

        self._price_paid = price_paid

    @property
    def product(self):
        """Gets the product of this OrderItem.  # noqa: E501


        :return: The product of this OrderItem.  # noqa: E501
        :rtype: SimpleProductDTO
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this OrderItem.


        :param product: The product of this OrderItem.  # noqa: E501
        :type: SimpleProductDTO
        """

        self._product = product

    @property
    def quantity(self):
        """Gets the quantity of this OrderItem.  # noqa: E501


        :return: The quantity of this OrderItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderItem.


        :param quantity: The quantity of this OrderItem.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def sku(self):
        """Gets the sku of this OrderItem.  # noqa: E501


        :return: The sku of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this OrderItem.


        :param sku: The sku of this OrderItem.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def tour_date(self):
        """Gets the tour_date of this OrderItem.  # noqa: E501


        :return: The tour_date of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._tour_date

    @tour_date.setter
    def tour_date(self, tour_date):
        """Sets the tour_date of this OrderItem.


        :param tour_date: The tour_date of this OrderItem.  # noqa: E501
        :type: str
        """

        self._tour_date = tour_date

    @property
    def updated(self):
        """Gets the updated of this OrderItem.  # noqa: E501


        :return: The updated of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this OrderItem.


        :param updated: The updated of this OrderItem.  # noqa: E501
        :type: str
        """

        self._updated = updated

    @property
    def updated_by(self):
        """Gets the updated_by of this OrderItem.  # noqa: E501


        :return: The updated_by of this OrderItem.  # noqa: E501
        :rtype: UserDTO
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this OrderItem.


        :param updated_by: The updated_by of this OrderItem.  # noqa: E501
        :type: UserDTO
        """

        self._updated_by = updated_by

    @property
    def validation_id(self):
        """Gets the validation_id of this OrderItem.  # noqa: E501


        :return: The validation_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._validation_id

    @validation_id.setter
    def validation_id(self, validation_id):
        """Sets the validation_id of this OrderItem.


        :param validation_id: The validation_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._validation_id = validation_id

    @property
    def vendor_voucher_id(self):
        """Gets the vendor_voucher_id of this OrderItem.  # noqa: E501


        :return: The vendor_voucher_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._vendor_voucher_id

    @vendor_voucher_id.setter
    def vendor_voucher_id(self, vendor_voucher_id):
        """Sets the vendor_voucher_id of this OrderItem.


        :param vendor_voucher_id: The vendor_voucher_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._vendor_voucher_id = vendor_voucher_id

    @property
    def voucher_id(self):
        """Gets the voucher_id of this OrderItem.  # noqa: E501


        :return: The voucher_id of this OrderItem.  # noqa: E501
        :rtype: str
        """
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, voucher_id):
        """Sets the voucher_id of this OrderItem.


        :param voucher_id: The voucher_id of this OrderItem.  # noqa: E501
        :type: str
        """

        self._voucher_id = voucher_id

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
        if not isinstance(other, OrderItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other