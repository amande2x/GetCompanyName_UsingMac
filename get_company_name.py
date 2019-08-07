import requests
import json
import sys 
#https://macaddress.io



# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://api.macaddress.io/v1?"
  
mac_address = sys.argv[1]

print("input mac:",mac_address)

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'apiKey':'at_BekVOuaEf4kakXdvV63GdKHlpIQSP', 'output' : 'json', 'search' : mac_address} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 

# print company name associated with input mac address
print (data['vendorDetails']['companyName'])
