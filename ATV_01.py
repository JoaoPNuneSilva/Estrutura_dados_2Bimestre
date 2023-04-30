nome = input("Insira seu nome: ")
numeroConta = int(input("Digite o número da sua conta: "))
saldo = 0
print("\nCONTA CORRENTE:")
print("Nome do Titular: ",nome)
print("Número de Conta Corrente: ",numeroConta)
print("Saldo atual: ",saldo)

class ContaCorrente:
    def __init__(self):
        self.saldo = 0

    def depositar(self):
        deposito = float(input("Digite o valor de depósito: "))
        print("Depósito de ",deposito," realizado com sucesso!")
        self.saldo += deposito

    def sacar(self):
        saque = float(input("Digite o valor de saque: "))
        if saque > self.saldo:
            print("Saldo insuficiente. Por favor, digite um valor de saque que seja condinzente com seu saldo: ",self.saldo)
        else:
            print("Saque de ",saque," realizado com sucesso!")
            self.saldo = self.saldo - saque

def menu():
    conta = ContaCorrente()
    while True:
        print("")
        print("O QUE DESEJA FAZER?")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Imprimir Saldo")
        print("4 - Encerrar sessão de acesso")
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            conta.depositar()
        elif opcao == 2:
            conta.sacar()
        elif opcao == 3:
            print ("Seu saldo atual: ",conta.saldo)
        elif opcao == 4:
            print("")
            print("Sessão encerrada.")
            print("Obrigado por utilizar nossos serviços!")
            break
        else:
            print("OPÁ! Opção inválida. Tente novamente.")

menu()