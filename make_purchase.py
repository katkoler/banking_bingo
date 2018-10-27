import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

accountId = os.environ["accountId"]

url_pur = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(accountId,apiKey)

# purchase = {
#   "merchant_id": "57cf75cea73e494d8675ec4a",
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 1,
#   "status": "pending",
#   "description": "everything"
# }

# # Create a purchase 
# response = requests.post( 
#   url_pur, 
#   data=json.dumps(purchase),
#   headers={'content-type':'application/json'},
#   )
# print(url_pur)
# print(response)

# if response.status_code == 201:
#   print('purchase created')

purchases = [{
  "merchant_id": "57cf75cea73e494d8675ec4a", # More than £100 in 1 transaction
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 105,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "57cf75cea73e494d8675ec4a", # Spend £10 or more at tombola
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 10.50,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "57cf75cea73e494d8675ec4a", # Buy from Amazon
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 24.99,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "57cf75cea73e494d8675ec4a", # Buy Coffee at Starbucks
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 10.50,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "57cf75cea73e494d8675ec4a", # Buy lunch from Subway
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 4.99,
  "status": "pending",
  "description": "everything"
}]


# {
#   "merchant_id": "57cf75cea73e494d8675ec4a", # Send money to savings account
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 10.50,
#   "status": "pending",
#   "description": "everything"
# },{
#   "merchant_id": "57cf75cea73e494d8675ec4a", # Transfer to regular saver
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 10.50,
#   "status": "pending",
#   "description": "everything"
# },{
#   "merchant_id": "57cf75cea73e494d8675ec4a", # Direct Debit to Giff Gaff
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 10.50,
#   "status": "pending",
#   "description": "everything"
# },


# {
#   "merchant_id": "57cf75cea73e494d8675ec4a", # withdraw some cash
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 10.50,
#   "status": "pending",
#   "description": "everything"
# }]


# Create a purchase 

for i, pur in enumerate(purchases):
  response = requests.post( 
  url_pur, 
  data=json.dumps(pur),
  headers={'content-type':'application/json'},
  )


print(response)

if response.status_code == 201:
	print('purchases created')













