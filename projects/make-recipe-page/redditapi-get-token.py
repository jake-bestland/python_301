# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.



import requests
import requests.auth
from pprint import pprint

client_auth = requests.auth.HTTPBasicAuth('*InsertCLIENT_ID*', '*InsertCLIENT_SECRET*')
post_data = {"grant_type": "password", "username": "*InsertUSERNAME*", "password": "*InsertPASSWORD*"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
response.json()

headers = {"Authorization": "bearer *InsertACCESS_TOKEN*", "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)

response.json()

recipes = requests.get("https://oauth.reddit.com/r/recipes/hot", headers=headers)
recipes.json()

for post in recipes.json()['data']['children']:
    pprint(post)