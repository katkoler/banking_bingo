import os
import requests
import json
import ast
# import config #delete before deployment, but need it for local testing
# from pprint import pprint


# apiKey = os.environ["capitalone_api_key"]
merchant_id = "57cf75cea73e494d8675ec4a"

#get purchases
def get_all_merchants():
	url= 'http://api.reimaginebanking.com/merchants/?key={}'.format(apiKey)
	response = requests.get(url)
	return json.loads(response.text)

def get_merchant_name(merchant_Id, apiKey):
	url= 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(merchant_Id, apiKey)
	response = requests.get(url)
	merchant_info = json.loads(response.text)
	mer_name = merchant_info["name"]
	return mer_name


def get_merchant_id(merchant_Name, apiKey):
	url= 'http://api.reimaginebanking.com/merchants/?key={}'.format(apiKey)
	response = requests.get(url)
	response = json.loads(response.text)
	for i, mer in enumerate(response):
		if mer['name'] == merchant_Name:
			mer_id = mer["_id"]
			return mer_id

def get_merchant_location(merchant_Id, apiKey):
	url= 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(merchant_Id, apiKey)
	response = requests.get(url)
	response = json.loads(response.text)
	print(response)
	mer_location = response['address']['city']
	return mer_location

# def create_merchant(merchant_Name, category, )

# merchant_info = get_merchant_name(merchant_id)
# pprint(merchant_info['name'])
# pprint(get_all_merchants())

# print(get_merchant_id("Apple"))

# Get a purchase 
def get_purchases(account_id, apiKey):
	url_pur = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(account_id,apiKey)
	response = requests.get(url_pur)
	return json.loads(response.text)

#Get transactions
def get_transactions(account_id, apiKey):
	url_pur = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(account_id,apiKey)
	response = requests.get(url_pur)
	return json.loads(response.text)


# Get withdrawls
def get_withdrawals(account_id, apiKey):
	url_pur = 'http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}'.format(account_id,apiKey)
	response = requests.get(url_pur)
	return json.loads(response.text)

#get a list of all other accounts you have
def get_other_accounts(account_id, apiKey):
	#get customer id first
	url_pur = 'http://api.reimaginebanking.com/accounts/{}?key={}'.format(account_id,apiKey)
	response = requests.get(url_pur)
	account_info = json.loads(response.text)
	customer_id = account_info['customer_id']
	print(customer_id)
	#get all the accounts from that customer id
	url_pur = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_id,apiKey)
	response = requests.get(url_pur)
	all_accounts = json.loads(response.text)
	all_account_ids = []
	for i, item in enumerate(all_accounts):
		print(item)
		acc_id = item.get('_id')
		print(acc_id)
		all_account_ids.append(acc_id)
	return all_account_ids



