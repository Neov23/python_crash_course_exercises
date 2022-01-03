# Exercise 3-5

invites = ["giannis", "vasiliki", "maria", "michalis"]

# First set of invitations
print(f"\nDear friend {invites[1].title()}, You're invited to dinner.")
print(f"Dear friend {invites[3].title()}, You're invited to dinner.")
print(f"Dear friend {invites[2].title()}, You're invited to dinner.\n")

# Guest who won't come to dinner
print(f"{invites[0].title()} won't be able to make it to the dinner.\n")

del invites[0]
invites.insert(0, "tasos")

# Second set of invitations
print(f"Dear friend {invites[0].title()}, you're invited to dinner.")
print(f"Dear friend {invites[1].title()}, you're invited to dinner.")
print(f"Dear friend {invites[2].title()}, you're invited to dinner.")
print(f"Dear friend {invites[3].title()}, you're invited to dinner.\n")