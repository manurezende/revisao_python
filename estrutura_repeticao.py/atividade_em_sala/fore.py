
vogal = ["a","e","i","o","u"]
letra = input("digite uma letra: ")
letra = letra.lower() 
for vogais in vogal:
    if letra == vogais:
        print("é uma vogal")
        break
    else:
        print("é uma consoante")