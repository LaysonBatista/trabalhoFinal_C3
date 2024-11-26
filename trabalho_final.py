RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
GRAY = "\033[90m"
RESET = "\033[0m"

surfistas = []
bateria1 = []
bateria2 = []

ultimo_cadastro = 0

print("\nOlá, Seja Bem-vindo ao SurfEasy! Sistema de gerenciamento de Campeonatos de Surf.")
print("Por favor, Escolha Uma Das Opções Abaixo Para Seguir:")


def erro_tipo_dado():
    return print(f"{RED}Erro: Tipo de dado inválido. Tente novamente.{RESET}")

    
def criar_surfista():
    respota = ' '
    while respota != 'n':
        while True:
            try:
                nome = input("\nDigite o nome do surfista: ")
                if not nome.replace(" ", "").isalpha():
                    raise ValueError
                break
            except:
                erro_tipo_dado()

        surfistas.append([nome])
        print(f"\n{GREEN}Surfista \"{nome}\" cadastrado(a) com sucesso!{RESET}")

        respota = input("\nDeseja cadastrar mais um surfista? (s/n) ").lower()
        while respota != 's' and respota != 'n':
            erro_tipo_dado()
            respota = input("\nDeseja cadastrar mais um surfista? (s/n) ").lower()
            

def listar_surfistas():
    if not surfistas:
        return print(f"\n{RED}Nenhum surfista foi cadastrado para listar.{RESET}")
        
    print("\n====== Lista de Surfistas ======")
    for i , valor in enumerate(surfistas):
        print(f"{i+1}. {GRAY}{surfistas[i][0]} - Bateria 1: 1º Nota: {bateria1[i][1]} - 2º Nota: {bateria1[i][2]} | Bateria 2: 1º Nota: {bateria2[i][1]} - 2º Nota: {bateria2[i][2]}{RESET}")


def atualizar_surfistas():
    if not surfistas:
        return print(f'\n{RED}Nenhum surfista foi cadastrado para atualizar.{RESET}')

    print('--- Atualizar surfista ---')
    listar_surfistas()
    while True:
        try:
            busca = int(input('\nInforme a posição (número) do surfista que deseja atualizar a nota: ')) - 1
            if busca < 0 or busca >= len(surfistas):
                raise IndexError(f'Erro: Não existe surfista na posição {busca + 1}.')
            print(f'{BLUE}\nSurfista selecionado: {surfistas[busca][0]} - Notas: {bateria1[busca][1]}, {bateria1[busca][2]}{RESET}')
            atualizar_nota = int(input('Qual nota deseja atualizar?\nDigite (1) para 1ª nota\nDigite (2) para 2ª nota\nEscolha uma opção: '))
            if atualizar_nota not in [1, 2]:
                raise ValueError('Opção inválida. Escolha (1) ou (2).')
            nova_nota = float(input(f'Informe a nova nota {atualizar_nota}: '))
            bateria1[busca][atualizar_nota] = nova_nota
            print(f"\n{GREEN}Nota atualizada com sucesso!{RESET}")
            print(f"Novas notas do surfista \"{surfistas[busca][0]}\": {bateria1[busca][1]}, {bateria1[busca][2]}")
            return
        except ValueError as e:
            print(f"{RED}Erro: {e}{RESET}")
        except IndexError as e:
            print(f"{RED}Erro: {e}{RESET}")
        except Exception:
            print(f"{RED}Erro inesperado. Tente novamente.{RESET}")


def buscar_surfista():
    if not surfistas:
        print(f'\n{RED}Nenhum surfista foi cadastrado para buscar.{RESET}')
        return

    print('\n--- Buscar Surfista ---')
    nome_buscado = input("Digite o nome do surfista para buscar: ").strip().lower()

    surfistas_encontrados = [
        (i,surfista) for i, surfista in enumerate(surfistas) if surfista[0].strip().lower() == nome_buscado
    ]

    if surfistas_encontrados:
        print("\nSurfistas encontrados:")
        for i, surfista in surfistas_encontrados:
            try:
                # Verifica se há notas na bateria
                notas = bateria1[i]
                print(f"Nome: {surfista[0]}, 1ª Nota: {notas[1]}, 2ª Nota: {notas[2]}")
            except IndexError:
                # Caso não haja notas registradas
                print(f"Nome: {surfista[0]}, {RED}Notas não registradas.{RESET}")
    else:
        print(f"\n{RED}Nenhum surfista com o nome '{nome_buscado}' foi encontrado.{RESET}")




def menu():
    while True:
        print("\n=== Sistema SurfEasy ===")
        print("1. Gerenciar Surfistas")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            global ultimo_cadastro
            while True:
                print("\n--- Gerenciar Surfistas ---")
                print("1. Cadastrar Surfistas")
                print("2. Listar Surfistas")
                print("3. Atualizar Notas dos Surfistas")
                print("4. Buscar Surfistas")
                print("5. Voltar")
                sub_opcao = input("Escolha uma opção: ")

                if sub_opcao == "1":
                    criar_surfista()
                    print("\n> Agora informe as notas de cada surfista cadastrado:")
                    for i in range(ultimo_cadastro, len(surfistas)):
                        while True: 
                            try: 
                                print("\n--- Bateria 1 ---")
                                b1nota1 = float(input(f"Informe a 1º nota de \"{surfistas[i][0]}\": "))
                                b1nota2 = float(input(f"Informe a 2º nota de \"{surfistas[i][0]}\": "))
                                bateria1.append([i,b1nota1,b1nota2])
                                print("\n--- Bateria 2 ---")
                                b2nota1 = float(input(f"Informe a 1º nota de \"{surfistas[i][0]}\": "))
                                b2nota2 = float(input(f"Informe a 2º nota de \"{surfistas[i][0]}\": "))
                                bateria2.append([i,b2nota1,b2nota2])
                                break
                            except:
                                erro_tipo_dado()
                    ultimo_cadastro = len(surfistas)

                elif sub_opcao == "2":
                    listar_surfistas()
                elif sub_opcao == "3":
                    atualizar_surfistas()
                elif sub_opcao == "4":
                    buscar_surfista()                   
                elif sub_opcao == "5":
                    break
                else:
                    print(f"\n{RED}Opção inválida. Tente novamente{RESET}")
        elif opcao == "2":
            print("\nSaindo do sistema. Até logo!")
            print(f'{BLUE}Programa criado por: Layson Batista, Matheus Carvalho e Pedro Pelissari.{RESET}')
            break
        else:
            print(f"{RED}Opção inválida. Tente novamente.{RESET}")


menu()