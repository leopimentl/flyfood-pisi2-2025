def ler_matriz(caminho_arquivo):
    with open(caminho_arquivo) as c:
        linhas, colunas = [int(x) for x in c.readline().split()]
        pontos = {'R': None}
        for i in range(linhas):
            linha = c.readline().strip().split()
            for j in range(colunas):
                if linha[j] != '0':
                    pontos[linha[j]] = (i, j)
        return pontos

def calcula_distancia(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def gerar_permutacoes(itens):
    if len(itens) == 0:
        return []
    if len(itens) == 1:
        return [itens]
    
    permutacoes = []
    for i in range(len(itens)):
        elem = itens[i]
        resto = itens[:i] + itens[i+1:]
        for p in gerar_permutacoes(resto):
            permutacoes.append([elem] + p)
    
    return permutacoes

def encontrar_rota_otima(pontos):
    pontos_entrega = [p for p in pontos.keys() if p != 'R']
    origem = pontos['R']
    menor_distancia = float('inf')
    melhor_rota = None
    
    for permutacao in gerar_permutacoes(pontos_entrega):
        distancia_atual = 0
        posicao_atual = origem
        
        for ponto in permutacao:
            distancia_atual += calcula_distancia(posicao_atual, pontos[ponto])
            posicao_atual = pontos[ponto]

        distancia_atual += calcula_distancia(posicao_atual, origem)
        
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = permutacao
    
    return ' '.join(melhor_rota)

def main():
    caminho_arquivo = 'matriz.txt'
    pontos = ler_matriz(caminho_arquivo)
    rota_otima = encontrar_rota_otima(pontos)
    print(rota_otima)
    
if __name__ == "__main__":
    main()