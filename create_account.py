import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

customerId = os.environ["customerId"]

url_pay = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "Kirsty's Account",
  "rewards": 1000000,
  "balance": 1000000,	
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
