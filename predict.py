import requests
import json

port = 5000

try:
    requests.post('http://127.0.0.1:{}/predict'.format(port))
    server_available = True
except:
    server_available = False
    
#result = model_predict('netherlands','2018','08','01',test=False)


request_json = {'country':'all','year':'2018','month':'05','day':'01'}
r = requests.post('http://127.0.0.1:{}/predict'.format(port),json=request_json)

print("All: ", r.text)        

request_json = {'country':'united_kingdom','year':'2018','month':'05','day':'01'}
r = requests.post('http://127.0.0.1:{}/predict'.format(port),json=request_json)

print("United Kingdom: ", r.text)