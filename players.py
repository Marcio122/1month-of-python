#slicing
players = ['ronaldo', 'messi', 'neymar', 'benzema', 'rooney', 'marcelo', 'dimaria']
print(players[0:3])
# Looping through a slice
players = ['ronaldo', 'messi', 'neymar', 'benzema', 'rooney', 'marcelo', 'dimaria']
print(f"My first three players are:")
for player in players[0:3]:
    print(player.title())

#copying a list
my_foods = ['rice', 'beacon', 'meat', 'fish','vegetables']
myfriend_food = my_foods[:]
my_foods.append('icecream')
myfriend_food.append('fruits')
print(f"My favorite foods are:")
print(my_foods)
print(f"\nMy friend's favorite food are: ")
print(myfriend_food)