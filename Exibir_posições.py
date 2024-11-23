#Busca vencedores
def vencedores():
    if not bateria:
        return print(f"{RED}Nenhuma nota foi cadastrada. Não é possível determinar os vencedores.{RESET}")
    resultado = [(surfistas[i][0], sum(bateria[i][1:])) for i in range(len(surfistas))]
    for i in range(len(resultado)):
        for s in range(0, len(resultado) - i - 1):
            if resultado[s][1] < resultado[s + 1][1]:
                resultado[s], resultado[s + 1] = resultado[s + 1], resultado[s]
    print('\n---- TOP 3 ----')
    for posicao, (nome, pontuacao) in enumerate(resultado[:3], start=1):
        print(f"{posicao}º lugar: {nome} com {pontuacao:.2f} pontos") 