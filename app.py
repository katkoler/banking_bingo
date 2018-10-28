from flask import Flask, render_template, request
from flask.json import jsonify
import json
import requests
import os
import ast
from get_activity import get_merchant_id, get_purchases, get_transactions, get_withdrawals, get_other_accounts, get_merchant_name, get_merchant_location



# import config #delete before deployment, but need it for local testing

apiKey = os.environ["capitalone_api_key"]

app = Flask("bangin_banking_bingo_app")
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
	# print(all_purchases)
	for i, task in enumerate(task_data):
		if task['status'] != "true":
			print(task)
			print(task['status'])
			type_of_transaction = task['type_of_transaction']
			#check if purchas meets a requirenment
			if type_of_transaction == "purchase":
				all_purchases = get_purchases(account_id, apiKey)
				task_merchant_name = task['merchant_name']
				if task_merchant_name != 666:
					if task.get('merchant_id') == None:
						task_mer_id = get_merchant_id(task_merchant_name, apiKey)
					else:
						task_mer_id = task['merchant_id']
					if task.get("location") != None:
						#check if a location specific task is set
						mer_loc = task.get("location")
						merchant_loc = get_merchant_location(task_mer_id, apiKey)
						if mer_loc == merchant_loc:
							task['status'] = "true"
							updated_tasks.append(task)							
					else:
						task_min_amount = task['transaction_amount_min']
						for j, pur in enumerate(all_purchases):
							if pur['merchant_id'] == task_mer_id:
								if pur['amount'] >= task_min_amount:
									task['status'] = "true"
									updated_tasks.append(task)
				else:
					task_min_amount = task['transaction_amount_min']
					for j, pur in enumerate(all_purchases):
						if pur['amount'] >= task_min_amount:
							task['status'] = "true"	
							#check if you made any puchases big enough than the amount specified in the task
							updated_tasks.append(task)

			#transfers
			elif type_of_transaction == "transfer":
				all_transactions = get_transactions(account_id, apiKey)
				#get all accounts from you
				other_accounts = get_other_accounts(account_id, apiKey)
				for i, item in enumerate(all_transactions):
					if item['payer_id'] == account_id:
						if item['payee_id'] != account_id:
							if item['payee_id'] in other_accounts:
								#you have sent money to another one of your account
								task['status'] = "true"
								# updated_tasks.append(task)
							else: 
							#you have sent money to a friend
								print("sending money to friend")
								task['status'] = "true"
								# updated_tasks.append(task)
				print("printing it here")
				updated_tasks.append(task)

			#withdrawals
			elif type_of_transaction == "withdrawal":
				#check if there was a withdrawal
				all_withdrawals = get_withdrawals(account_id, apiKey)
				if len(all_withdrawals) > 0:
					task['status'] = "true"
					updated_tasks.append(task)
				else:
					updated_tasks.append(task)
			else:
				updated_tasks.append(task)
		else:
			updated_tasks.append(task)
	return jsonify(updated_tasks)

@app.route("/activity/<account_id>",methods=['GET'])
def list_activities(account_id="5bd44f84322fa06b67793e85"):
	activities = []
	all_purchases = get_purchases(account_id, apiKey)
	all_transactions = get_transactions(account_id, apiKey)
	all_withdrawals = get_withdrawals(account_id, apiKey)
	for i, item in enumerate(all_purchases):
		item['name'] = get_merchant_name(item['merchant_id'], apiKey)
		activities.append(item)
	for i, item in enumerate(all_withdrawals):
		activities.append(item)
	for i, item in enumerate(all_transactions):
		if item['payer_id'] != account_id:
			item['amount'] = -item['amount']
			activities.append(item)
		else:
			activities.append(item)
	return jsonify(activities)

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
