credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10",
}

username = input("What is your username? ")
password = input("What is your password? ")

if username not in credentials.keys():
    print("Not a valid user of the system.")
elif username in credentials.keys() and password != credentials[username]:
    print("Invalid password.")
else:
    print("You are now logged into the system.")