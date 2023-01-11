"""
    Pterodactyl v1 API Reference

    Welcome to the Pterodactyl v1 API documentation. This documentation is unofficial and provided by Dashflo.  If you find any errors throughout this API reference, please [let us know](https://dashflo.net/tickets/new). A special thanks to everyone who has helped contribute!  **The legacy Pterodactyl v0.7 API documentation [can be found here](https://dashflo.net/docs/api/pterodactyl/v0.7/).** Please remember you should not be using v0.7, and should upgrade as soon as possible.  Pterodactyl Links: **[Website](https://pterodactyl.io/)** | **[GitHub](https://github.com/pterodactyl)** | **[Discord](https://discord.gg/pterodactyl)**  <!-- # API Wrappers/SDKs These wrappers can help save time while working with the API in your programming language of choice.  - [Ptero4J](https://github.com/stanjg/Ptero4J) (Java) - [Pterodactyl4J](https://github.com/mattmalec/Pterodactyl4J) (Java) - [crocgodyl](https://github.com/parkervcp/crocgodyl) (Golang) - [Nodeactyl](https://github.com/Burchard36/Nodeactyl) (Node.js) - [pterodactyl-sdk](https://github.com/hcgcloud/pterodactyl-sdk) (PHP) - [Sharpdactyl](https://github.com/KadePcGames/Sharpdactyl) (C#) - [Pydactyl](https://github.com/iamkubi/pydactyl) (Python) - [aiodactyl](https://github.com/WardPearce/aiodactyl) (Python)  If you are a developer of a Pterodactyl API wrapper that's not listed here, feel free to [contact us](https://dashflo.net/tickets/new) and we can add your API wrapper/SDK to the list. -->  # Authentication A user can generate an client API key from: https://pterodactyl.app/account/api An admin can generate an application API key from: https://pterodactyl.app/admin/api  API keys are entered as bearer tokens with all API requests. Here is an example CURL request:  ``` curl \"<endpoint>\"   -H \"Authorization: Bearer <API-Key>\"   -H \"Content-Type: application/json\" \\   -H \"Accept: Application/vnd.pterodactyl.v1+json\" \\ ```  # Ratelimits 240 requests can be made each minute. Headers are returned to show thelimit, and how many are used within minute. ``` x-ratelimit-limit: 240 x-ratelimit-remaining: 237 ```  # Docs Guide Some API routes require data input, or have additional information that can be provided. The route will include table(s) with the available parameters.   | Name                 | Description       | |----------------------|-------------------| | Include parameters   | List of parameters that can be used after adding `?include=<parameters>,<more-parameters>` to the route | | Available parameters | List of all the different parameters available such as `?example=something&example2=something` | | Filters | Filter the data to only include certain information `?filter[uuid]=something` | | Sort by | Sort the returned results `?sort=-id`. Add a `-` before the sort type to reverse the order | | Fields               | Data input fields |  You can combine multiple filters, it'll look for all matching results. For example, you could add &filter[uuid]=3387 and then it'll only return test@example.com.  ** ** [![Dashflo](https://cdn.dashflo.net/promotions/banners/service/minecraft/7u54t2qnuu8qTRv4.png?cache300620192021 =100%x100% \"Dashflo\")](https://dashflo.net/store/dedicated-servers)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pterodactyl_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from pterodactyl_client.exceptions import ApiAttributeError



class DecompressDecompressfileRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'file': (str,),  # noqa: E501
            'root': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'file': 'file',  # noqa: E501
        'root': 'root',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, file, root, *args, **kwargs):  # noqa: E501
        """DecompressDecompressfileRequest - a model defined in OpenAPI

        Args:
            file (str):
            root (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.file = file
        self.root = root
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, file, root, *args, **kwargs):  # noqa: E501
        """DecompressDecompressfileRequest - a model defined in OpenAPI

        Args:
            file (str):
            root (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.file = file
        self.root = root
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
