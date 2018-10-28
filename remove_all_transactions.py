### DOES NOT WORK YET!


import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

accountId = os.environ["accountId"]

# call current transactions

url_pur_get = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(accountId,apiKey)
url_trans_get = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(accountId,apiKey)
url_with_get = 'http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}'.format(accountId,apiKey)


# Get list of purchase IDs

purchases = requests.get(url_pur_get)
transfers = requests.get(url_trans_get)
withdrawals = requests.get(url_with_get)


pur_info = json.loads(purchases.text)
# print(pur_info)
trans_info = json.loads(transfers.text)
# print(trans_info)
# with_info = json.loads(withdrawals.text)
# print(with_info)




for i, item in enumerate(pur_info):
	pur_id = item["_id"]
	pur_id_send = [{
		  "_id": pur_id,
		  "code": 0,
		  "message": "string",
		  "fields": "string"
		}]
	url_pur_del = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(pur_id_send,apiKey)
	response = requests.delete(url_pur_del, 
		data=json.dumps(pur_id_send),
  		headers={'content-type':'application/json'})
	print(pur_id)
	print(response)
	if response.status_code == 201:
		print('purchases created')



for i, item in enumerate(pur_info):
	pur_id = item["_id"]
	pur_id_send = [{
		  "_id": pur_id,
		  "code": 0,
		  "message": "string",
		  "fields": "string"
		}]
	url_trans_del = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(_id,apiKey)
	response = requests.delete(url_trans_del, 
		data=json.dumps(pur_id_send),
  		headers={'content-type':'application/json'})
	print(pur_id)
	print(response)
	if response.status_code == 201:
		print('purchases created'

	

# for i, item in enumerate(pur_info):
# 	_id = item["_id"]
# 	url_with_del = 'http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}'.format(_id,apiKey)








