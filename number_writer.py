#Using json.dump()
import json

numbers = [2,4,5,3,8,9]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)