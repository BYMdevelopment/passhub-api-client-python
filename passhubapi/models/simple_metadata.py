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


class SimpleMetadata(object):
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
        'extra': 'dict(str, str)',
        'pass_currency_amount': 'float'
    }

    attribute_map = {
        'extra': 'extra',
        'pass_currency_amount': 'passCurrencyAmount'
    }

    def __init__(self, extra=None, pass_currency_amount=None):  # noqa: E501
        """SimpleMetadata - a model defined in Swagger"""  # noqa: E501

        self._extra = None
        self._pass_currency_amount = None
        self.discriminator = None

        if extra is not None:
            self.extra = extra
        if pass_currency_amount is not None:
            self.pass_currency_amount = pass_currency_amount

    @property
    def extra(self):
        """Gets the extra of this SimpleMetadata.  # noqa: E501


        :return: The extra of this SimpleMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this SimpleMetadata.


        :param extra: The extra of this SimpleMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra = extra

    @property
    def pass_currency_amount(self):
        """Gets the pass_currency_amount of this SimpleMetadata.  # noqa: E501


        :return: The pass_currency_amount of this SimpleMetadata.  # noqa: E501
        :rtype: float
        """
        return self._pass_currency_amount

    @pass_currency_amount.setter
    def pass_currency_amount(self, pass_currency_amount):
        """Sets the pass_currency_amount of this SimpleMetadata.


        :param pass_currency_amount: The pass_currency_amount of this SimpleMetadata.  # noqa: E501
        :type: float
        """

        self._pass_currency_amount = pass_currency_amount

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
        if not isinstance(other, SimpleMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
