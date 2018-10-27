import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

accountId = os.environ["accountId"]


url_pur = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(accountId,apiKey)
purchase = {
  "merchant_id": "57cf75cea73e494d8675ec4a",
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 1,
  "status": "pending",
  "description": "everything"
}

# Create a purchase	
response = requests.post( 
	url_pur, 
	data=json.dumps(purchase),
	headers={'content-type':'application/json'},
	)
print(url_pur)
print(response)


if response.status_code == 201:
	print('purchase created')