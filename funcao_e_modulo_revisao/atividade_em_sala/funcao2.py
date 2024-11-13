def soma (n1,n2):
    return n1 + n2

def produto (n1,n2):
    return n1 * n2

def restoDiv (n1,n2):
    return n1 % n2

def subtracao (n1,n2):
    return n1 - n2

def separarResultados(texto):
    print("------------------o resultado de"+texto+"------------------")
    
print("ola seja bem vindo ao rogramas de calculos")
separarResultados("Soma")
print("o resultado da soma entre 5 e 10 é "+str(soma(5,10)))

separarResultados("multiplicação")
print("o resultado do produto entre 5 e 10 é "+str(produto(5,10)))

separarResultados("resto da divisão")
print("o resultado do resto é entre 5 e 10 é "+str(restoDiv(5,10)))