def saudacao(nome):
    """
    a função exibe uma menssagem de recepção,ela pede um parametro(argumento)chamado nome
    você deve digitar um nome 
    """
    print(f"olá {nome}! seja bem vindo")
    
    
def Area_retangulo(base,altura):
    """
    essa função calcula a area do triangulo, ela pede dois parametros base e altura e faz a multiplicação deles
    """
    area = base * altura
    return area


def Potencia (base,expoente):
    '''essa função faz uma potencia pedindo dois argumentos a Base e a Altura'''
    resultado = base ** expoente
    return resultado

def Soma(*numeros):
    '''essa função vai somar ela adiciona 1 na variavel resultado'''
    resultado = 0
    for i in numeros:
        resultado+=i
    return resultado

def Soma2 (n1,n2):
    '''essa função faz uma soma entre dois resultados'''
    return n1 + n2