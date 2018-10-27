import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

customerId = '5bd44f83322fa06b67793e83'
accountId = '5bd44f84322fa06b67793e85'

url_pay = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,	
}
url_pur = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(accountId,apiKey)
purchase = {
  "merchant_id": "57cf75cea73e494d8675ec4a",
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 99,
  "status": "pending",
  "description": "everything"
}
# Create a Savings Account
response = requests.post( 
	url_pay, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)
print(url_pay)
print(response)

if response.status_code == 201:
	print('account created')

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