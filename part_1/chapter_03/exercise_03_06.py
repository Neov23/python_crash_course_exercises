# Exercise 3-6

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