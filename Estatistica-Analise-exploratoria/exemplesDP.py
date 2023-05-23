import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Parâmetro da distribuição de Poisson
lambda_ = 3  # taxa de ocorrência média

# Gerando 1000 amostras aleatórias
samples = np.random.poisson(lambda_, size=1000)

# Plotando o histograma das amostras
plt.hist(samples, bins=range(max(samples)+2), density=True, alpha=0.7, color='skyblue', rwidth=0.8)

# Gerando os pontos para a curva de distribuição de Poisson teórica
x = np.arange(0, max(samples)+1)
y = poisson.pmf(x, lambda_)

# Plotando a curva de distribuição de Poisson teórica
plt.plot(x, y, marker='o', color='red')

# Definindo os rótulos do gráfico
plt.xlabel('Número de Chamadas')
plt.ylabel('Probabilidade')
plt.title('Distribuição de Poisson')

# Exibindo o gráfico
plt.show()
