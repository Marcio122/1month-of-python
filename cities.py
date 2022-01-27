# Using break to exit a Loop
prompt = "\nPlease enter the name of a city you have visited"
prompt += "\nEnter quit to end the program "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to be in {city.title()} too")