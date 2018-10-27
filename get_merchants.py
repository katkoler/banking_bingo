import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]
merchant_id = "57cf75cea73e494d8675ec4a"

def get_all_merchants():
	url= 'http://api.reimaginebanking.com/merchants/?key={}'.format(apiKey)
	response = requests.get(url)
	return json.loads(response.text)

def get_merchant_name(merchant_Id):
	url= 'http://api.reimaginebanking.com/merchants/{}?key={}'.format(merchant_Id, apiKey)
	response = requests.get(url)
	return json.loads(response.text)

merchant_info = get_merchant_name(merchant_id)
print(merchant_info['name'])