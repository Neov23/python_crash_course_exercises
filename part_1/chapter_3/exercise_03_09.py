#Exercise 3-9, from exercise 3-7 (lines 59-60)

invites = ["giannis", "vasiliki", "maria", "michalis"]

# Display the first set of invitations
print(f"\nDear friend {invites[1].title()}, you're invited to dinner.")
print(f"Dear friend {invites[2].title()}, you're invited to dinner.")
print(f"Dear friend {invites[3].title()}, you're invited to dinner.\n")

# Guest who won't come to dinner
print(f"{invites[0].title()} won't be able to make it to the dinner.\n")

del invites[0]
invites.insert(0, "tasos")

# Display the second set of invitations
print(f"Dear friend {invites[0].title()}, you're invited to dinner.")
print(f"Dear friend {invites[1].title()}, you're invited to dinner.")
print(f"Dear friend {invites[2].title()}, you're invited to dinner.")
print(f"Dear friend {invites[3].title()}, you're invited to dinner.\n")

# Informing people that i found a bigger table for dinner
print("I have a big announcement to make! I found a bigger table!\n")

# Insert a guest in the beginning, in the middle and one in the end of the list
invites.insert(0, "Takis")
invites.insert(2, "Makis")
invites.append("Lakis")

# Display the third set of invitations
print(f"Dear friend {invites[0].title()}, you're invited to dinner.")
print(f"Dear friend {invites[1].title()}, you're invited to dinner.")
print(f"Dear friend {invites[2].title()}, you're invited to dinner.")
print(f"Dear friend {invites[3].title()}, you're invited to dinner.")
print(f"Dear friend {invites[4].title()}, you're invited to dinner.")
print(f"Dear friend {invites[5].title()}, you're invited to dinner.")
print(f"Dear friend {invites[6].title()}, you're invited to dinner.\n")

# Informing people that we have space only for two guests at last
print("New announcement. Unfortunately, we have space for only two guests.\n")

# Remove guests from list, until two names remain
# Each time a person is removed from list, print personal message apologizing
print(f"Sorry {invites[-1].title()}, you can't come to dinner.")
invites.pop()
print(f"Sorry {invites[-1].title()}, you can't come to dinner.")
invites.pop()
print(f"Sorry {invites[-1].title()}, you can't come to dinner.")
invites.pop()
print(f"Sorry {invites[-1].title()}, you can't come to dinner.")
invites.pop()
print(f"Sorry {invites[-1].title()}, you can't come to dinner.\n")
invites.pop()

# Invite to dinner the remaining people of the list
print(f"{invites[0].title()}, please come to dinner.")
print(f"{invites[1].title()}, please come to dinner.\n")

# Number of people i invited at last
print(f"Number of people invited: {len(invites)}\n")

# Delete the remaining people of the list and display the empty list
del(invites[1])
del(invites[0])
print("Invitation list:")
print(f"{invites} \n")