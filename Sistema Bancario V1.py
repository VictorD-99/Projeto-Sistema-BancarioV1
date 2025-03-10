Menu = '''

[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair 

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(Menu)

    if opcao == "D":
        entrada = float(input("Qual valor a ser depositado? :")) 
        saldo += entrada 
        extrato += f"Deposito: R${entrada:.2f}\n"
        print("Parabéns, o valor foi depositado em sua conta")

    elif opcao == "S":
        numero_saques += 1

        if numero_saques <= 3:
            print("Saque:")
            saque = float(input("Qual valor deseja sacar? : "))
            
            if saque > 500:
                print("Valor excede seu limite de 500")
                numero_saques -= 1
            else: 
                if saque > saldo:
                    print("Saldo insuficiente para saque")
                else:
                    saldo -= saque
                    print("Saque realizado com sucesso, seu novo saldo é: R$",saldo)
                    extrato += f"\nSaque: R${saque:.2f}"
        else:
            print("Você atingiu seu limite diario de saques, volte amanhã!")        

    elif opcao == "E": 
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao =="X":
        print("Obrigado por utilizar nosso banco! Volte sempre")
        break

    else: 
        print("Operação invalida, tente novamente")
