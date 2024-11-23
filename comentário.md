Na linha 90 caso não haja surfistas na lista [], a função exibe uma mensagem de erro e retorna imediatamente, encerrando a execução.
Na linha 92  função listar_surfistas() é chamada para exibir os surfistas já cadastrados, ajudando ao usuário identificar.
na linha 96 ao entrar no try, o programa solicita ao usuário para informar o nome do surfista ou a posição dele no código
Na linha 97 o 'if busca.isdigit():' garante que a busca seja realizada pelo indice do surfista. Já o 'Else' realiza a busca pelo nome do atleta.
Na linha 107 o (if indice == -1:) garante que caso o surfista não seja encontrato o programa vai informar ao usuário. Criando o IndexErro que será tratado.
Na linha 109 o surfista selecionado é mostrado, junto as suas atuais notas. Depois disso o programa 

na linha 109 print(f'\nSurfista selecionado{surfistas[indice][0]} - Notas{bateria1[indice][1]}, {bateria1[indice][2]}')
Exibe o nome e as notas atuais do surfista selecionado.

na linha 110 atualizar_nota = int(input('Qual nota deseja atualizar?\nDigite (1) para 1ª nota\nDigite (2) para 2ª nota:'))
Solicita ao usuário que escolha qual nota (1ª ou 2ª) deseja atualizar.

linha 111 if atualizar_nota not in [1, 2]:
Verifica se a escolha de nota não é válida (diferente de 1 ou 2).

linha 111 raise ValueError
Caso a escolha de nota seja inválida, lança uma exceção ValueError.

linha 113 nova_nota = float(input(f'Informe a nova nota {atualizar_nota}: '))
Solicita ao usuário a nova nota para atualizar.

linha 114 bateria1[indice][atualizar_nota] = nova_nota
Atualiza a nota na lista bateria1 no índice correspondente.

linha 115 print(f"\n{GREEN}Nota atualizada com sucesso!{RESET}")
Exibe uma mensagem de sucesso após a atualização da nota.

linha 116 print(f"Novas notas do surfista {surfistas[indice][0]}: {bateria1[indice][1]}, {bateria1[indice][2]}")
Exibe as novas notas do surfista após a atualização.

linha 117 break
Interrompe o loop infinito, pois a atualização foi concluída.

linha 118 except ValueError:
Captura e trata erros de tipo de dado, como entrada inválida.

linha 119 erro_tipo_dado()
Chama uma função chamada erro_tipo_dado, provavelmente para exibir uma mensagem de erro ao usuário.

linha 120 except IndexError:
Captura e trata erros de índice fora do intervalo.

linha 121 print(f"{RED}Erro: Posição fora do intervalo. Tente novamente.{RESET}")
Exibe uma mensagem de erro quando o índice fornecido está fora do intervalo válido.

linha 122 except StopIteration:
Captura a exceção StopIteration, que pode ocorrer se o nome do surfista não for encontrado.

linha 123 print(f"{RED}Erro: Nome do surfista não encontrado. Tente novamente.{RESET}")
Exibe uma mensagem de erro caso o nome do surfista não seja encontrado.