saldo = 0.00
limite = 500.00
extrato_depositos = ''
extrato_saques = ''

saques = 0

SAQUES_DIARIOS = 3
LIMITE_SAQUE = 500.00

MENU = """

Escolha a operação desejada:

[D]epósito
[S]aque
[E]xtrato
[T]erminar sessão

"""

print("------------------------------------------------------")
print("Bem vindo ao Seu Banco!")
print("------------------------------------------------------")

while True:
    print(MENU)
    escolha = input("> ")[0].lower()

    if escolha == 'd':
        print("Informe o valor que deseja depositar:")
        valor_deposito = float(input("> "))
        if valor_deposito < 0.01:
            print("Valor informado é inválido: utilize apenas valores positivos.")
        else:
            saldo += valor_deposito
            extrato_depositos += f"\nR$ {valor_deposito:.2f}"
            print("Depósito efetuado com sucesso.")

    elif escolha == 's':
        if saques >= SAQUES_DIARIOS:
            print("Você já ultrapassou o limite de saques diários hoje.")
        else:
            print("Informe o valor que deseja sacar:")
            valor_saque = float(input("> "))
            if valor_saque < 0.01:
                print("Valor informado é inválido.")
            elif valor_saque > 500.00:
                print("Valor limite para saques é de R$ 500.00.")
            elif saldo - valor_saque < 0.00:
                print("Você não possui saldo para efetuar um saque neste valor.")
            else:
                saldo -= valor_saque
                saques += 1
                extrato_saques += f"\nR$ {valor_saque:.2f}"
                print("Saque efetuado com sucesso.")

    elif escolha == 'e':
        if extrato_depositos == '' and extrato_saques == '':
            print("Não foram realizadas movimentações")
        else:
            print("------------------------------------------------------")
            print("Saques efetuados:")
            print(extrato_saques)
            print("------------------------------------------------------")
            print("Depósitos efetuados:")
            print(extrato_depositos)
            print("------------------------------------------------------")
            print(f"Saldo Atual: R$ {saldo:.2f}")
            print("------------------------------------------------------")

    elif escolha == 't':
        print("\nVolte sempre!")
        break
    else:
        print("\nEscolha uma das opções do menu.")





