import matplotlib.pyplot as plt
import pandas as pd

dados = {
    'Pontos de Entrega': [4, 5, 6, 7, 8, 9, 10, 11],
    'Tempo (s)': [0.000078, 0.000275, 0.002560, 0.013510, 0.132191, 1.446592, 19.514644, 952.287879]
}

df = pd.DataFrame(dados)

plt.figure(figsize=(10, 6))
plt.plot(df['Pontos de Entrega'], df['Tempo (s)'], marker='o', linestyle='-', color='blue')
plt.title('Tempo de execução x Número de Pontos de Entrega')
plt.xlabel('Pontos de Entrega')
plt.ylabel('Tempo (segundos)')
plt.grid(True)
plt.xticks(df['Pontos de Entrega'])
plt.tight_layout()
plt.show()
