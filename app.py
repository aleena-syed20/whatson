from flask import Flask, render_template
from datetime import date
app = Flask(__name__)

import requests
import constants

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



