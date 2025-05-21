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

    def calcular_distancia(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    pontos_entrega = [p for p in pontos.keys() if p != 'R']
    todos_pontos = pontos_entrega + ['R']
    cache_distancias = {}
    
    for i in range(len(todos_pontos)):
        for j in range(i+1, len(todos_pontos)):
            ponto_origem = todos_pontos[i]
            ponto_destino = todos_pontos[j]
            distancia = calcular_distancia(pontos[ponto_origem], pontos[ponto_destino])
            cache_distancias[(ponto_origem, ponto_destino)] = distancia

    return cache_distancias

def get_distancia(cache_distancias, ponto_origem, ponto_destino):
    if ponto_origem == ponto_destino:
        return 0
    distancia = cache_distancias.get((ponto_origem, ponto_destino))
    if distancia is None:
        distancia = cache_distancias.get((ponto_destino, ponto_origem))

    return distancia

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
    cache_distancias = precalcular_distancias(pontos)
    rota_otima = encontrar_rota_otima(pontos, cache_distancias)
    print(rota_otima)
    
if __name__ == "__main__":
    main()