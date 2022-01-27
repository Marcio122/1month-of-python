#prompt = input("\nTell me something and I will repeat it back to you: ")
#prompt += "\nEnter quit to end the program "
#message = ""
#while message != 'quit':
#   message = input(prompt)
#    print(message)
 

#another way of doing things--->flags
#prompt = input("\nTell me something and I will repeat it back to you: ")
#prompt += "\nEnter quit to end the program "
#active = True
#while active:
#    message = input(prompt)
#   if message == 'quit':
#      active = False
# else:
#    print(message)
        
# Trying to be perfect on flags
linha = "\nEscreva algo e eu irei repetir para você: "
linha += "\nUse quit para fechar o programa. "

activo = True
while activo:
    mensagem = input(linha)
    if mensagem == 'quit':
        activo = False
    else:
        print(mensagem)

