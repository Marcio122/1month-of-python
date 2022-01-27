# counting from 1 to 5
#current_number = 1
#while current_number <=5:
 #   print(current_number)
  #  current_number += 1
    

# Using continue in a Loop
#counting only odd numbers
#current_number = 0
#while current_number < 10:
 #   current_number += 1
  #  if current_number % 2 == 0:
   #     continue
   # print(current_number)
    
# Avoiding Infinite Loops
#x = 1
#while x < 5:
  #  print(x)
 #   x += 1
#this loop runs forever
#x = 1
#while x < 5:
  #  print(x)

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