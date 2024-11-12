num = []
for i in range(5):
    s=int(input("digite um valor: "))
    num.append(s)


maior = num[0]
for n in num:
    if n > maior:
        maior = n
print("o maior é",maior)