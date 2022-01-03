# Exercise 8-13

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('dimitris', 'ch',
                           location='greece',
                           field='mathematics',
                           height_cm=184,
                           weight_category='heavy')

print(my_profile)