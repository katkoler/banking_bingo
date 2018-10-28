import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

accountId = os.environ["accountId"]
accountId2 = os.environ["accountId2"]
accountId3 = os.environ["accountId3"]


url_trans = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(accountId3,apiKey)


transfer = {
  "medium": "balance",
  "payee_id": accountId2,
  "transaction_date": "2018-10-26",
  "status": "pending",
  "amount": 199,
  "description": "string"
}

# Create a new transaction

response = requests.post( 
  url_trans, 
  data=json.dumps(transfer),
  headers={'content-type':'application/json'},
  )


print(response)

if response.status_code == 201:
  print('transfer complete')



