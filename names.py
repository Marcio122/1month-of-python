from name_function import get_formatted_name
print("Enter q to quit the program")
while True:
    
    first = input("\nPlease tell your first name: ")
    
    if first == 'q':
    
        break
    
    last = input("\nPlease tell your last name: ")
    
    if last == 'q':
        
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")