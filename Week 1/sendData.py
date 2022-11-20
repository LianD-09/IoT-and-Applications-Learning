import requests
import json

f = open('return.txt', 'w')

URL = 'https://api.thingspeak.com/update?api_key=T7H40F0X82VGW7L5'

body = {
    'field1': 1509,
    'field2': 20194314
}

# Sending get request and saving the response as response object
r = requests.get(url=URL, json=body)

# Display the result
print("Request status:", r.status_code)
print("Body request:", body)
print("Return:", r.json())

# Save the return data received
f.write(str(r.json()))
f.close()