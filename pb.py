from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import json
import http.client

load_dotenv()


conn = http.client.HTTPSConnection("api.collectapi.com")
key = os.getenv("API_KEY", str)
headers = {'content-type': "application/json",'authorization': f"apikey {key}"}

conn.request("GET", "/chancegame/usaPowerball", headers=headers)

res = conn.getresponse()
data = res.read()

data.decode("utf-8")

powerball_dict = json.loads(data)
next_jackpot3 = powerball_dict['result']['next-jackpot']['amount']


if "Billion" in next_jackpot3:
    
        next_jackpot2 = next_jackpot3.replace("$","")
        next_jackpot = next_jackpot2.replace("Billion","")
        new_jackpot = next_jackpot.replace(" ","")
        number_before = float(new_jackpot)
        number_after = number_before*1000000000

    
        buy_in = 2
        odds = 1 / 292201338
        jackpot = round(number_after)
        EV_of_ticket = round(odds*jackpot, 3)
        alpha = EV_of_ticket - buy_in
        
if "Million" in next_jackpot3:
        
        next_jackpot2 = next_jackpot3.replace("$","")
        next_jackpot = next_jackpot2.replace("Million","")
        new_jackpot = next_jackpot.replace(" ","")
        number_before = float(new_jackpot)
        number_after = number_before*1000000

    
        buy_in = 2
        odds = 1 / 292201338
        jackpot = round(number_after)
        EV_of_ticket = round(odds*jackpot, 2)
        alpha = EV_of_ticket - buy_in
        


