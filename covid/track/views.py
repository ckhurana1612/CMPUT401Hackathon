from django.shortcuts import render
import requests

def home(req, name="Canada"):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-key': "cbef3ad3damsh177a38ec66e4f95p1a51f3jsne5512dc00c01",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    r=response.json() 
    r=r["response"]
    countrylist=[x["country"] for x in r]
    i=1
    while (countrylist[i]!=name):
        i+=1
    countrylist=sorted(countrylist)
    return render(req,'home.html',{"countrylist":countrylist,"details":r[i]})
