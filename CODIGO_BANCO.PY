menu = """

[b] Depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "b":
        valor = float(input("informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"deposito:R$ {valor:.2f}\n"

        else:
            print("operação falhou!o valor enformado é inválido.")

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou! você não tem aldo suficiente.")
        
        elif excedeu_limite:
            print("operação falhou! o valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("operação falhou! Número máximo de saque excedido.")

        elif valor > 0:
            saldo -= valor 
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1     

        else:
            print("opração falhou! o valor informado é infalido.")

    elif opcao == "e":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao =="q":
        break

    else:
        print("operação inválida, por favor selecione novamente a operação desejada.")    
