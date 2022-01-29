with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#reading file
ficheiro = 'pi_digits.txt'

with open(ficheiro) as file_object:
    for line in file_object:
        print(line.rstrip())

#making a list of lines from a file
ficha = 'pi_digits.txt'

with open(ficha) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())