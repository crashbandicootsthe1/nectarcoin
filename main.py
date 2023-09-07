import datetime
import json
import os

os.system ("pip install --upgrade -U scratchattach")
os.environ["SESSION_ID"] = ".eJxVUEFugzAQ_IvPKcUG2yS39NYcWqk55YQWewEXsCMwikrVv3ctccltNTszO7O_bF1w9jAhOzEzw9I34K0zIcQl9sjZgdWwxr5OtNpZYlVca13kilYRl0jUwSX1I8wD2mdBA2ZAn1QJQx-dgeiCz_bFkn3hfdzBt51MvoEGEukS4JhX1mgNpebtUQkpihIbaKRG254ul6516vwj9Hbb8m0b5HKdts93uBqyGUPn_Iu7k5PM-FFmZSZKmRKO4LsVuhSbDh2Y_SYg1NFNuAWf4POEM-V6_cBHfaNmz716elQq1WqlykoZLcAKibYphMyNBbAV8gqAS1CWW_b3D9sbdrQ:1q0vnp:o8KgDTfwAwj2jKhTuU40ceVp5fk"
import scratchattach as scratch3

session = scratch3.Session(os.environ["SESSION_ID"], username="crashbandicootsthe1")
conn = session.connect_cloud("854753637")

client = scratch3.CloudRequests(conn)

@client.request
def connect():
  linked_user = session.get_linked_user()
  return linked_user


@client.request
def ping():
    print ("ping recieved")
    return "pong" # Return a response



# Function to load user data from a JSON file
def load_user_data():
    if os.path.exists('user_data.json'):
        try:
            with open('user_data.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}
            return session.get_linked_user
            return balance
    else:
        return {}

# Function to save user data to a JSON file
def save_user_data(user_data):
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file, indent=4)

# Function to add Nectarcoin to a user's account and update user data
# Function to add Nectarcoin to a user's account and update user data
def add_nectarcoin(user_data, linked_user, amount):
    if linked_user in user_data:
        user_data[username]['nectarcoin'] += amount
    else:
        user_data[username] = {'nectarcoin': amount, 'last_claim_date': datetime.date.today().isoformat()}  # Start with 150 Nectarcoin

# Rest of your code...


# Function to claim daily Nectarcoin and update user data
def claim_daily_nectarcoin(user_data, username):
    today = datetime.date.today()
    if username in user_data:
        last_claim_date = user_data[username].get('last_claim_date')
        if last_claim_date != today.isoformat():
            user_data[username]['nectarcoin'] += 15
            user_data[username]['last_claim_date'] = today.isoformat()
            save_user_data(user_data)  # Save the updated user_data to the JSON file
    else:
        # Add the missing user to the database with an initial balance of 150 and today's date
        user_data[username] = {'nectarcoin': 150, 'last_claim_date': today.isoformat()}  # Start with 150 Nectarcoin
        save_user_data(user_data)  # Save the updated user_data to the JSON file

# Rest of your code...


# Function to check Nectarcoin balance
def check_balance(user_data, username):
    if username in user_data:
        return user_data[username]['nectarcoin']
    else:
        # Add the missing user to the database with an initial balance of 150
        today = datetime.date.today()
        user_data[username] = {'nectarcoin': 150, 'last_claim_date': today.isoformat()}
        save_user_data(user_data)  # Save the updated user_data to the JSON file
        return 150  # Return 150 as the initial balance for the missing user

# ... (previous code)

# Function to establish a connection


# ... (previous code)

# Main program
if __name__ == "__main__":
    user_data = load_user_data()

    while True:
        print("Nectarcoin Menu:")
        print("1. Check Balance")
        print("2. Claim Daily Nectarcoin")
        print("3. Send Nectarcoin")
        print("4. Connect")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            username = input("Enter your username: ")
            balance = check_balance(user_data, username)
            print(f"Your Nectarcoin balance: {balance}")
        
        elif choice == "2":
            username = input("Enter your username: ")
            claim_daily_nectarcoin(user_data, username)
            print("You have claimed 15 Nectarcoin for today.")
        
        elif choice == "3":
            sender = input("Enter your username (sender): ")
            receiver = input("Enter receiver's username: ")
            amount = int(input("Enter the amount to send: "))
            
            if sender in user_data and user_data[sender]['nectarcoin'] >= amount:
                add_nectarcoin(user_data, receiver, amount)
                user_data[sender]['nectarcoin'] -= amount
                print(f"{amount} Nectarcoin sent to {receiver}.")
            else:
                print("Insufficient funds.")
        
        elif choice == "4":
            try:
                connect()
                
                print("Connection established.")
            except Exception as e:
                print(f"Failed to connect: {e}")
        
        elif choice == "5":
            save_user_data(user_data)
            print("Exiting Nectarcoin.")
            break
        
        else:
            print("Invalid choice. Please try again.")


client.run()
