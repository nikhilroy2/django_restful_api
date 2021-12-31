from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .helper import PriceJson
import requests
import json
# Create your views here.
def Index(request):
    data = PriceJson()
    output = ''
    for data in data["data"]:
        output += f'<span style="color: red; padding-left: 5px;"> {data["name"]} </span>'
    
    #json_res = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    #print(json(json_res.json()))


    return HttpResponse(f'<div> {output} </div>')