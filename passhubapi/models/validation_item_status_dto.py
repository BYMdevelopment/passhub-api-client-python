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


class ValidationItemStatusDTO(object):
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
        'balance': 'float',
        'expiry_date': 'str',
        'max_use_count': 'int',
        'max_use_hours': 'int',
        'start_date': 'str',
        'type': 'str',
        'used_count': 'int'
    }

    attribute_map = {
        'balance': 'balance',
        'expiry_date': 'expiryDate',
        'max_use_count': 'maxUseCount',
        'max_use_hours': 'maxUseHours',
        'start_date': 'startDate',
        'type': 'type',
        'used_count': 'usedCount'
    }

    def __init__(self, balance=None, expiry_date=None, max_use_count=None, max_use_hours=None, start_date=None, type=None, used_count=None):  # noqa: E501
        """ValidationItemStatusDTO - a model defined in Swagger"""  # noqa: E501

        self._balance = None
        self._expiry_date = None
        self._max_use_count = None
        self._max_use_hours = None
        self._start_date = None
        self._type = None
        self._used_count = None
        self.discriminator = None

        if balance is not None:
            self.balance = balance
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if max_use_count is not None:
            self.max_use_count = max_use_count
        if max_use_hours is not None:
            self.max_use_hours = max_use_hours
        if start_date is not None:
            self.start_date = start_date
        if type is not None:
            self.type = type
        if used_count is not None:
            self.used_count = used_count

    @property
    def balance(self):
        """Gets the balance of this ValidationItemStatusDTO.  # noqa: E501


        :return: The balance of this ValidationItemStatusDTO.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ValidationItemStatusDTO.


        :param balance: The balance of this ValidationItemStatusDTO.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ValidationItemStatusDTO.  # noqa: E501


        :return: The expiry_date of this ValidationItemStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ValidationItemStatusDTO.


        :param expiry_date: The expiry_date of this ValidationItemStatusDTO.  # noqa: E501
        :type: str
        """

        self._expiry_date = expiry_date

    @property
    def max_use_count(self):
        """Gets the max_use_count of this ValidationItemStatusDTO.  # noqa: E501


        :return: The max_use_count of this ValidationItemStatusDTO.  # noqa: E501
        :rtype: int
        """
        return self._max_use_count

    @max_use_count.setter
    def max_use_count(self, max_use_count):
        """Sets the max_use_count of this ValidationItemStatusDTO.


        :param max_use_count: The max_use_count of this ValidationItemStatusDTO.  # noqa: E501
        :type: int
        """

        self._max_use_count = max_use_count

    @property
    def max_use_hours(self):
        """Gets the max_use_hours of this ValidationItemStatusDTO.  # noqa: E501


        :return: The max_use_hours of this ValidationItemStatusDTO.  # noqa: E501
        :rtype: int
        """
        return self._max_use_hours

    @max_use_hours.setter
    def max_use_hours(self, max_use_hours):
        """Sets the max_use_hours of this ValidationItemStatusDTO.


        :param max_use_hours: The max_use_hours of this ValidationItemStatusDTO.  # noqa: E501
        :type: int
        """

        self._max_use_hours = max_use_hours

    @property
    def start_date(self):
        """Gets the start_date of this ValidationItemStatusDTO.  # noqa: E501


        :return: The start_date of this ValidationItemStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ValidationItemStatusDTO.


        :param start_date: The start_date of this ValidationItemStatusDTO.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def type(self):
        """Gets the type of this ValidationItemStatusDTO.  # noqa: E501


        :return: The type of this ValidationItemStatusDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ValidationItemStatusDTO.


        :param type: The type of this ValidationItemStatusDTO.  # noqa: E501
        :type: str
        """
        allowed_values = ["BASIC_SINGLE", "BASIC_VALID_HOURS", "PASS_LIMITED", "PASS_UNLIMITED", "PASS_CALENDAR", "FLEXPASS", "PASS_CURRENCY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def used_count(self):
        """Gets the used_count of this ValidationItemStatusDTO.  # noqa: E501


        :return: The used_count of this ValidationItemStatusDTO.  # noqa: E501
        :rtype: int
        """
        return self._used_count

    @used_count.setter
    def used_count(self, used_count):
        """Sets the used_count of this ValidationItemStatusDTO.


        :param used_count: The used_count of this ValidationItemStatusDTO.  # noqa: E501
        :type: int
        """

        self._used_count = used_count

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
        if not isinstance(other, ValidationItemStatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
