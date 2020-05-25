# use the request module to:
#1 - in "get" function, send a GET request to request to http://httpbin.org/status/204 and return the status code. 
#2 - in "post", send a POST request to http://httpbin.org/post with data:
#   x = 1
#   y = 2 
#   then return the response


import requests
import json

def get():
    url = "http://httpbin.org/status/204"
    req = requests.get(url)
    return req.status_code

def post():
    url="http://httpbin.org/post"
    req = requests.post(url, json={"x":"1","y":"2"})
    response = req.json()
    return(response)

# the following  version works in the submit action into the course codeboard.
    #url = "http://httpbin.org/post"
    #payload = {'x': '1', 'y':'2'}
    #r = requests.post(url, data=json.dumps(payload))
    #response_dict = json.loads(r.text)
    #print(response_dict['data'])
    #return json.dumps(response_dict['data'])

print(get())
print(post())