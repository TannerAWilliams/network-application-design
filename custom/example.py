import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--IP_ADDRESS", help="This is the address of the rabbitMQ instance that is running", type=str)
parser.add_argument("-p", "--PORT", help="municate with", type=str)

# This gets the arguments from the user, access them through SERVER_PORT, etc
args = parser.parse_args()
addr = args.IP_ADDRESS
port = args.PORT

URL = "http://" + str(addr) +"/" + str(port)
 
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
 
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
 
# extracting data in json format
data = r.json()
 
 
# extracting latitude, longitude and formatted address 
# of the first matching location
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']
 
# printing the output
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address))