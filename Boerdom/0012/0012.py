import sys
import requests # type: ignore

args = sys.argv
if len(args) != 2:
    sys.exit("Missing command-line argument")
if not args[1].isdigit():
    sys.exit("Command-line argument is not a number")

btc_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
btc_val = btc_data["bpi"]["USD"]["rate_float"]
btc_val = float(btc_val) * float(args[1])

print(f"${btc_val:,.4f}")