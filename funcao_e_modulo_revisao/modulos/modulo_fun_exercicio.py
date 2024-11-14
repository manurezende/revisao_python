def Soma1():
    '''essa funcao faz a soma de dois numeros'''
    n1 = int(input("por favor digite um numero: "))
    n2 = int(input("por favor digite um numero: "))
    resultado = n1+n2
    print(resultado)



def graus():
    '''essa função vai converter graus Celcius para fahrenheit'''
    graus_c = float(input("por favor digite a temperatura: "))
    fahrenheit = graus_c * 1.8 + 32
    print(graus_c)
    print(fahrenheit)




def par_impar():
    """essa função vai falar com o usuario se o numero digitado é par ou impar"""
    num = int(input("por favor digite um numero: "))
    if num % 2 == 0:
        print("é um numero par")
    else:
        print("é um numero impar")
        
        
        
    
def Inverter_string():
    '''essa função vai analizar a string digitada e ira invertela'''
    string =  input("por favor digite uma palavra: ")
    # No fatiamento de lista, geralmente há 3 fatores [x:y:z] x é o ponto inicial, y é o ponto final, z é o passo dado de x para y. 
    # Um passo regular será 1, que percorre a lista normalmente, mas quando é -1, a lista dá seu passo para trás,
    # resultando em uma lista invertida
    string_invertida = string[::-1]
    print(string_invertida)
    
    
    
    
def string_inverter_prof1(texto):
    tm = len(texto)
    print(texto)
    for i in range(tm-1,-1,-1):
        print(texto[i],end="")
        
        
        
def string_inverter_prof2(texto):
    
    tm = len(texto)
    # variavel q devolve texto invertido
    txt_invertido = ""
    for i in range(tm-1,-1,-1):
        txt_invertido += texto[i]
    return txt_invertido



def Palindromo():
    '''vai comparar se a string invertida é igual a string normal'''
    string =  input("por favor digite uma palavra: ")
    string_invertida = string[::-1]
    if string == string_invertida:
        print("é um palindromo")
        print(string,string_invertida)
    else:
        print("não é um palindromo")
        print(string,string_invertida)
        
        
        
        
def Palindromo_prof():
    '''vai comparar se a string invertida é igual a string normal'''
    string =  input("por favor digite uma palavra: ")
    if string == Inverter_string():
        print("é um palindromo")
    else:
        print("não é um palindromo")



def media_aritmetica():
    '''essa função analizara uma lista e ira tirar a media '''
    lista_num = []
    for n in range(5):
        n=int(input("digite um valor"))
    lista_num.append(n)
    
    soma = 0
    for i in lista_num:
        soma+=i
    print("a media é: "+str(soma/len(lista_num)))
    print(lista_num)
   
   
    
    
def Lista_par():
    '''essa função analizara uma lista e ira mostrar apenas os numeros pares '''
    
    lista_num = []
    
    for n in range(5):
        n=int(input("digite um valor"))
        lista_num.append(n)
    print(lista_num)
   
    lista_num2 = []

    soma = 0
    for i in lista_num:
        soma+=i  
        # vai calcular se é par ou impar
        if i % 2 == 0:
            lista_num2.append(i)
    print(lista_num2)
    
        
        
