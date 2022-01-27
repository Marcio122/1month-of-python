#work - Movie tickets
tickets = "\nTell me your age and I'll tell you, how much your ticket movie costs: "

while True:
    ticket = (int(input(tickets)))
    if ticket < 3:
        print(f"Your ticket costs $0.")
    
    elif ticket <= 12:
        print(f"Your ticket costs: $10.")
    
    else:
        print(f"Your ticket costs $15.")