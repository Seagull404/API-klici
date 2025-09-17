# API klici (spletni klici)

import requests
import pprint
#baseUrl = "https://www.google.com/"
#klic = requests.get(baseUrl)

#print(klic) #koda odgovora
#print(klic.text) #raw odgovor - t

"""
for i in range(2):
    # API klic z JSON odgovorom
    baseUrl = "https://api.chucknorris.io/jokes/random"
    klic = requests.get(baseUrl)

    # preverimo .text, da je 100% json
    js = klic.json() # pretvorimo klic v dict
    #pprint.pprint(js)
    print(js.get("value"))
"""

baseUrl = "https://api.nationalize.io/?name="
ime = "David"

klic = requests.get(baseUrl+ime).json()
#print(klic.url) #preverimo klic
#print(klic)

print(f"{klic.get("count")=}")
print(f"{klic.get("name")=}")

drzave = klic.get("country")
for d in drzave:
    print(d.get("country_id"))
    print(d.get("probability"))

#popravite izpis da bo lepši v procentih