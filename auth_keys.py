import json

class AuthKeys:
    def __init__(self):
        with open('config/twi_api_key.json') as config_file:
            self.twi_keys = json.load(config_file)
        self.access_token = self.twi_keys['access_token']
        self.access_token_secret = self.twi_keys['access_token_secret']
        self.consumer_key = self.twi_keys['consumer_key']
        self.consumer_secret = self.twi_keys['consumer_secret']

    def getConsumerKeys(self):
        return self.consumer_key, self.consumer_secret

    def getAccessTokens(self):
        return self.access_token, self.access_token_secret



