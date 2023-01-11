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


class ApiClientClientApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.__permissions_showpermissions_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/client/permissions',
                'operation_id': '__permissions_showpermissions',
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
        self.get__listservers_endpoint = _Endpoint(
            settings={
                'response_type': (bool, date, datetime, dict, float, int, list, str, none_type,),
                'auth': [
                    'bearer'
                ],
                'endpoint_path': '/client',
                'operation_id': 'get__listservers',
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
                ],
                'required': [
                    'accept',
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
                },
                'attribute_map': {
                    'accept': 'Accept',
                },
                'location_map': {
                    'accept': 'header',
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

    def __permissions_showpermissions(
        self,
        accept,
        content_type,
        **kwargs
    ):
        """[ /permissions ] Show permissions  # noqa: E501

        Retries all available permissions  This is used for the frontend  <!-- RESPONSE 200 --> {   \"object\": \"system_permissions\",   \"attributes\": {     \"permissions\": {       \"websocket\": {         \"description\": \"Allows the user to connect to the server websocket, giving them access to view console output and realtime server stats.\",         \"keys\": {           \"connect\": \"Allows a user to connect to the websocket instance for a server to stream the console.\"         }       },       \"control\": {         \"description\": \"Permissions that control a user's ability to control the power state of a server, or send commands.\",         \"keys\": {           \"console\": \"Allows a user to send commands to the server instance via the console.\",           \"start\": \"Allows a user to start the server if it is stopped.\",           \"stop\": \"Allows a user to stop a server if it is running.\",           \"restart\": \"Allows a user to perform a server restart. This allows them to start the server if it is offline, but not put the server in a completely stopped state.\"         }       },       \"user\": {         \"description\": \"Permissions that allow a user to manage other subusers on a server. They will never be able to edit their own account, or assign permissions they do not have themselves.\",         \"keys\": {           \"create\": \"Allows a user to create new subusers for the server.\",           \"read\": \"Allows the user to view subusers and their permissions for the server.\",           \"update\": \"Allows a user to modify other subusers.\",           \"delete\": \"Allows a user to delete a subuser from the server.\"         }       },       \"file\": {         \"description\": \"Permissions that control a user's ability to modify the filesystem for this server.\",         \"keys\": {           \"create\": \"Allows a user to create additional files and folders via the Panel or direct upload.\",           \"read\": \"Allows a user to view the contents of a directory and read the contents of a file. Users with this permission can also download files.\",           \"update\": \"Allows a user to update the contents of an existing file or directory.\",           \"delete\": \"Allows a user to delete files or directories.\",           \"archive\": \"Allows a user to archive the contents of a directory as well as decompress existing archives on the system.\",           \"sftp\": \"Allows a user to connect to SFTP and manage server files using the other assigned file permissions.\"         }       },       \"backup\": {         \"description\": \"Permissions that control a user's ability to generate and manage server backups.\",         \"keys\": {           \"create\": \"Allows a user to create new backups for this server.\",           \"read\": \"Allows a user to view all backups that exist for this server.\",           \"update\": \"\",           \"delete\": \"Allows a user to remove backups from the system.\",           \"download\": \"Allows a user to download backups.\"         }       },       \"allocation\": {         \"description\": \"Permissions that control a user's ability to modify the port allocations for this server.\",         \"keys\": {           \"read\": \"Allows a user to view the allocations assigned to this server.\",           \"create\": \"Allows a user to assign additional allocations to the server.\",           \"update\": \"Allows a user to change the primary server allocation and attach notes to each allocation.\",           \"delete\": \"Allows a user to delete an allocation from the server.\"         }       },       \"startup\": {         \"description\": \"Permissions that control a user's ability to view this server's startup parameters.\",         \"keys\": {           \"read\": \"\",           \"update\": \"\"         }       },       \"database\": {         \"description\": \"Permissions that control a user's access to the database management for this server.\",         \"keys\": {           \"create\": \"Allows a user to create a new database for this server.\",           \"read\": \"Allows a user to view the database associated with this server.\",           \"update\": \"Allows a user to rotate the password on a database instance. If the user does not have the view_password permission they will not see the updated password.\",           \"delete\": \"Allows a user to remove a database instance from this server.\",           \"view_password\": \"Allows a user to view the password associated with a database instance for this server.\"         }       },       \"schedule\": {         \"description\": \"Permissions that control a user's access to the schedule management for this server.\",         \"keys\": {           \"create\": \"\",           \"read\": \"\",           \"update\": \"\",           \"delete\": \"\"         }       },       \"settings\": {         \"description\": \"Permissions that control a user's access to the settings for this server.\",         \"keys\": {           \"rename\": \"\",           \"reinstall\": \"\"         }       }     }   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.__permissions_showpermissions(accept, content_type, async_req=True)
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
        return self.__permissions_showpermissions_endpoint.call_with_http_info(**kwargs)

    def get__listservers(
        self,
        accept,
        **kwargs
    ):
        """[ / ] List servers  # noqa: E501

        Lists all servers  ## Include parameters | Parameter | Description                               | |-----------|-------------------------------------------| | egg       | Information about the egg the server uses | | subusers  | List of subusers on the server            |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server\",       \"attributes\": {         \"server_owner\": true,         \"identifier\": \"{server_id}\",         \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"name\": \"Gaming\",         \"node\": \"Test\",         \"sftp_details\": {           \"ip\": \"pterodactyl.file.properties\",           \"port\": 2022         },         \"description\": \"Matt from Wii Sports\",         \"limits\": {           \"memory\": 512,           \"swap\": 0,           \"disk\": 200,           \"io\": 500,           \"cpu\": 0         },         \"feature_limits\": {           \"databases\": 5,           \"allocations\": 5,           \"backups\": 2         },         \"is_suspended\": false,         \"is_installing\": false,         \"relationships\": {           \"allocations\": {             \"object\": \"list\",             \"data\": [               {                 \"object\": \"allocation\",                 \"attributes\": {                   \"id\": 1,                   \"ip\": \"45.86.168.218\",                   \"ip_alias\": null,                   \"port\": 25565,                   \"notes\": null,                   \"is_default\": true                 }               },               {                 \"object\": \"allocation\",                 \"attributes\": {                   \"id\": 2,                   \"ip\": \"45.86.168.218\",                   \"ip_alias\": null,                   \"port\": 25566,                   \"notes\": \"Votifier\",                   \"is_default\": false                 }               }             ]           }         }       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 1,       \"count\": 1,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get__listservers(accept, async_req=True)
        >>> result = thread.get()

        Args:
            accept (str): 

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
        return self.get__listservers_endpoint.call_with_http_info(**kwargs)

