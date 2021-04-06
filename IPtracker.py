# Feito por: Mainjota
# Editado, reduzido e otimizado para Py3/Py2
# Segue no twitter: http://twitter.com/mainjota
# Só isso mesmo, tamo junto.

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

    print(" IP do otário: " +  values['query'])
    print(" Cidade do otário: " + values['city'])
    print(" Internet do otário: " + values['isp'])
    print(" País do otário: " + values['country'])
    print(" Estado do otário: " + values['region'])
    print(" Fuso do horário do otário: " + values['timezone'])


    break
input("Pressione alguma tecla")
