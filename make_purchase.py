import os
import requests
import json
import config

apiKey = os.environ["capitalone_api_key"]

accountId = os.environ["accountId"]
accountId2 = os.environ["accountId2"]

url_pur = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(accountId2,apiKey)

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
  "merchant_id": "57cf75cea73e494d8675ec49", # More than £100 in 1 transaction at Apple
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 105,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "5ade2542f0cec56abfa40730", # Spend £10 or more at tesco
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 10.50,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "5b06eeeff0cec56abfa40907", # Buy from Amazon.com
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 24.99,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "57cf75cea73e494d8675edd7", # Buy Coffee at Starbucks
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 10.50,
  "status": "pending",
  "description": "everything"
},{
  "merchant_id": "57cf75cea73e494d8675edad", # Buy lunch from Subway
  "medium": "balance",
  "purchase_date": "2018-10-27",
  "amount": 4.99,
  "status": "pending",
  "description": "everything"
}]


# {
#   "merchant_id": "5555555", # Send money to a friend
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 10.50,
#   "status": "pending",
#   "description": "everything"
# },{
#   "merchant_id": "5555555", # Transfer to savings account
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 10.50,
#   "status": "pending",
#   "description": "everything"
# },

#{
#   "merchant_id": "583aadf10fa692b34a9b89f4", # Make purchase in Sheffield
#   "medium": "balance",
#   "purchase_date": "2018-10-27",
#   "amount": 10.50,
#   "status": "pending",
#   "description": "everything"
# },


# {
#   "merchant_id": "5555555", # withdraw some cash
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





