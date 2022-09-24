import os
import urllib.request as urllib2
import json
import requests

while True:
    ip=input("IP Alvo: ")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)

    print(" IP: " +  values['query'])
    print(" Cidade: " + values['city'])
    print(" Internet: " + values['isp'])
    print(" País: " + values['country'])
    print(" Estado: " + values['region'])
    print(" Fuso: " + values['timezone'])


    break
input("Pressione alguma tecla")
