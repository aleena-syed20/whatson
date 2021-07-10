from flask import Flask, render_template
from datetime import date
app = Flask(__name__)

import requests
import constants
import tweepy


url = constants.API_URL
today = date.today()
d1 = today.strftime("%Y%m%d")

querystring = {"Category":"tennis","Date":d1}

headers = {
    'x-rapidapi-key': constants.API_KEY,
    'x-rapidapi-host': constants.API_HOST
    }

response = requests.request("GET", url, headers=headers, params=querystring)

jsonResponse = response.json()

@app.route("/")
def live_matches():
    matches = []
    for index in jsonResponse["Stages"]:
        matches.append(index["Cnm"])
    print(matches)
    if "ATP" in matches:
        matches.remove("ATP")
    if "WTA" in matches:
         matches.remove("WTA")
    umatches = set(matches)
    return render_template('index.html', umatches=umatches)

@app.route("/tweets")
def tweets():
    auth = tweepy.OAuthHandler(constants.TWEEPY_API_KEY, constants.TWEEPY_API_SECRET_KEY)
    api = tweepy.API(auth)

    screen_name = "josemorgado"
    user = api.get_user(screen_name)
    ID = user.id_str
    number_of_tweets = 5
    tweets = api.user_timeline(user_id=ID, count=number_of_tweets, include_rts = False, tweet_mode="extended")
    tweets = list(tweets)
    return render_template('tweets.html', tweets=tweets)



