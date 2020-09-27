#This app relies on https://exchangeratesapi.io/ 's api in order to get exchange rates.
#Exchange rates may NOT be %100 true ALL times!

import requests
import json
import os

mode = 0 #(0 or 1) 0 Makes everything work the other way around. Chances are this is what you are looking for.
base = "TRY" #Your base currency
var_s = ["EUR","USD"] #Variable currencies. Use , between each one
delay = 10000 #Notification time delay. Try with different integers to find the best for you.
rates = requests.get(f"https://api.exchangeratesapi.io/latest?base={base}").content
rates_json = json.loads(rates)["rates"]
coms = ""

if mode == 0:
    for var in var_s:
        rate=(float(rates_json[var]))
        rate = 1/rate
        rate=(float("{:.2f}".format(rate)))
        coms=coms+(f"'1 {var} = {rate} {base}\n'")

    os.system(f"notify-send {coms} -t {delay}")


elif mode == 1:
    for var in var_s:
        rate=(rates_json[var])
        rate=("{:.2f}".format(rate))
        coms=coms+f"'\n = {rate} {var}'"
        rate=(rates_json[var])
        rate=("{:.2f}".format(rate))

    os.system(f"notify-send '1 {base}' {coms} -t {delay}")