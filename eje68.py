import json
import requests
from pprint import pprint
from os import system

system("cls")

response = requests.get(
"https://jsonplaceholder.typicode.com/todos")
pendientes = json.loads(response.text)
#imprime el json cargado
pprint(pendientes[:2])

