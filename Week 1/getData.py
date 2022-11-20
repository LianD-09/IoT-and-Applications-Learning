import requests
import json

idFile = open('return.txt', 'r')

id =idFile.readline()

idFile.close()

URL = 'https://api.thingspeak.com/channels/1529099/feeds.json?results=2'

# Sending get request and saving the response as response object
data = requests.get(url = URL).json()

# Save the data received
with open("data.json", "w") as f:
    json.dump(data, f)

f.close()

# Print the request data
print('Request data:',data)
print('---------------')
for i in data['feeds']:
    if i['entry_id'] == int(id):
        print('field1:', i['field1'])
        print('field2:', i['field2'])