from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)

import requests
import constants

url = constants.API_URL

querystring = {"Category":"tennis","Date":"20210701"}

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
    return render_template('index.html', match1=matches[0], match2=matches[1])
    #return str(set(matches))
        #notify("Match", index["Cnm"])



