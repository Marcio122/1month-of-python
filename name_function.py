#testing a function
def get_formatted_name(first, last, middle = ''):
    fullname = f"{first} {middle} {last}"
    if middle:
        fullname = f"{first} {middle} {last}"
    else:
        fullname = f"{first} {last}"
    return fullname.title()
