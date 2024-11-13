def Soma1():
    n1 = int(input("por favor digite um numero: "))
    n2 = int(input("por favor digite um numero: "))
    resultado = n1+n2
    print(resultado)


def graus():
    graus_c = float(input("por favor digite a temperatura: "))
    fahrenheit = graus_c * 1.8 + 32
    print(graus_c)
    print(fahrenheit)



def par_impar():
    num = int(input("por favor digite um numero: "))
    if num % 2 == 0:
        print("é um numero par")
    else:
        print("é um numero impar")
        
    
def Inverter_string():
    string =  input("por favor digite uma palavra: ")
    string_invertida = string[::-1]
    print(string_invertida)
    

def Palidromo():
    string =  input("por favor digite uma palavra: ")
    string_invertida = string[::-1]
    if string == string_invertida:
        print("é um palidromo")
    else:
        print("não é um palidromo")
        

def media_aritmetica():
    lista_num = []
    for n in range(5):
        n=int(input("digite um valor"))
    lista_num.append(n)
    
    
    soma = 0
    for i in lista_num:
        soma+=i
    print("a media é: "+str(soma/len(lista_num)))
    
    
def Lista_par(lista_num):
    lista_num = []
    lista_num2 = []
    soma = 0
    for i in lista_num:
        soma+=i
    if soma % 2 == 0:
        lista_num2 = soma
        
        
