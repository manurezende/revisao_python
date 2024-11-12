salario = int(input("olá caro colaborador por favor digite o seu salario!!"))

if salario <= 280:
    aumento = salario * 0.2
    salario_novo = salario + aumento
    print("olá seu aumento foi de 20%, você recebeu um aumento de",aumento ,"e seu salario era de", salario ,"agora seu salario está em", salario_novo)


elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    salario_novo = salario + aumento
    print("olá seu aumento foi de 15%, você recebeu um aumento de",aumento ,"e seu salario era de", salario ,"agora seu salario está em", salario_novo)


elif salario > 700 and salario <= 1500:
    aumento = salario * 0.10
    salario_novo = salario + aumento
    print("olá seu aumento foi de 10%, você recebeu um aumento de",aumento ,"e seu salario era de", salario ,"agora seu salario está em", salario_novo)

else:
    aumento = salario * 0.05
    salario_novo = salario + aumento
    print("olá seu aumento foi de 5%, você recebeu um aumento de",aumento ,"e seu salario era de", salario ,"agora seu salario está em", salario_novo)