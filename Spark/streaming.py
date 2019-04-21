import  json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream



# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="XXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is tweets_counta basic listener that just prints received tweets to stdout.
    """

    def on_data(self, data):
        print(data.rstrip())
        return True

    def on_exception(self, exception):
        print(exception)
        return

    def on_error(self, status):
        print(status)

    def on_status(self, status):
        return

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['raga','gandhi','election','votede','bhajpa','loksabha','rss','votekar','shivsena','bjp','chowkidar','janata','indiancongress','janasena','aap','mulayam','tdp', 'bjd', 'bsp','samajwadi','mns','dmk','aiadmk','pdp','cpi','gatbandhan','tmc','trinamool'], stall_warnings=True)


