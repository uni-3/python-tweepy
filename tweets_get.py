import tweepy
from pprint import pprint

from auth_keys import AuthKeys

def getTweetsInfo(tweets):
    for tweet in tweets:
        print(tweet.created_at, tweet.text)

if __name__ == '__main__':
    auth_keys = AuthKeys()
    consumer_key, consumer_secret = auth_keys.getConsumerKeys()
    access_token, access_token_secret = auth_keys.getAccessTokens()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
#APIのインスタンス生成 APIのメソッドが入る
    api = tweepy.API(auth)
#queryで検索した結果を15個取得する
    query = 'curry'
    search_result = api.search(query)
    getTweetsInfo(search_result)
