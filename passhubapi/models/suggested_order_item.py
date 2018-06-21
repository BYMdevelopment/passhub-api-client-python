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

from passhubapi.models.order_item import OrderItem  # noqa: F401,E501


class SuggestedOrderItem(object):
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
        'order_item': 'OrderItem'
    }

    attribute_map = {
        'order_item': 'orderItem'
    }

    def __init__(self, order_item=None):  # noqa: E501
        """SuggestedOrderItem - a model defined in Swagger"""  # noqa: E501

        self._order_item = None
        self.discriminator = None

        if order_item is not None:
            self.order_item = order_item

    @property
    def order_item(self):
        """Gets the order_item of this SuggestedOrderItem.  # noqa: E501


        :return: The order_item of this SuggestedOrderItem.  # noqa: E501
        :rtype: OrderItem
        """
        return self._order_item

    @order_item.setter
    def order_item(self, order_item):
        """Sets the order_item of this SuggestedOrderItem.


        :param order_item: The order_item of this SuggestedOrderItem.  # noqa: E501
        :type: OrderItem
        """

        self._order_item = order_item

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
        if not isinstance(other, SuggestedOrderItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
