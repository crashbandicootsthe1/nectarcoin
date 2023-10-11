import datetime
import random
import json
import os

import scratchattach as scratch3

# Your username and session setup
username = "crashbandicootsthe1"
session = scratch3.Session(os.environ["SESSION_ID"], username=username)
conn = session.connect_cloud("854753637")
client = scratch3.CloudRequests(conn)

REQUESTS_PER_MINUTE = 30
MINUTE_IN_SECONDS = 60

# Initialize last_request_time
last_request_time = datetime.datetime.now()

# Initialize user_data dictionary
user_data = {}

# Function to load user data from a JSON file
def load_user_data():
    global user_data
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as data_file:
            user_data = json.load(data_file)

# Function to save user data to a JSON file
def save_user_data():
    with open("user_data.json", "w") as data_file:
        json.dump(user_data, data_file, indent=4)

# Function to check the Nectarcoin balance
@client.request
def check_balance(username):
    if username in user_data:
        return user_data[username]['nectarcoin_balance']
    else:
        # Initialize user with 150 Nectarcoins and today's date
        user_data[username] = {
            'nectarcoin_balance': 150,
            'last_claim_date': datetime.datetime.now().strftime("%Y-%m-%d")
        }
        save_user_data()
        return 150  # Return the initial balance

# Function to claim daily Nectarcoin
@client.request
def claim_daily_nectarcoin(username):
    global last_request_time
    current_time = datetime.datetime.now()
    time_since_last_request = current_time - last_request_time

    if time_since_last_request.total_seconds() < MINUTE_IN_SECONDS / REQUESTS_PER_MINUTE:
        return "Too many requests. Please try again later."

    last_request_time = current_time

    linked_user_info = get_linked_username(username)
    linked_username = linked_user_info.get("linked_username")

    if linked_username is not None:
        if linked_username in user_data:
            last_claim_date = datetime.datetime.strptime(user_data[linked_username]["last_claim_date"], "%Y-%m-%d")
            if current_time.date() > last_claim_date.date():
                user_data[linked_username]["nectarcoin_balance"] += 15
                user_data[linked_username]["last_claim_date"] = current_time.strftime("%Y-%m-%d")
                save_user_data()
                return f"You claimed 15 Nectarcoins for {linked_username} today!"
            else:
                return f"You have already claimed Nectarcoins today for {linked_username}."
        else:
            return f"User '{linked_username}' not found in user_data."
    else:
        return "No linked user found."

# Function to get linked username
@client.request
def get_linked_username(username):
    linked_username = username  # Replace this with your implementation to get the linked username
    return {"linked_username": linked_username}

@client.event
def on_request(request):
    print("Received request", request.name, request.requester, request.arguments, request.timestamp, request.id)

if __name__ == "__main__":
    load_user_data()
    client.run()
