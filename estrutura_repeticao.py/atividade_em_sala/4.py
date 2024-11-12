num = []
num1 = int(input ("digite um numero: "))

num2 = int(input ("digite um numero: "))

num3 = int(input ("digite um numero: "))

num.append(num1)
num.append(num2)
num.append(num3)

maior = num[0]
for n in num:
    if n > maior:
        maior = n
print("o maior é",maior)