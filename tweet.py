import pprint
import sys
from twython import Twython
import argparse


App_Key = 'HN5NhZPaXgNZQf05Se9S6oaj4'
App_Secret = 'msCNUjoAG1hzD2cL46MOpdGWEd75Obrz7XMtFny5cs7LYp9wA5'
# twitter = Twython(App_Key, App_Secret)
# auth = twitter.get_authentication_tokens()
Access_Token = '949862289108361216-rgxLJ7u4keWwe236J0D0J2MJ2r4SGBk'
Access_Secret = 'lHZXHEq3uTh8Topah8rPXr8b9cuHBzOJQkf5ZEQAuu7F0'
twit = Twython(App_Key, App_Secret, Access_Token, Access_Secret)


parser = argparse.ArgumentParser()
parser.parse_args()


def search(query, type):
    results = twit.search(q=query, result_type=type)  # search returns a dictionary
    # pprint.pprint(result)
    # results = twit.cursor(twit.search, q='python')
    count = 0
    for result in results['statuses']:
        count += 1
        print(str(count) + ': ' + result['text'])


def home_timeline():
    results = twit.get_home_timeline()
    count = 0
    for result in results:
        count += 1
        print(str(count) + ": " + result['text'])


def user_timeline(user):
    results = twit.get_user_timeline(screen_name=user)
    count = 0
    for result in results:
        count += 1
        print(str(count) + ": " + result['text'])


def update_status(status):
    twit.update_status(status=status)   


def follow_user(user):
    twit.create_friendship(screen_name=user, follow="true")  

# text = sys.argv[1]
# search_type = sys.argv[2]
# search('python', 'None')
# user_timeline('nithyanandh')
# update_status("@ShreyasSF Check2")
follow_user("nithyanandh")