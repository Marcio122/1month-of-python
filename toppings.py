requested_toppings = 'mushrooms'
if requested_toppings != 'anchovies':
    print("Hold the anchovies")
# multiple testing condition
requested_pizzas = ['mushrooms', 'extracheese']
if 'mushrooms' in requested_pizzas:
    print("Adding mushrooms")
if 'bread' in requested_pizzas:
    print("Adding bread")
if 'extracheese' in requested_pizzas:
    print("Adding extracheese")

print("\nFinished your pizza")

# checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extracheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry,we don't have green peppers")
    print(f"Adding your {requested_topping}")
print("\nFinished your pizza")

# multiple lists
availables = ['audi', 'bmw', 'toyota', 'ferrari', 'iphone', 'samsung']
requesteds = ['iphone', 'bmw', 'ferrari', 'nokia']

for requested in requesteds:
    if requested in availables:
        print(f"Yes, you're going to receive your {requested}")
    else:
        print(f"Sorry we don't have this product") 