from matplotlib import pyplot as plt

def plotar_rota(pontos, rota_str):
    coords = [pontos['R']] + [pontos[letra] for letra in rota_str.split()] + [pontos['R']]
    fig, ax = plt.subplots()

    linhas = max(coord[0] for coord in pontos.values()) + 1
    colunas = max(coord[1] for coord in pontos.values()) + 1
    for i in range(linhas):
        ax.axhline(i, color='lightgray', linewidth=0.5)
    for j in range(colunas):
        ax.axvline(j, color='lightgray', linewidth=0.5)
 
    for label, (x, y) in pontos.items():
        ax.plot(y + 0.5, linhas - x - 0.5, 'o', markersize=10)
        ax.text(y + 0.5, linhas - x - 0.5, label, ha='center', va='center', color='white', bbox=dict(facecolor='black', boxstyle='circle'))

    for i in range(len(coords) - 1):
        x1, y1 = coords[i]
        x2, y2 = coords[i + 1]
        
        path = [
            (y1 + 0.5, linhas - x1 - 0.5),
            (y2 + 0.5, linhas - x1 - 0.5),
            (y2 + 0.5, linhas - x2 - 0.5)
        ]
        ax.plot(*zip(*path), color='blue')

    ax.set_aspect('equal')
    ax.set_xticks(range(colunas))
    ax.set_yticks(range(linhas))
    ax.set_xlim(0, colunas)
    ax.set_ylim(0, linhas)
    ax.invert_yaxis()
    plt.grid(True)
    plt.show()

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
    caminho_arquivo = 'matriz10x10_10p.txt'
    pontos = ler_matriz(caminho_arquivo)
    cache = precalcular_distancias(pontos)
    rota_otima = encontrar_rota_otima(pontos, cache)
    print(rota_otima)
    plotar_rota(pontos, rota_otima)

if __name__ == "__main__":
    main()