import os
import requests
import json
# import config #delete before deployment, but need it for local testing
# from pprint import pprint


# apiKey = os.environ["capitalone_api_key"]
merchant_id = "57cf75cea73e494d8675ec4a"

def get_all_merchants():
	url= 'http://api.reimaginebanking.com/merchants/?key={}'.format(apiKey)
	response = requests.get(url)
	return json.loads(response.text)

def get_merchant_name(merchant_Id, apiKey):
	url= 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(merchant_Id, apiKey)
	response = requests.get(url)
	return json.loads(response.text)

def get_merchant_id(merchant_Name, apiKey):
	url= 'http://api.reimaginebanking.com/merchants/?key={}'.format(apiKey)
	response = requests.get(url)
	response = json.loads(response.text)
	for i, mer in enumerate(response):
		if mer['name'] == merchant_Name:
			mer_id = mer["_id"]
			return mer_id

# def create_merchant(merchant_Name, category, )

# merchant_info = get_merchant_name(merchant_id)
# pprint(merchant_info['name'])
# pprint(get_all_merchants())

# print(get_merchant_id("Apple"))


