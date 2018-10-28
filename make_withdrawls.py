import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

accountId = os.environ["accountId"]


url_with = 'http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}'.format(accountId,apiKey)


withdrawl = {
  "medium": "balance",
  "transaction_date": "2018-10-27",
  "status": "pending",
  "amount": 1995,
  "description": "string"
}

# Create a new transaction
response = requests.post( 
  url_with, 
  data=json.dumps(withdrawl),
  headers={'content-type':'application/json'},
  )


print(response)

if response.status_code == 201:
  print('withdrawl made')



# Output
# [
#     {
#         "_id": "5bd4db6cf0cec56abfa4410d",
#         "medium": "balance",
#         "transaction_date": "2018-10-27",
#         "status": "pending",
#         "amount": 1995,
#         "description": "string",
#         "type": "withdrawal",
#         "payer_id": "5bd48ec6f0cec56abfa440e9"
#     }
# ]