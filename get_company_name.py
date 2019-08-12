import requests
import json
import sys 
#https://macaddress.io



# importing the requests library 
import requests 
  
# api-endpoint 
URL = "https://api.macaddress.io/v1?"
  
def isMACaddressIsValid(input_str):
    if input_str.count(":")!=5:
        return False
    for each_i in input_str.split(":"):
        for char1 in each_i:
            if char1.upper()>"F" or (char1.upper()<"A" and not char1.isdigit()) or len(each_i) !=2: 
                return False
    return True


if len(sys.argv) < 2:
    print("Please provide MAC adress as input!!!")
    sys.exit(1)
else:
    mac_address = sys.argv[1]

while True:
    try:
        if isMACaddressIsValid(mac_address):
            break
        else: 
            mac_address = input("Error:Please enter valid MAC address:")
    except ValueError:
        print("Invalid mac address")
            
print("input mac:",mac_address)

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'apiKey':'at_BekVOuaEf4kakXdvV63GdKHlpIQSP', 'output' : 'json', 'search' : mac_address} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 

# print company name associated with input mac address
print (data['vendorDetails']['companyName'])
