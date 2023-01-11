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
from pterodactyl_client.model.client_servers_server_id_databases_post_request import ClientServersServerIdDatabasesPostRequest


class DatabasesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.client_serversserver_id_databases_get_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/client/servers/{server_id}/databases',
                'operation_id': 'client_serversserver_id_databases_get',
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
                    'server_id',
                ],
                'required': [
                    'accept',
                    'content_type',
                    'server_id',
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
                    'server_id':
                        (str,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'content_type': 'Content-Type',
                    'server_id': 'server_id',
                },
                'location_map': {
                    'accept': 'header',
                    'content_type': 'header',
                    'server_id': 'path',
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
        self.client_serversserver_id_databases_post_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/client/servers/{server_id}/databases',
                'operation_id': 'client_serversserver_id_databases_post',
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
                    'server_id',
                    'client_servers_server_id_databases_post_request',
                ],
                'required': [
                    'accept',
                    'server_id',
                    'client_servers_server_id_databases_post_request',
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
                    'server_id':
                        (str,),
                    'client_servers_server_id_databases_post_request':
                        (ClientServersServerIdDatabasesPostRequest,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'server_id': 'server_id',
                },
                'location_map': {
                    'accept': 'header',
                    'server_id': 'path',
                    'client_servers_server_id_databases_post_request': 'body',
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
        self.client_serversserver_id_databasesdatabase_id_delete_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/client/servers/{server_id}/databases/{database_id}',
                'operation_id': 'client_serversserver_id_databasesdatabase_id_delete',
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
                    'server_id',
                    'database_id',
                ],
                'required': [
                    'accept',
                    'content_type',
                    'server_id',
                    'database_id',
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
                    'server_id':
                        (str,),
                    'database_id':
                        (int,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'content_type': 'Content-Type',
                    'server_id': 'server_id',
                    'database_id': 'database_id',
                },
                'location_map': {
                    'accept': 'header',
                    'content_type': 'header',
                    'server_id': 'path',
                    'database_id': 'path',
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
        self.client_serversserver_id_databasesdatabase_id_rotate_password_post_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/client/servers/{server_id}/databases/{database_id}/rotate-password',
                'operation_id': 'client_serversserver_id_databasesdatabase_id_rotate_password_post',
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
                    'server_id',
                    'database_id',
                ],
                'required': [
                    'accept',
                    'server_id',
                    'database_id',
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
                    'server_id':
                        (str,),
                    'database_id':
                        (int,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'server_id': 'server_id',
                    'database_id': 'database_id',
                },
                'location_map': {
                    'accept': 'header',
                    'server_id': 'path',
                    'database_id': 'path',
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

    def client_serversserver_id_databases_get(
        self,
        accept,
        content_type,
        server_id,
        **kwargs
    ):
        """[ / ] List databases  # noqa: E501

        Lists all databases on a server  ## Include parameters | Parameter | Description                         | |-----------|-------------------------------------| | password  | Includes the database user password |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": \"bEY4yAD5\",         \"host\": {           \"address\": \"127.0.0.1\",           \"port\": 3306         },         \"name\": \"s5_perms\",         \"username\": \"u5_QsIAp1jhvS\",         \"connections_from\": \"%\",         \"max_connections\": 0       }     },     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": \"E0A0Rw42\",         \"host\": {           \"address\": \"127.0.0.1\",           \"port\": 3306         },         \"name\": \"s5_coreprotect\",         \"username\": \"u5_2jtJx1nO1d\",         \"connections_from\": \"%\",         \"max_connections\": 0       }     }   ] } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.client_serversserver_id_databases_get(accept, content_type, server_id, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            content_type (str): 
            server_id (str): 

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
        kwargs['server_id'] = \
            server_id
        return self.client_serversserver_id_databases_get_endpoint.call_with_http_info(**kwargs)

    def client_serversserver_id_databases_post(
        self,
        accept,
        server_id,
        client_servers_server_id_databases_post_request,
        **kwargs
    ):
        """[ / ] Create database  # noqa: E501

        Creates a new database  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": \"y9YVxO4V\",     \"host\": {       \"address\": \"127.0.0.1\",       \"port\": 3306     },     \"name\": \"s5_punishments\",     \"username\": \"u5_aeZqbGdCM9\",     \"connections_from\": \"%\",     \"max_connections\": 0,     \"relationships\": {       \"password\": {         \"object\": \"database_password\",         \"attributes\": {           \"password\": \"=lR2orDOcwfKkM=BXb.BVF.C\"         }       }     }   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.client_serversserver_id_databases_post(accept, server_id, client_servers_server_id_databases_post_request, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            server_id (str): 
            client_servers_server_id_databases_post_request (ClientServersServerIdDatabasesPostRequest): 

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
        kwargs['server_id'] = \
            server_id
        kwargs['client_servers_server_id_databases_post_request'] = \
            client_servers_server_id_databases_post_request
        return self.client_serversserver_id_databases_post_endpoint.call_with_http_info(**kwargs)

    def client_serversserver_id_databasesdatabase_id_delete(
        self,
        accept,
        content_type,
        server_id,
        database_id,
        **kwargs
    ):
        """[ /{database} ] Delete database  # noqa: E501

        Deletes the specified database  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.client_serversserver_id_databasesdatabase_id_delete(accept, content_type, server_id, database_id, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            content_type (str): 
            server_id (str): 
            database_id (int): 

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
        kwargs['server_id'] = \
            server_id
        kwargs['database_id'] = \
            database_id
        return self.client_serversserver_id_databasesdatabase_id_delete_endpoint.call_with_http_info(**kwargs)

    def client_serversserver_id_databasesdatabase_id_rotate_password_post(
        self,
        accept,
        server_id,
        database_id,
        **kwargs
    ):
        """[ /{database}/rotate-password ] Rotate password  # noqa: E501

        Changes the password of a specified database  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": \"y9YVxO4V\",     \"host\": {       \"address\": \"127.0.0.1\",       \"port\": 3306     },     \"name\": \"s5_punishments\",     \"username\": \"u5_aeZqbGdCM9\",     \"connections_from\": \"%\",     \"max_connections\": 0,     \"relationships\": {       \"password\": {         \"object\": \"database_password\",         \"attributes\": {           \"password\": \"vnFKXlJ.p77!EiGR+Kd3muB.\"         }       }     }   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.client_serversserver_id_databasesdatabase_id_rotate_password_post(accept, server_id, database_id, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 
            server_id (str): 
            database_id (int): 

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
        kwargs['server_id'] = \
            server_id
        kwargs['database_id'] = \
            database_id
        return self.client_serversserver_id_databasesdatabase_id_rotate_password_post_endpoint.call_with_http_info(**kwargs)

