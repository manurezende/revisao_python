idade = int(input("por favor digite a sua idade, te retornaremos se você pode votar!: "))
 
if idade < 18:
    if idade < 16:
        print("você é novo demais para poder votar!")
    else:
        print("você pode votar, mas não tem obrigação")
        
else:
    print("você tem a obrigação de votar! ")