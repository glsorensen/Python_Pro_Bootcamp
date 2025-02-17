from art import logo

print(logo)
# TODO-1: Ask the user for input

name = input("What is your name?\n")
bid = input("What is your bid?\n")

# TODO-2: Save data into dictionary {name: price}
name_bid = {}
name_bid[name] = bid

print(name_bid)

# TODO-3: Whether if new bids need to be added
def key_with_max_value(my_dict):
    if not my_dict:
        return None  # Return None for an empty dictionary
    return max(my_dict, key=my_dict.get)

def more_bids_needed():
    more_bids = input("Are there any more bidders? y/n")
    while more_bids == "y":
        print("\n" * 50)
        name = input("What is your name?")
        bid = input("What is your bid?")
        name_bid[name] = bid
        more_bids = input("Are there any more bidders? y/n")
    else:
        max_key = key_with_max_value(name_bid)
        print(f"{max_key} is the winner with a winning bid of ${int(name_bid[max_key])}")
# TODO-4: Compare bids in dictionary

more_bids_needed()




from art import logo

print(logo)

# Function to get the key with the maximum value in a dictionary
def key_with_max_value(my_dict):
    if not my_dict:
        return None  # Return None for an empty dictionary
    return max(my_dict, key=my_dict.get)

# Function to handle the bidding process
def more_bids_needed():
    name_bid = {}  # Dictionary to store names and bids

    while True:
        # Ask the user for input
        name = input("What is your name?\n")
        bid = float(input("What is your bid?\n"))  # Assume bid is numeric

        # Save data into the dictionary
        name_bid[name] = bid

        # Check if more bids need to be added
        more_bids = input("Are there any more bidders? y/n\n").lower()
        if more_bids != "y":
            break  # Exit the loop if no more bids

    # Find and print the highest bid
    max_key = key_with_max_value(name_bid)
    if max_key:
        print(f"{max_key} is the winner with a winning bid of ${name_bid[max_key]:.2f}")

# Start the bidding process
more_bids_needed()