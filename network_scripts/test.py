# goal: make network requests with python script

import requests

# res = requests.get('https://example.com/')
# print(res.text)


res = requests.get('https://www.epidemicsound.com/api/subscription_service/recurly/plans/')
print(type(res.text))

