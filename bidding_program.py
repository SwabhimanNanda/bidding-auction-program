# Importing necessary modules
from clear_console import clear_screen
from logo import logo

# Displaying the program's logo
print(logo)

# Dictionary to store bidders and their bid prizes
bidd = {}

# Flag to check if the bidding process is finished
bidding_finished = False

# Function to find the highest bid and the winner
def find_highest_bid(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Main bidding loop
while not bidding_finished:
    # Get bidder's name
    name = input("What is your name?: ")

    # Get bid prize from the bidder
    prize = int(input("What is your bid?: $"))

    # Add bidder and bid prize to the dictionary
    bidd[name] = prize

    # Ask if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    # Check if the bidding process is finished
    if should_continue == "no":
        bidding_finished = True
        # Call the function to find the highest bid and winner
        find_highest_bid(bidd)
    elif should_continue == "yes":
        # Clear the console for the next bidder
        clear_screen()

# End of the program



