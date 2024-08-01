# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import sys
import requests
import json

# If user didn't gave Command line argument
if len(sys.argv) != 2:
    print("Missing command-line argument")
    exit(
        1
    )  # Manually typed 1 because they want us to give exit code as 1 not 0. but if you dont type anything => returns 0 maybe

try:
    n = float(sys.argv[1])  # If Error occurs then it goes to last one exception
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    amount_btc = response.json()
    amount_btc = amount_btc["bpi"]["USD"]["rate_float"]

    print("$" + "{:,}".format(amount_btc * n))

except requests.RequestException:
    sys.exit("Unknown")
except:
    sys.exit("Command-line argument is not a number")
