number = int(input("Digite o número da sua conta bancária: "))

if number != 1212:
    print("Conta bancária inexistente!!")
else:
    oper = int(input("Tipo de operação a ser realizada: digite 1 para depósito ou 2 para retirada: "))
    if oper != 1 and oper != 2 in range(3):
        print("Digite apenas 1 OU 2. ") 
        print("Tente novamente!") 
    else: 
        saldo = float(2000)
        valor = float(input("Valor a ser depositado/retirado: "))
        if oper == 1:
            saldo = saldo + valor
            print("Valor depositado: ", valor)
            print("Valor na conta: ", saldo)
        else:
            if valor > saldo: 
                print("Você não possuí saldo suficiente!")
            else:
                saldo = saldo - valor
                print("Valor retirado: ", valor)
                print("Valor na conta: ", saldo)
                if saldo == 0:
                    print("Conta está zerada!")

