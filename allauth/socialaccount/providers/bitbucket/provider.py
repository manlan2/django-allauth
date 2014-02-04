from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth.provider import OAuthProvider

from allauth.socialaccount import app_settings


class BitbucketAccount(ProviderAccount):
    def get_profile_url(self):
        return 'http://bitbucket.org/' + self.account.extra_data['username']

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar')

    def to_str(self):
        return self.account.extra_data['username']


class BitbucketProvider(OAuthProvider):
    id = 'bitbucket'
    name = 'Bitbucket'
    package = 'allauth.socialaccount.providers.bitbucket'
    account_class = BitbucketAccount

    def extract_uid(self, data):
        return data['username']

    def extract_common_fields(self, data):
        return dict(email=data.get('email'),
                    first_name=data.get('first_name'),
                    username=data.get('username'),
                    last_name=data.get('last_name'))

providers.registry.register(BitbucketProvider)
