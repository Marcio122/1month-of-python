#A simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
#Accessing values
print(alien_0['points'])

#adding new key-pairs value
alien_1 = {'player': 'ronaldo', 'shirt': 7}
alien_1['laliga'] = 'barça'
del alien_1['player']
print(alien_1)
#starting an empty dictionary
alien_2 = {}
alien_2['car'] = 'lamborghini'
alien_2['country'] = 'usa'
print(alien_2)
#modifying values in a dictionary
alien_3 = {'color': 'white'}
print(f"This is a {alien_3['color']} color")
alien_3['color'] = 'yellow'
print(f"This color is now {alien_3['color']}")
