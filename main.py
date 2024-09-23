import json
import requests
import os
from pprint import pprint

# github username
username = "VasanSoundararajan"
# url to request
url = f"https://api.github.com/users/{username}/events"
# make the request and return the json
user_data = requests.get(url).json()
# pretty print JSON data
if os.path.exists('Data.json'):
    with open('Data.json', 'r') as file:
        data = json.load(file)
        # If the data is a dictionary, turn it into a list for task management
        if isinstance(data, dict):
            data = [data]
else:
    # Initialize data as an empty list if the file doesn't exist
    data = []
data.append(user_data)  # Append the new task to the list

# Write the updated list back to the file
with open('Data.json', 'w') as f:
    json.dump(user_data, f, indent=4)
pprint(user_data)