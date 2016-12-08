import tweepy
import time
import csv

from auth_keys import AuthKeys

def getTweetsInfo(tweets):
    for tweet in tweets:
        print(tweet.created_at, tweet.text)

def getTweets(api, query='', since='', until=''):
#apiのリクエストリミットが来たら、少し待ってから再び取るようにする
#15分待てばOK
    tweets=[]
    c = tweepy.Cursor(api.search
                    , q=query
                    , since=since
                    , until=until
                    , show_user=True, lang='ja').items()
    while True:
        try:
            tweet = c.next()
            tweets.append([tweet.id_str
                , tweet.user.screen_name
                , tweet.created_at
                , tweet.text
                , tweet.retweet_count
                , tweet.user.description
                , tweet.user.friends_count
                , tweet.user.followers_count
                , tweet.user.favourites_count
                , tweet.user.statuses_count
                ,])
            # Insert into db
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
        except StopIteration:
            break

    return tweets

def getTweetsIdsList(tweets):
    list_ids = []
    for tweet in tweets:
        list_ids.append(tweet.id)
    return list_ids

def getUserTimeline(api, screen_name):
    page = 1
    tweets = []
    for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name).items():
        tweets.append([status.id_str
            , status.user.screen_name
            , status.created_at
            , status.text
            , status.retweet_count
            , status.user.description
            , status.user.friends_count
            , status.user.followers_count
            , status.user.favourites_count
            , status.user.statuses_count
            ,])
        print(status.text)
    return tweets


if __name__ == '__main__':
    auth_keys = AuthKeys()
    consumer_key, consumer_secret = auth_keys.getConsumerKeys()
    access_token, access_token_secret = auth_keys.getAccessTokens()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
#APIのインスタンス生成 APIのメソッドが入る
    api = tweepy.API(auth)
#queryで検索した結果を15個取得する
    query = 'トランプ'
    search_results = api.search(query)
    #getTweetsInfo(search_result)

#無限に取得する
    since = '2016-11-09'
    until = '2016-11-16'
    #tweets = getTweets(api, query=query, since=since, until=until)
    header = ['id_str', 'screen_name', 'created_at', 'text', 'ツイートのリツイート数', 'プロフィール文', 'フォロー数', 'フォロワー数', 'お気に入り登録数', '投稿数']

    """
    with open('tweets_' + query + '.csv', 'w') as f:
        dataWriter = csv.writer(f)
        dataWriter.writerow(header)
        dataWriter.writerows(tweets)
    """


    screen_name = 'Bio_Gorilla_bot'
    tweets = getUserTimeline(api, screen_name)

    with open('tweets_' + screen_name + '.csv', 'w') as f:
        dataWriter = csv.writer(f)
        dataWriter.writerow(header)
        dataWriter.writerows(tweets)
#取得したツイートのidを取っておく
    #tweets_ids = getTweetsIdsList(search_results)

#100個まで、listにあるidでツイートを取得
    #lookup = api.statuses_lookup(tweets_ids)
    #getTweetsInfo(lookup)


"""
    #twitterの投稿テキスト表示 pagesとは、、、pageの概念がわからない
    cur = tweepy.Cursor(api.user_timeline, id='twitter').pages()
    for page in cur:
        getPageTweetText(page)
"""


"""
    user = api.get_user('twitter')
    #userのフォローしている人のスクリーンネームを20件表示
    for friend in user.friends():
        print(friend.screen_name)
"""

"""
"""
