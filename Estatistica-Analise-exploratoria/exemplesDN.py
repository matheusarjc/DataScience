import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da distribuição normal
mean = 0  # média
std = 1   # desvio padrão

# Gerando 1000 amostras aleatórias
samples = np.random.normal(mean, std, size=1000)

# Plotando o histograma das amostras
plt.hist(samples, bins=30, density=True, alpha=0.7, color='skyblue')

# Gerando os pontos para a curva de distribuição normal teórica
x = np.linspace(-4, 4, 100)
y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-(x - mean)**2 / (2 * std**2))

# Plotando a curva de distribuição normal teórica
plt.plot(x, y, color='red', linewidth=2)

# Definindo os rótulos do gráfico
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Distribuição Normal')

# Exibindo o gráfico
plt.show()
