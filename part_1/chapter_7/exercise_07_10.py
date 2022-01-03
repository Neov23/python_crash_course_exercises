# Exercise 7-10

# Create empty list. Later we will append dictionaries as elements in here
results = []

# Each loop creates a dictionary (name-place)
while True:
    name = input("What is your name?")
    dream_visit = input("If you could visit one place in the world, where "
                        "would you go? ")

    # Create dictionary with name-dream_visit inputs as key-value
    participant = {
        name: dream_visit
        }
    # Add dictionary to the list
    results.append(participant)

    # Ask the user if he is done
    while True:
        end = input("Are you done (yes/no)? ")
        
        # If user's answer isn't 'yes' or 'no', the "done" question repeats
        if end.lower() != 'yes' and end.lower() != 'no':
            print("Invalid answer. Try again")
            continue
        else:
            break
    
    # If user's answer is 'yes' or 'no', break or repeat the initial loop
    if end.lower() == 'yes':
        break
    elif end.lower() == 'no':
        continue

print("")

# Create a variable to use in the loop
loop = 0

# Display all info for each element (dictionary) of the list
for result in results:
    loop += 1
    for name, place in result.items():
        print(f"Participant {loop}: \n")
        print(f"Name: {name.title()}")
        print("Question: If you could visit one place in the world, where "
              "would you go?")
        print(f"Answer: {place.title()}\n\n")