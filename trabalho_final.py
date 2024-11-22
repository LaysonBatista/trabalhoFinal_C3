#Cores de aviso, para tratar exceções (usado para destacar e diferenciar um "erro" de "sucesso").
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

print("\nOlá, Seja Bem-vindo ao SurfEasy! Sistema de gerenciamento de Compeonatos de Surf.")
print("Por favor, Escolha Uma Das Opções Abaixo Para Seguir:")

surfistas = []
bateria1 = []
bateria2 = []

def erro_tipo_dado():
    return print(f"{RED}Erro: Tipo de dado inválido. Tente novamente.{RESET}")
    
def criar_surfista():
    respota = ' '
    while respota != 'n':
        while True:
            try:
                nome = input("\nDigite o nome do surfista: ")
                # Validar se o nome contém apenas letras e espaços
                if not nome.replace(" ", "").isalpha():
                    raise ValueError  # Levantar exceção manualmente
                break  # Sair do loop se o nome for válido
            except:
                erro_tipo_dado()

        while True:
            try:
                pais = input("Digite o país do surfista: ")
                # Validar se o nome contém apenas letras e espaços
                if not pais.replace(" ", "").isalpha():
                    raise ValueError  # Levantar exceção manualmente
                break  # Sair do loop se o nome for válido
            except:
                erro_tipo_dado()

        surfistas.append([nome, pais])
        print(f"\n{GREEN}Surfista \"{nome}\" cadastrado(a) com sucesso!{RESET}")

        while True:
            respota = input("\nDeseja cadastrar mais um surfista? (s/n) ").lower()
            if respota == 's':
                break
            elif respota == 'n':
                break
            else:
                erro_tipo_dado()
        

def listar_surfistas():
    if not surfistas:
        return print(f"\n{RED}Nenhum surfista cadastrado.{RESET}")
        
    print("\n=== Lista de Surfistas ===")
    for i, valor in enumerate(surfistas):
        print(f"{i+1}. {surfistas[i][0]} - {surfistas[i][1]} - 1º nota: {bateria1[i][1]} - 2º nota: {bateria1[i][2]}")


def menu():
    while True:
        print("\n=== Sistema SurfEasy ===")
        print("1. Gerenciar Surfistas")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("\n--- Gerenciar Surfistas ---")
                print("1. Cadastrar Surfista")
                print("2. Listar Surfistas")
                print("3. Atualizar Surfista")
                print("4. Voltar")
                sub_opcao = input("Escolha uma opção: ")

                if sub_opcao == "1":
                    criar_surfista()
                    for i, valor in enumerate(surfistas):
                        try: 
                            nota1 = float(input(f"\nInforme a 1º nota de \"{surfistas[i][0]}\": "))
                            nota2 = float(input(f"informe a 2º nota de \"{surfistas[i][0]}\": "))
                        except:
                            erro_tipo_dado()
                        bateria1.append([i,nota1,nota2])
                elif sub_opcao == "2":
                    listar_surfistas()
                elif sub_opcao == "3":
                    atualizar_surfista() #Fazer update de surfistas  
                elif sub_opcao == "4":
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "2":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print(f"{RED}Opção inválida. Tente novamente.{RESET}")

# Executar o menu
menu()

