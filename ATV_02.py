class Time:
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores
    
    def adiciona_jogador(self, nome, camisa):
        self.jogadores.append([nome, camisa])
    
    def imprime_jogadores(self):
        print(f"Jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            print(f"{jogador[1]} - {jogador[0]}")

# Menu para inserir informações
nome_time = input("Insira o nome do time: ")
jogadores = []
while True:
    nome_jogador = input("Insira o nome do jogador (ou 'fim' para encerrar): ")
    if nome_jogador == 'fim':
        break
    camisa_jogador = int(input("Insira o número da camisa: "))
    jogadores.append([nome_jogador, camisa_jogador])

# Cria um objeto da classe Time
time = Time(nome_time, jogadores)

# Menu de opções para o usuário
while True:
    print("Escolha uma opção:")
    print("1 - Adicionar jogador")
    print("2 - Imprimir jogadores")
    print("3 - Encerrar programa")
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        nome_jogador = input("Insira o nome do jogador: ")
        camisa_jogador = int(input("Insira o número da camisa: "))
        time.adiciona_jogador(nome_jogador, camisa_jogador)
    
    elif opcao == 2:
        time.imprime_jogadores()
    
    elif opcao == 3:
        print("Encerrando programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")