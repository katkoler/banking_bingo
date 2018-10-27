import os
import requests
import json
import config
from pprint import pprint

# apiKey = os.environ["capitalone_api_key"]

# accountId = os.environ["accountId"]

# Get a purchase 
def get_purchases(account_id):
  url_pur = 'http://api.reimaginebanking.com/accounts/{}/purchases?key={}'.format(account_id,apiKey)
  response = requests.get(url_pur)
  return json.loads(response.text)


# pprint(get_purchase(accountId))











