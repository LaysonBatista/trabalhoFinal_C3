RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
GRAY = "\033[90m"
YELLOW = "\033[33m"
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

    print('\n------ Atualizar Notas dos Surfistas ------')
    listar_surfistas()
    while True:
        try:
            busca = int(input('\nInforme a posição (número) do surfista que deseja atualizar a nota: ')) - 1
            if busca < 0 or busca >= len(surfistas):
                raise IndexError(f'Erro: Não existe surfista na posição {busca + 1}.')
            print(f'{BLUE}\nSurfista selecionado: {surfistas[busca][0]} - Bateria 1: 1º Nota: {bateria1[busca][1]} - 2º Nota: {bateria1[busca][2]} | Bateria 2: 1º Nota: {bateria2[busca][1]} - 2º Nota: {bateria2[busca][2]}{RESET}')

            bateria = int(input('\nInforme sobre qual bateria deseja atualizar a nota.\nDigite (1) para BATERIA 1.\nDigite (2) para BATERIA 2.\nInforme: '))

            if bateria == 1: 
                atualizar_nota = int(input('\nQual nota deseja atualizar?\nDigite (1) para 1ª nota\nDigite (2) para 2ª nota\nEscolha uma opção: '))
                if atualizar_nota not in [1, 2]:
                    raise ValueError('Opção inválida. Escolha (1) ou (2).')
                nova_nota = float(input(f'\nInforme a nova {atualizar_nota}º nota: '))
                bateria1[busca][atualizar_nota] = nova_nota
                print(f"\n{GREEN}Nota atualizada com sucesso!{RESET}")
                print(f"Novas notas do surfista \"{surfistas[busca][0]}\": Bateria 1: 1º Nota: {bateria1[busca][1]} - 2º Nota: {bateria1[busca][2]} | Bateria 2: 1º Nota: {bateria2[busca][1]} - 2º Nota: {bateria2[busca][2]}")
                return
            elif bateria == 2: 
                atualizar_nota = int(input('\nQual nota deseja atualizar?\nDigite (1) para 1ª nota\nDigite (2) para 2ª nota\nEscolha uma opção: '))
                if atualizar_nota not in [1, 2]:
                    raise ValueError('Opção inválida. Escolha (1) ou (2).')
                nova_nota = float(input(f'\nInforme a nova {atualizar_nota}º nota: '))
                bateria2[busca][atualizar_nota] = nova_nota
                print(f"\n{GREEN}Nota atualizada com sucesso!{RESET}")
                print(f"Novas notas do surfista \"{surfistas[busca][0]}\": Bateria 1: 1º Nota: {bateria1[busca][1]} - 2º Nota: {bateria1[busca][2]} | Bateria 2: 1º Nota: {bateria2[busca][1]} - 2º Nota: {bateria2[busca][2]}")
                return
            else:
                while bateria != 1 or bateria != 2:
                    print(f'\n{RED}Opção inválida. Escolha (1) ou (2).{RESET}')
                    bateria = int(input('\nInforme sobre qual bateria deseja atualizar a nota.\nDigite (1) para BATERIA 1.\nDigite (2) para BATERIA 2.\nInforme: '))
        except ValueError as e:
            erro_tipo_dado()
        except IndexError as e:
            print(f"\n{RED}Erro: {e}{RESET}")
        except Exception:
            print(f"\n{RED}Erro inesperado. Tente novamente.{RESET}")


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
        print(f"\n{BLUE}Surfistas encontrados:{RESET}")
        for i, surfista in surfistas_encontrados:
            try:
                notas = bateria1[i]
                print(f"{BLUE}Nome: {surfista[0]}, 1ª Nota: {notas[1]}, 2ª Nota: {notas[2]}{RESET}")
            except IndexError:
                print(f"Nome: {surfista[0]}, {RED}Notas não registradas.{RESET}")
    else:
        print(f"\n{RED}Nenhum surfista com o nome '{nome_buscado}' foi encontrado.{RESET}")


def cal_resultado():
    if not surfistas or len(bateria1) != len(surfistas) or len(bateria2) != len(surfistas):
        print(f'{RED}Erro: Certifique-se de que as listas de surfistas e notas estão completas e consistentes.{RESET}')
        return
    resultado = []
    for i in range(len(surfistas)):
        bateria1[i].pop(0) 
        bateria2[i].pop(0)
        nome = surfistas[i]
        soma_notas = sum(bateria1[i])+sum(bateria2[i])
        media = soma_notas/4 
        resultado.append([nome,media])
        resultado.sort(key=lambda x: x[1], reverse=True)
        bateria1[i].insert(0,0) 
        bateria2[i].insert(0,0)

    print(f'\n{YELLOW}=== RESULTADO FINAL ==={RESET}')
    for posicao, (nome, media) in enumerate(resultado[:3], start=1): 
        print(f"{posicao}º lugar: {GRAY}{nome}{RESET} com média {media:.2f}")
    print(f"{YELLOW}Parabéns aos vencedores!{RESET}")


def filtro():
    if not surfistas:
        print(f'\n{RED}Nenhum surfista foi cadastrado para filtrar.{RESET}')
        return
   
    notas_bateria1 = [nota for surfista in bateria1 for nota in surfista]
    notas_bateria2 = [nota for surfista in bateria2 for nota in surfista]

    maiorB1 = max(notas_bateria1)
    menorB1 = min(notas_bateria1)
    maiorB2 = max(notas_bateria2)
    menorB2 = min(notas_bateria2)

    while True:
        try:
            entrada = int(input('\nDeseja saber quais dados referente a competição?\nDigite (1) para Parcial das baterias. Digite (2) para o resultado do torneio: '))
            if entrada == 1:
                surch = int(input('\n--- PARCIAL ---\nPara vizualizar a parcial da BATERIA 1, digite(1)\nPara vizualizar a parcial da BATERIA 2, digite(2)\nInforme: '))
                if surch == 1:
                    print('\n== Parcial da 1ª BATERIA ==')
                    for i , valor in enumerate(surfistas): 
                        print(f"{i+1}. {GRAY}{surfistas[i][0]} - 1º nota: {bateria1[i][1]} - 2º nota: {bateria1[i][2]}{RESET}") 
                    print(f'Total de competidores: {len(surfistas)}')
                    print(f'Maior nota da bateria: {maiorB1}')
                    print(f'Menor nota da bateria: {menorB1}')
                elif surch == 2:
                    print('\n== Parcial da 2ª BATERIA ==')
                    for i , valor in enumerate(surfistas): 
                        print(f"{i+1}. {GRAY}{surfistas[i][0]} - 1º nota: {bateria2[i][1]} - 2º nota: {bateria2[i][2]}{RESET}")
                    print(f'Total de competidores: {len(surfistas)}')
                    print(f'Maior nota da bateria: {maiorB2}')
                    print(f'Menor nota da bateria: {menorB2}')
                else:
                    raise ValueError('Opção inválida. Escolha (1) ou (2).')
            elif entrada == 2:
                cal_resultado()
                break
            else:
                raise ValueError('Opção inválida. Escolha (1) ou (2).')             
        except ValueError as e:
            print(f"{RED}Erro: {e}{RESET}")


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
                print("5. Filtrar Surfistas")
                print("6. Voltar")
                sub_opcao = input("Escolha uma opção: ")

                if sub_opcao == "1":
                    criar_surfista()
                    print("\n> Agora informe as notas dos surfistas cadastrados para cada bateria:")
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
                                print(f"\n{GREEN}Notas de \"{surfistas[i][0]}\" Armazenadas com sucesso!{RESET}")
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
                    filtro()                 
                elif sub_opcao == "6":
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