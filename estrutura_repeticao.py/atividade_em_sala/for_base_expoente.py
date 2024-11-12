bs = int(input("digite um valor para a base"))
ex = int(input("digite um valor para a expoente"))

n=bs
for i in range(0,ex-1):
    n = n * bs
    print(str(n))