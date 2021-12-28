#Άσκηση 6-8

pets = {
    'dog': {
        'owner': 'michael'
        },

    'cat': {
        'owner': 'jimmy'
        },

    'rabbit': {
        'owner': 'thomas'
        }
    }

for species, info in pets.items():
    owner = info['owner'].title()
    print(f"{owner} owns a {species} as his pet.")
    
# Αυτή η άσκηση με δυσκόλεψε, χρειάστηκα αρκετά πειράματα
# Επίσης χρειάστηκε πολλή αναζήτηση, γιατί δεν σκέφτηκα αμέσως τον τρόπο
# Άρα την έλυσα με την βοήθεια σημειώσεων
