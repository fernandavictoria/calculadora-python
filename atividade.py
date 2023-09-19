print("MENU")
print("escolha uma opcao da calculadora")
print("1.soma")
print("2.subtracao")
print("3.divisao")
print("4.multiplicacao")
opcao = int(input())
n1 = float(input())
n2 = float(input())

if opcao ==1:
    print(n1+n2)
elif opcao ==2:
    print(n1-n2)
elif opcao ==3:
    print(n1/n2)
elif opcao ==4:
    print(n1*n2)
