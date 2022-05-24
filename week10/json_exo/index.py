#
# import json

# json_file = 'file.json'
# with open(json_file, 'r') as file_obj:
#     my_family = json.load(file_obj)

# print(my_family)

import requests

requests.get('api_link')
response = requests.get("http://api.open-notify.org/iss-now.json")

print(response.status_code)
