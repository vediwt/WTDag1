print('Start API read application')

import requests

#Voor een URL importeren moet je https gebruiken
paginaresults = requests.get('https://catfact.ninja/facts')
print(paginaresults)

feitjes = paginaresults.json()
print(feitjes["current_page"])
#Eerste lijst nummer is altijd 0
print(feitjes["data"][0]["fact"])
