numeros = []

for n in range(5):
    n=int(input("digite um valor"))
    numeros.append(n)


soma = 0
for i in numeros:
    soma+=i
    
print("a soma dos valores é: "+str(soma))
print("a media de valores é>: "+str(soma/len(numeros)))