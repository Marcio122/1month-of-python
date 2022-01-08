first_age = 100
if first_age <= 4:
    print("Your entrance is free")
elif first_age < 18:
    print("Your entrance costs: $25")
else:
    print("Your entrance costs: $40")

# another way
age = 12
if age < 4:
    price = 0

elif age < 18:
    price = 25

else:
    price = 40

print(f"Your admission cost is ${price}")
    
