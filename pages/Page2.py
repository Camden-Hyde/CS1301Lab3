# overwatch api: https://overfast-api.tekrop.fr/heroes

import streamlit as st
import pandas as pd
import json
import requests

baseUrl = "https://overfast-api.tekrop.fr/"
endpoint = baseUrl + "heroes"
resp = requests.get(endpoint)
data = resp.json()

#print(len(data))

heroList = []
for item in data:
    name = item["name"]
    heroList.append(name)
    
#print(heroList)

# Dynamic / interactable chart

st.divider()
st.header("Interactable Chart")

st.multiselect("Which heroes do you want to display?", heroList, key = "chosen_heroes")

st.write(st.session_state["chosen_heroes"])
for hero in st.session_state["chosen_heroes"]:
    baseUrl = "https://overfast-api.tekrop.fr/heroes/"
    endpoint = baseUrl + hero.lower
    resp = requests.get(endpoint)
    data = resp.json()

    pass
