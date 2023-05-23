import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da distribuição binomial
n = 20  # número de ensaios
p = 0.5  # probabilidade de sucesso

# Gerando 1000 amostras aleatórias
samples = np.random.binomial(n, p, size=1000)

# Plotando o histograma das amostras
plt.hist(samples, bins=range(n+2), density=True, alpha=0.7, color='skyblue', rwidth=0.8)

# Gerando os pontos para a curva de distribuição binomial teórica
x = np.arange(0, n+1)
y = np.random.binomial(n, p, size=len(x)) / float(n)

# Plotando a curva de distribuição binomial teórica
plt.plot(x, y, marker='o', color='red')

# Definindo os rótulos do gráfico
plt.xlabel('Número de Acertos')
plt.ylabel('Probabilidade')
plt.title('Distribuição Binomial')

# Exibindo o gráfico
plt.show()
