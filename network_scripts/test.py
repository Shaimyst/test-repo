# goal: make network requests with python script

import requests
import json

# res = requests.get('https://example.com/')
# print(res.text)


res = requests.get('https://www.epidemicsound.com/api/subscription_service/recurly/plans/')

res_json = res.text
res_data = json.loads(res_json)
back_to_json = json.dumps(res_data)
print(type(str(res_data)))
print(type(back_to_json))