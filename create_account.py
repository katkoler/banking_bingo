import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

customerId = os.environ["customerId"]
# customerId = "5bd44f83322fa06b67793e83"

url_pay = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "Random Account",
  "rewards": 10000,
  "balance": 50000,	
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