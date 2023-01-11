"""
    Pterodactyl v1 API Reference

    Welcome to the Pterodactyl v1 API documentation. This documentation is unofficial and provided by Dashflo.  If you find any errors throughout this API reference, please [let us know](https://dashflo.net/tickets/new). A special thanks to everyone who has helped contribute!  **The legacy Pterodactyl v0.7 API documentation [can be found here](https://dashflo.net/docs/api/pterodactyl/v0.7/).** Please remember you should not be using v0.7, and should upgrade as soon as possible.  Pterodactyl Links: **[Website](https://pterodactyl.io/)** | **[GitHub](https://github.com/pterodactyl)** | **[Discord](https://discord.gg/pterodactyl)**  <!-- # API Wrappers/SDKs These wrappers can help save time while working with the API in your programming language of choice.  - [Ptero4J](https://github.com/stanjg/Ptero4J) (Java) - [Pterodactyl4J](https://github.com/mattmalec/Pterodactyl4J) (Java) - [crocgodyl](https://github.com/parkervcp/crocgodyl) (Golang) - [Nodeactyl](https://github.com/Burchard36/Nodeactyl) (Node.js) - [pterodactyl-sdk](https://github.com/hcgcloud/pterodactyl-sdk) (PHP) - [Sharpdactyl](https://github.com/KadePcGames/Sharpdactyl) (C#) - [Pydactyl](https://github.com/iamkubi/pydactyl) (Python) - [aiodactyl](https://github.com/WardPearce/aiodactyl) (Python)  If you are a developer of a Pterodactyl API wrapper that's not listed here, feel free to [contact us](https://dashflo.net/tickets/new) and we can add your API wrapper/SDK to the list. -->  # Authentication A user can generate an client API key from: https://pterodactyl.app/account/api An admin can generate an application API key from: https://pterodactyl.app/admin/api  API keys are entered as bearer tokens with all API requests. Here is an example CURL request:  ``` curl \"<endpoint>\"   -H \"Authorization: Bearer <API-Key>\"   -H \"Content-Type: application/json\" \\   -H \"Accept: Application/vnd.pterodactyl.v1+json\" \\ ```  # Ratelimits 240 requests can be made each minute. Headers are returned to show thelimit, and how many are used within minute. ``` x-ratelimit-limit: 240 x-ratelimit-remaining: 237 ```  # Docs Guide Some API routes require data input, or have additional information that can be provided. The route will include table(s) with the available parameters.   | Name                 | Description       | |----------------------|-------------------| | Include parameters   | List of parameters that can be used after adding `?include=<parameters>,<more-parameters>` to the route | | Available parameters | List of all the different parameters available such as `?example=something&example2=something` | | Filters | Filter the data to only include certain information `?filter[uuid]=something` | | Sort by | Sort the returned results `?sort=-id`. Add a `-` before the sort type to reverse the order | | Fields               | Data input fields |  You can combine multiple filters, it'll look for all matching results. For example, you could add &filter[uuid]=3387 and then it'll only return test@example.com.  ** ** [![Dashflo](https://cdn.dashflo.net/promotions/banners/service/minecraft/7u54t2qnuu8qTRv4.png?cache300620192021 =100%x100% \"Dashflo\")](https://dashflo.net/store/dedicated-servers)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pterodactyl_client.api_client import ApiClient, Endpoint as _Endpoint
from pterodactyl_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pterodactyl_client.model.application_locations_location_id_patch_request import ApplicationLocationsLocationIdPatchRequest
from pterodactyl_client.model.int import Int


class LocationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.application_locationslocation_id_delete_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/application/locations/{location_id}',
                'operation_id': 'application_locationslocation_id_delete',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://pterodactyl.file.properties/api",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'accept',
                    'content_type',
                    'location_id',
                ],
                'required': [
                    'accept',
                    'content_type',
                    'location_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'accept':
                        (str,),
                    'content_type':
                        (str,),
                    'location_id':
                        (Int,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'content_type': 'Content-Type',
                    'location_id': 'location_id',
                },
                'location_map': {
                    'accept': 'header',
                    'content_type': 'header',
                    'location_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.application_locationslocation_id_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/application/locations/{location_id}',
                'operation_id': 'application_locationslocation_id_get',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://pterodactyl.file.properties/api",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'accept',
                    'content_type',
                    'location_id',
                ],
                'required': [
                    'accept',
                    'content_type',
                    'location_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'accept':
                        (str,),
                    'content_type':
                        (str,),
                    'location_id':
                        (Int,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'content_type': 'Content-Type',
                    'location_id': 'location_id',
                },
                'location_map': {
                    'accept': 'header',
                    'content_type': 'header',
                    'location_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.application_locationslocation_id_patch_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/application/locations/{location_id}',
                'operation_id': 'application_locationslocation_id_patch',
                'http_method': 'PATCH',
                'servers': [
                    {
                        'url': "https://pterodactyl.file.properties/api",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'accept',
                    'location_id',
                    'application_locations_location_id_patch_request',
                ],
                'required': [
                    'accept',
                    'location_id',
                    'application_locations_location_id_patch_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'accept':
                        (str,),
                    'location_id':
                        (Int,),
                    'application_locations_location_id_patch_request':
                        (ApplicationLocationsLocationIdPatchRequest,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'location_id': 'location_id',
                },
                'location_map': {
                    'accept': 'header',
                    'location_id': 'path',
                    'application_locations_location_id_patch_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def application_locationslocation_id_delete(
        self,
        accept,
        content_type,
        location_id,
        **kwargs
    ):
        """[ /{location} ] Delete location  # noqa: E501

        Deletes the specified location  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.application_locationslocation_id_delete(accept, content_type, location_id, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            content_type (str): 
            location_id (Int): 

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['accept'] = \
            accept
        kwargs['content_type'] = \
            content_type
        kwargs['location_id'] = \
            location_id
        return self.application_locationslocation_id_delete_endpoint.call_with_http_info(**kwargs)

    def application_locationslocation_id_get(
        self,
        accept,
        content_type,
        location_id,
        **kwargs
    ):
        """[ /{location} ] Location details  # noqa: E501

        Retrieves the specified location  # Available include parameters | Parameter | Description                            | |-----------|----------------------------------------| | nodes     | List of nodes assigned to the location | | servers   | List of servers in the location        |  <!-- RESPONSE 200 --> {   \"object\": \"location\",   \"attributes\": {     \"id\": 1,     \"short\": \"Test\",     \"long\": \"Test\",     \"updated_at\": \"2019-12-22T04:44:18+00:00\",     \"created_at\": \"2019-12-22T04:44:18+00:00\"   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.application_locationslocation_id_get(accept, content_type, location_id, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            content_type (str): 
            location_id (Int): 

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['accept'] = \
            accept
        kwargs['content_type'] = \
            content_type
        kwargs['location_id'] = \
            location_id
        return self.application_locationslocation_id_get_endpoint.call_with_http_info(**kwargs)

    def application_locationslocation_id_patch(
        self,
        accept,
        location_id,
        application_locations_location_id_patch_request,
        **kwargs
    ):
        """[ / ] Update location  # noqa: E501

        Updates the specified location  <!-- RESPONSE 200 --> {   \"object\": \"location\",   \"attributes\": {     \"id\": 1,     \"short\": \"GB\",     \"long\": \"London Datacenter\",     \"updated_at\": \"2020-06-13T21:16:58+00:00\",     \"created_at\": \"2019-12-22T04:44:18+00:00\"   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.application_locationslocation_id_patch(accept, location_id, application_locations_location_id_patch_request, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            location_id (Int): 
            application_locations_location_id_patch_request (ApplicationLocationsLocationIdPatchRequest): 

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            bool, date, datetime, dict, float, int, list, str, none_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['accept'] = \
            accept
        kwargs['location_id'] = \
            location_id
        kwargs['application_locations_location_id_patch_request'] = \
            application_locations_location_id_patch_request
        return self.application_locationslocation_id_patch_endpoint.call_with_http_info(**kwargs)
