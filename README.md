# SurfEasy - Sistema de Gerenciamento de Campeonatos de Surf

**SurfEasy** é um sistema desenvolvido para gerenciar campeonatos de surf, permitindo o cadastro, listagem, atualização, busca de surfistas e filtragem dos melhores 3 surfistas e dos resultados parciais.

## Funcionalidades Principais

- **Cadastrar Surfistas**: Permite adicionar novos surfistas ao sistema.
- **Listar Surfistas**: Exibe a lista de surfistas cadastrados, incluindo suas notas.
- **Atualizar Notas**: Permite modificar as notas de surfistas existentes.
- **Buscar Surfistas**: Realiza a busca de surfistas pelo nome.
- **Filtrar**: REaliza filtro dos 3 melhores surfista com as melhores notas.

## Pré-requisitos

- Python 3.x instalado.
- Console ou terminal para execução do programa.

## Passo a Passo do Uso

### Menu Principal

Ao iniciar o sistema, você verá o seguinte menu:

=== Sistema SurfEasy ===
1. Gerenciar Surfistas
2. Sair <br/>
Escolha uma opção:

Digite o número correspodente à opção desejada e pressione **Enter**.

### Gerenciar Surfistas

Dentro do menu de gerenciamento, as opções disponíveis são:

1. Cadastrar Surfistas: Adiciona novos surfistas e solicita as notas para cada um.
2. Listar Surfistas: Exibe todos os surfistas cadastrados e suas respectivas notas.
3. Atualizar Notas dos Surfistas: Permite alterar as notas já cadastradas.
4. Buscar Surfistas: Realiza uma busca pelo nome do surfista.
5. Filtrar surfistas: Realiza uma filtragem com as notas dos surfistas.
6. Voltar: Retorna ao menu principal.

### Exemplo de Uso

Cadastrar um Surfista
- Escolha a opção 1 no menu de gerenciamento.
- Digite o nome do surfista e confirme.
- Informe as notas quando solicitado. <br/>

Listar surfistas
- Escolha a opção 2 no menu de gerenciamento.
- Será exibido uma lista de todos os surfistas cadastrados no sistema. <br/>

Atualizar Notas dos Surfistas
- Escolha a opção 3 no menu de gerenciamento.
- Informe a "número" / "posição" do surfista segundo a lista.
- Escolha sobre qual bateria (1 ou 2) deseja fazer a atualização das notas.
- Informe sobre qual nota (1 ou 2) deseja fazer a atualização da nota em especifico. <br/>

Buscar um Surfista
- Escolha a opção 4 no menu de gerenciamento.
- Digite o nome do surfista e o sistema exibirá as informações, se encontradas. <br/>

Filtar surfistas
- Escolha a opção 5 no menu de gerenciamento.
- Digite 1 para filtrar a parcial das baterias ou 2 para saber o resultado final.
- Se a opção escolhida for 1, informe qual parcial da bateria deseja ver (bateria 1 ou bateria 2).

Mensagens de Erro
- Erro: Tipo de dado inválido. Tente novamente.: Ocorre ao inserir dados incorretos, como números em vez de letras no nome.
- Erro inesperado. Tente novamente.: Mensagem genérica para caso ocorra erros não tratados.

### Autores
- Layson Batista
- Matheus Carvalho
- Pedro Pelissari
