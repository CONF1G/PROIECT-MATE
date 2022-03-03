from pprint import pprint
import requests
import os
import urllib.parse

appid = "4KUYY6-Y8T2XXLWVL"

query = urllib.parse.quote_plus(input("> "))
query_url = f"http://api.wolframalpha.com/v2/query?" \
             f"appid={appid}" \
             f"&input={query}" \
             f"&format=plaintext" \
             f"&output=json"

r = requests.get(query_url).json()

data = r["queryresult"]["pods"][0]["subpods"][0]
plaintext = data["plaintext"]

print(f"Result: {plaintext}")
