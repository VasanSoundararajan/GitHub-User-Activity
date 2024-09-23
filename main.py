import json
import requests
import os
import click
from pprint import pprint

@click.command()
@click.argument('name', default='VasanSoundararajan')

def main(name):
    # github username
    username = name
    # url to request
    url = f"https://api.github.com/users/{username}/events"
    # make the request and return the json
    user_data = requests.get(url).json()

    # Extract the activity information from the user data
    activities = []
    for event in user_data:
        activity = {
            "type": event.get("type"),
            "repo": event.get("repo", {}).get("name"),
            "created_at": event.get("created_at")
        }
        activities.append(activity)

    # Print the activities
    print("Activities:")
    for activity in activities:
        print(f"Type: {activity['type']}, Repo: {activity['repo']}, Created at: {activity['created_at']}")

    # Save the activities to a file
    if os.path.exists('Activities.json'):
        with open('Activities.json', 'r') as file:
            data = json.load(file)
            # If the data is a dictionary, turn it into a list for task management
            if isinstance(data, dict):
                data = [data]
    else:
        # Initialize data as an empty list if the file doesn't exist
        data = []
    data.extend(activities)  # Append the new activities to the list

    # Write the updated list back to the file
    with open('Activities.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()