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
from pterodactyl_client.model.createnode_request import CreatenodeRequest


class NodesNodesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.__createnode_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/application/nodes',
                'operation_id': '__createnode',
                'http_method': 'POST',
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
                    'createnode_request',
                ],
                'required': [
                    'accept',
                    'createnode_request',
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
                    'createnode_request':
                        (CreatenodeRequest,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                },
                'location_map': {
                    'accept': 'header',
                    'createnode_request': 'body',
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
        self.__listnodes_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/application/nodes',
                'operation_id': '__listnodes',
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
                ],
                'required': [
                    'accept',
                    'content_type',
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
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'accept': 'header',
                    'content_type': 'header',
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

    def __createnode(
        self,
        accept,
        createnode_request,
        **kwargs
    ):
        """[ / ] Create node  # noqa: E501

        Creates a new node  <!-- RESPONSE 201 --> {   \"object\": \"node\",   \"attributes\": {     \"id\": 4,     \"uuid\": \"4158cfe9-2aa8-4812-bf6e-d88beeb08e98\",     \"public\": true,     \"name\": \"New Node\",     \"description\": null,     \"location_id\": 1,     \"fqdn\": \"node2.example.com\",     \"scheme\": \"https\",     \"behind_proxy\": false,     \"maintenance_mode\": false,     \"memory\": 10240,     \"memory_overallocate\": 0,     \"disk\": 50000,     \"disk_overallocate\": 0,     \"upload_size\": 100,     \"daemon_listen\": 8080,     \"daemon_sftp\": 2022,     \"daemon_base\": \"/var/lib/pterodactyl/volumes\",     \"created_at\": \"2020-10-29T01:17:38+00:00\",     \"updated_at\": \"2020-10-29T01:17:38+00:00\",     \"allocated_resources\": {       \"memory\": 0,       \"disk\": 0     }   },   \"meta\": {     \"resource\": \"https://pterodactyl.file.properties/api/application/nodes/4\"   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.__createnode(accept, createnode_request, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            createnode_request (CreatenodeRequest): 

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
        kwargs['createnode_request'] = \
            createnode_request
        return self.__createnode_endpoint.call_with_http_info(**kwargs)

    def __listnodes(
        self,
        accept,
        content_type,
        **kwargs
    ):
        """[ / ] List nodes  # noqa: E501

        Retrieves a list of nodes  ## Available include parameters | Parameter   | Description                                            | |-------------|--------------------------------------------------------| | allocations | List of allocations added to the node                  | | location    | Information about the location the node is assigned to | | servers     | List of servers on the node                            |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"node\",       \"attributes\": {         \"id\": 1,         \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",         \"public\": true,         \"name\": \"Test\",         \"description\": \"Test\",         \"location_id\": 1,         \"fqdn\": \"pterodactyl.file.properties\",         \"scheme\": \"https\",         \"behind_proxy\": false,         \"maintenance_mode\": false,         \"memory\": 2048,         \"memory_overallocate\": 0,         \"disk\": 5000,         \"disk_overallocate\": 0,         \"upload_size\": 100,         \"daemon_listen\": 8080,         \"daemon_sftp\": 2022,         \"daemon_base\": \"/srv/daemon-data\",         \"created_at\": \"2019-12-22T04:44:51+00:00\",         \"updated_at\": \"2019-12-22T04:44:51+00:00\"       }     },     {       \"object\": \"node\",       \"attributes\": {         \"id\": 3,         \"uuid\": \"71b15cf6-909a-4b60-aa04-abb4c8f98f61\",         \"public\": true,         \"name\": \"2\",         \"description\": \"e\",         \"location_id\": 1,         \"fqdn\": \"pterodactyl.file.properties\",         \"scheme\": \"https\",         \"behind_proxy\": false,         \"maintenance_mode\": false,         \"memory\": 100,         \"memory_overallocate\": 0,         \"disk\": 100,         \"disk_overallocate\": 0,         \"upload_size\": 100,         \"daemon_listen\": 8080,         \"daemon_sftp\": 2022,         \"daemon_base\": \"/var/lib/pterodactyl/volumes\",         \"created_at\": \"2020-06-23T04:50:37+00:00\",         \"updated_at\": \"2020-06-23T04:50:37+00:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 2,       \"count\": 2,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.__listnodes(accept, content_type, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            content_type (str): 

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
        return self.__listnodes_endpoint.call_with_http_info(**kwargs)

