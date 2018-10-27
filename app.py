from flask import Flask, render_template, request
from flask.json import jsonify
import json
import requests
import os
from get_merchants import get_merchant_id
from get_purchase import get_purchases

# import config #delete before deployment, but need it for local testing

apiKey = os.environ["capitalone_api_key"] 

app = Flask("teamg_app")
tasks_json_file = "task_match.json"

with open(tasks_json_file) as f:
	# task_data = json.dumps(f)
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
	updated_tasks = []
	all_purchases = get_purchases(account_id)
	# print(all_purchases)
	for i, task in enumerate(task_data):
		print(task)
		type_of_transaction = task['type_of_transaction']
		# print(type_of_transaction)
		if type_of_transaction == "purchase":
			task_merchant_name = task['merchant_name']
			if task_merchant_name != 666:
				if task.get('merchant_id') == None:
					task_mer_id = get_merchant_id(task_merchant_name)
				else:
					task_mer_id = task['merchant_id']
				task_min_amount = task['transaction_amount_min']
				for j, pur in enumerate(all_purchases):
					if pur['merchant_id'] == task_mer_id:
						if pur['amount'] >= task_min_amount:
							task['status'] = "true"
							print("how many times")
							updated_tasks.append(task)
			else:
				updated_tasks.append(task)
		elif type_of_transaction == "transfer":
			print("transfer")
			updated_tasks.append(task)
		elif type_of_transaction == "withdrawl":
			print("withdrawl")
			updated_tasks.append(task)
		else:
			print("nothing")
			updated_tasks.append(task)

	return jsonify(updated_tasks)

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
