'''
command line argument hoga {if not "Missing command-line argument"}
    agar vo number float me change nhi ho sakta => sys.exit
    "Command-line argument is not a number"

use requests lib
response = get the dict form [requests.get("path")]
then see (for once) the dict using [json.dumps(response.json(), indent=2)]
see what is your desired location then delete line 8
get the desired numbers [ans["bpi"]["USD"]["rate_float"]]
and get the output [print("$" + '{:,}'.format(amount_btc * n))]
'''
# import json
# import requests

# response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# # print(json.dumps(response.json(), indent = 2))

# ans = response.json()
# # "bpi" -> "USD" -> "rate_float"

# ans2 = ans["bpi"]["USD"]["rate_float"]

# print(ans2)
