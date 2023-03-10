"""
    Pterodactyl v1 API Reference

    Welcome to the Pterodactyl v1 API documentation. This documentation is unofficial and provided by Dashflo.  If you find any errors throughout this API reference, please [let us know](https://dashflo.net/tickets/new). A special thanks to everyone who has helped contribute!  **The legacy Pterodactyl v0.7 API documentation [can be found here](https://dashflo.net/docs/api/pterodactyl/v0.7/).** Please remember you should not be using v0.7, and should upgrade as soon as possible.  Pterodactyl Links: **[Website](https://pterodactyl.io/)** | **[GitHub](https://github.com/pterodactyl)** | **[Discord](https://discord.gg/pterodactyl)**  <!-- # API Wrappers/SDKs These wrappers can help save time while working with the API in your programming language of choice.  - [Ptero4J](https://github.com/stanjg/Ptero4J) (Java) - [Pterodactyl4J](https://github.com/mattmalec/Pterodactyl4J) (Java) - [crocgodyl](https://github.com/parkervcp/crocgodyl) (Golang) - [Nodeactyl](https://github.com/Burchard36/Nodeactyl) (Node.js) - [pterodactyl-sdk](https://github.com/hcgcloud/pterodactyl-sdk) (PHP) - [Sharpdactyl](https://github.com/KadePcGames/Sharpdactyl) (C#) - [Pydactyl](https://github.com/iamkubi/pydactyl) (Python) - [aiodactyl](https://github.com/WardPearce/aiodactyl) (Python)  If you are a developer of a Pterodactyl API wrapper that's not listed here, feel free to [contact us](https://dashflo.net/tickets/new) and we can add your API wrapper/SDK to the list. -->  # Authentication A user can generate an client API key from: https://pterodactyl.app/account/api An admin can generate an application API key from: https://pterodactyl.app/admin/api  API keys are entered as bearer tokens with all API requests. Here is an example CURL request:  ``` curl \"<endpoint>\"   -H \"Authorization: Bearer <API-Key>\"   -H \"Content-Type: application/json\" \\   -H \"Accept: Application/vnd.pterodactyl.v1+json\" \\ ```  # Ratelimits 240 requests can be made each minute. Headers are returned to show thelimit, and how many are used within minute. ``` x-ratelimit-limit: 240 x-ratelimit-remaining: 237 ```  # Docs Guide Some API routes require data input, or have additional information that can be provided. The route will include table(s) with the available parameters.   | Name                 | Description       | |----------------------|-------------------| | Include parameters   | List of parameters that can be used after adding `?include=<parameters>,<more-parameters>` to the route | | Available parameters | List of all the different parameters available such as `?example=something&example2=something` | | Filters | Filter the data to only include certain information `?filter[uuid]=something` | | Sort by | Sort the returned results `?sort=-id`. Add a `-` before the sort type to reverse the order | | Fields               | Data input fields |  You can combine multiple filters, it'll look for all matching results. For example, you could add &filter[uuid]=3387 and then it'll only return test@example.com.  ** ** [![Dashflo](https://cdn.dashflo.net/promotions/banners/service/minecraft/7u54t2qnuu8qTRv4.png?cache300620192021 =100%x100% \"Dashflo\")](https://dashflo.net/store/dedicated-servers)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pterodactyl_client
from pterodactyl_client.api.account_api import AccountApi  # noqa: E501


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_account_api_keys_get(self):
        """Test case for account_api_keys_get

        [ /api-keys ] List API keys  # noqa: E501
        """
        pass

    def test_account_api_keys_post(self):
        """Test case for account_api_keys_post

        [ /api-keys ] Create API key  # noqa: E501
        """
        pass

    def test_account_api_keysapi_key_id_delete(self):
        """Test case for account_api_keysapi_key_id_delete

        [ /api-keys/{identifier} ] Delete API key  # noqa: E501
        """
        pass

    def test_account_email_put(self):
        """Test case for account_email_put

        [ /email ] Update email  # noqa: E501
        """
        pass

    def test_account_get(self):
        """Test case for account_get

        [ / ] Account details  # noqa: E501
        """
        pass

    def test_account_password_put(self):
        """Test case for account_password_put

        [ /password ] Update password  # noqa: E501
        """
        pass

    def test_account_two_factor_delete(self):
        """Test case for account_two_factor_delete

        [ /two-factor ] Disable 2FA  # noqa: E501
        """
        pass

    def test_account_two_factor_get(self):
        """Test case for account_two_factor_get

        [ /two-factor ] 2FA details  # noqa: E501
        """
        pass

    def test_account_two_factor_post(self):
        """Test case for account_two_factor_post

        [ /two-factor ] Enable 2FA  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
