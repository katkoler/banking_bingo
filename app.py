from flask import Flask, render_template, request
from flask.json import jsonify
import json
import requests
import os

import config #delete before deployment, but need it for local testing

app = Flask("teamg_app")
tasks_json_file = "tasks.json"

with open(tasks_json_file) as f:
    task_data = json.load(f)

@app.route("/")
def home():
	return render_template("index.html")

# @app.route('/search',methods=['POST','GET'])
# def search():
# 	if request.method=='POST':
# 		searchterm=request.form['searchbox']
# 		n=request.form['numbertweets']
# 		return render_template("hashtags.html", searchterm=searchterm, numbertweets=n)

# @app.route("/about")
# def about():
# 	profiles = get_profiles()
# 	return render_template("about.html", members=profiles, enumerate=enumerate)

@app.route("/tasks/update/<account_id>",methods=['GET'])
def update_tasks(account_id="5bd44f84322fa06b67793e85"):
	for i, task in enumerate(task_data):
		type_of_transaction = task['type_of_transaction']
		merchant_name = task['merchant_name']
#     short_json = shorten_json(tweets)
#     loc_json = geolocate_tweet(short_json)
#     return jsonify({"markers": [tweet for i, tweet in enumerate(loc_json)]})


"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at https://www.heroku.com/ before the deployment session!). When
running the app on Heroku, the PORT environment/config variable is pre-populated by
Heroku to tell our app the correct port to run on.
"""
if "PORT" in os.environ:
	app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
	app.run(debug=True)
