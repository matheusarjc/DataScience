# Estatística Inferencial 
<span> Estatística Inferencial é uma área da estatística que se concentra em fazer inferências e tirar conclusões sobre uma população 
com base em informações limitadas obtidas de uma amostra representativa dessa população. A Estatística Inferencial desempenha um papel fundamental na tomada de decisões baseada em dados, pois nos permite generalizar as conclusões obtidas a partir de uma amostra para toda a população.</span>

### Estatística Descritiva x Estatística Inferencial
<p>A principal diferença entre Estatística Descritiva e Estatística Inferencial é que a primeira está preocupada em resumir e descrever os dados observados, enquanto a segunda se preocupa em fazer inferências e tirar conclusões sobre a população com base nessas informações limitadas.</p>

## Distribuições de Probabilidade
### Distribuição Normal
A distribuição normal, também conhecida como curva em forma de sino, é amplamente utilizada em Estatística Inferencial. É caracterizada por sua forma simétrica e unimodal, com a média, o desvio padrão e a forma da curva normal completamente determinados.

Exemplo de aplicação: A altura das pessoas em uma população normalmente distribuída.

![distribuicaonormal.png](..%2Futilidades%2Fdistribuicaonormal.png)

O gráfico resultante mostrará o histograma das amostras aleatórias (barras) e a curva de distribuição normal teórica (linha vermelha). O eixo x representa os valores e o eixo y representa a densidade de probabilidade.

### Distribuição Binomial
A distribuição binomial modela experimentos que têm dois resultados possíveis: sucesso ou fracasso. Ela é caracterizada por dois parâmetros: o número de ensaios (n) e a probabilidade de sucesso (p).

Exemplo de aplicação: O número de acertos em um teste de múltipla escolha, onde cada pergunta tem apenas duas opções de resposta.

![distribuicaobinomial.png](..%2Futilidades%2Fdistribuicaobinomial.png)

O gráfico resultante mostrará o histograma das amostras aleatórias (barras) e a curva de distribuição binomial teórica (pontos). O eixo x representa o número de acertos e o eixo y representa a probabilidade.

### Distribuição de Poisson
A distribuição de Poisson é usada para modelar eventos raros que ocorrem em uma taxa constante. É caracterizada por um único parâmetro lambda (λ), que representa a taxa média de ocorrência do evento.

Exemplo de aplicação: O número de chamadas recebidas em uma central telefônica em um determinado intervalo de tempo.

![distribuicaodepoisson.png](..%2Futilidades%2Fdistribuicaodepoisson.png)

O gráfico resultante mostrará o histograma das amostras aleatórias (barras) e a curva de distribuição de Poisson teórica (pontos). O eixo x representa o número de chamadas e o eixo y representa a probabilidade.

## Testes de Hipóteses
Um teste de hipótese é uma ferramenta estatística que nos permite tomar decisões com base em dados amostrais.

### Etapas:
#### Formulação de Hipóteses
<p>No teste de hipótese, formulamos duas hipóteses: a hipótese nula (H0) e a hipótese alternativa (H1). A hipótese nula geralmente representa a ausência de um efeito ou diferença, enquanto a hipótese alternativa representa o efeito ou diferença que estamos interessados em provar.</p>

#### Seleção do Nível de Significância:
<p>O nível de significância (alfa) é a probabilidade de rejeitar a hipótese nula quando ela é verdadeira. Um nível de significância comum é 0,05, o que significa que estamos dispostos a cometer um erro de 5% ao rejeitar a hipótese nula.</p>

#### Cálculo do Valor-p:
<p>O valor-p é a probabilidade de observar os dados amostrais (ou algo mais extremo) sob a hipótese nula. Calculamos o valor-p com base na distribuição de probabilidade relevante para o teste estatístico em questão.</p>

#### Interpretação e Decisão Estatística:
<p>Com base no valor-p, comparamos com o nível de significância selecionado. Se o valor-p for menor do que o nível de significância, rejeitamos a hipótese nula em favor da hipótese alternativa. Caso contrário, não temos evidências suficientes para rejeitar a hipótese nula.</p>