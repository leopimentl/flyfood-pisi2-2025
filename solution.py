import time


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

def precalcular_distancias(pontos):
    calc = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
    chaves = list(pontos)
    return {
        (a, b): calc(pontos[a], pontos[b])
        for i, a in enumerate(chaves)
        for b in chaves[i + 1:]
    }

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

def get_distancia(cache, ponto_x, ponto_y):
    return 0 if ponto_x == ponto_y else cache.get((ponto_x, ponto_y)) or cache.get((ponto_y, ponto_x))

def encontrar_rota_otima(pontos, cache_distancias):
    pontos_entrega = [p for p in pontos.keys() if p != 'R']
    origem = 'R'
    menor_distancia = float('inf')
    melhor_rota = None
    
    for permutacao in gerar_permutacoes(pontos_entrega):
        distancia_atual = 0
        ponto_atual = origem
        
        for ponto in permutacao:
            distancia_atual += get_distancia(cache_distancias, ponto_atual, ponto)
            ponto_atual = ponto

        distancia_atual += get_distancia(cache_distancias, ponto_atual, origem)
        
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = permutacao
    
    return ' '.join(melhor_rota)

def main():
    caminho_arquivo = 'matriz.txt'
    pontos = ler_matriz(caminho_arquivo)
    cache = precalcular_distancias(pontos)
    inicio = time.time()
    rota_otima = encontrar_rota_otima(pontos, cache)
    fim = time.time()

    print(rota_otima)
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")
    
if __name__ == "__main__":
    main()