# Exercise 9-15

from random import choice

# Create list with all characters available to choose
lottery_characters = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')

def create_ticket():
    """Create a ticket with four random characters of lottery_characters"""
    ticket = []
    while len(ticket) < 4:
        character = choice(lottery_characters)

        # Prevent duplication in ticket
        if character not in ticket:
            ticket.append(character)
    return ticket

def check_ticket(ticket_1, ticket_2):
    """Check if all elements of ticket_1 are in ticket_2"""
    # If all items of ticket_1 are in ticket_2, return True, else return False
    for character in ticket_1:
        if character not in ticket_2:
            return False
    return True

winning_characters = []
my_ticket = []
ticket_number = 0

# Loop that ends only when my ticket wins
while True:
    winning_characters = create_ticket()
    my_ticket = create_ticket()
    ticket_number += 1

    # If my ticket is the winning ticket, break loop
    if check_ticket(winning_characters, my_ticket):
        break
        
# Display how many tickets i have created
print(f"I finally won, after {ticket_number} tries. \n")

# Display winning ticket
print("Here are today's winning numbers and/or letters:")
print(f"{winning_characters[0]}, {winning_characters[1]}, "
      f"{winning_characters[2]}, {winning_characters[3]}. \n")

# Display my ticket
print(f"My ticket:")
print(f"{my_ticket[0]}, {my_ticket[1]}, {my_ticket[2]}, {my_ticket[3]}.")