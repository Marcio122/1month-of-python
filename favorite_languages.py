# A dictionary of similar objects
favorite_languages = {
    'sarah' : 'python',
    'jess' : 'c',
    'carl' : 'javascript',
    'lina' : 'java',
    
    }
language = favorite_languages['sarah'].title()
print(f"Her favorite programming language is {language}")

#looping through all key-value pairs
for name, fav in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {fav.title()}")
    
# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())