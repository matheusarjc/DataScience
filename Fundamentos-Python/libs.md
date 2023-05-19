# Bibliotecas úteis (Básico)
### NumPy
O NumPy é uma biblioteca fundamental para computação numérica em Python. Ele fornece suporte para arrays multidimensionais (chamados de ndarrays), 
além de funções matemáticas e operações de vetorização eficientes. O NumPy é amplamente utilizado em áreas como ciência de dados, computação científica e machine learning.

<p>O NumPy é frequentemente importado usando a convenção import numpy as np. Ele fornece a estrutura de dados ndarray, que é um array multidimensional homogêneo. Os arrays do NumPy são mais eficientes em termos de memória e desempenho em comparação com as listas do Python, especialmente para operações matemáticas.</p>

#### Criando arrays
    
    import numpy as np
    
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
Isso criará um array NumPy unidimensional com os valores [1, 2, 3, 4, 5].

<h5>Você também pode criar arrays com valores predefinidos, como arrays de zeros, uns ou valores aleatórios usando as funções np.zeros(), np.ones() e np.random.random(), respectivamente.</h5>

#### Operações com Arrays
    
    import numpy as np

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    
    soma = arr1 + arr2
    subtracao = arr1 - arr2
    multiplicacao = arr1 * arr2
    divisao = arr1 / arr2
    
    print(soma)
    print(subtracao)
    print(multiplicacao)
    print(divisao)


#### Indexação e Fatiamento
Você pode acessar elementos específicos de um array NumPy usando indexação e fatiamento, assim como em listas do Python. A indexação em arrays NumPy começa em 0.

    import numpy as np

    arr = np.array([1, 2, 3, 4, 5])
    print(arr[0])  # Acesso ao primeiro elemento
    print(arr[2:4])  # Fatiamento para obter elementos de índice 2 a 3


#### Funções e Operações NumPy
O NumPy oferece uma ampla gama de funções e operações úteis para trabalhar com arrays. Algumas dessas funções incluem np.sum(), np.mean(), np.max(), np.min(), np.argmax(), np.argmin(), entre outras. Essas funções permitem realizar cálculos estatísticos, encontrar valores máximos e mínimos, bem como seus índices correspondentes.


#### Broadcasting
O broadcasting é uma funcionalidade poderosa do NumPy que permite realizar operações entre arrays de diferentes formas, sem a necessidade de fazer cópias dos dados. O broadcasting é útil quando você deseja realizar operações entre arrays que podem ter formas diferentes, mas são compatíveis para operações aritméticas. Isso evita a necessidade de escrever loops explícitos.

##### Broadcasting com um escalar
Você pode realizar operações entre um array e um escalar. O valor escalar será expandido para corresponder à forma do array e, em seguida, a operação será executada.

    import numpy as np

    arr = np.array([1, 2, 3])
    scalar = 2
    
    result = arr * scalar
    print(result)
    # Saída [2, 4, 6]

##### Broadcasting com arrays de formas diferentes
Você também pode realizar operações entre arrays de formas diferentes, desde que as dimensões sejam compatíveis. As dimensões são consideradas compatíveis quando são iguais ou uma delas é 1.

    import numpy as np

    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([1, 2, 3])
    
    result = arr1 + arr2
    print(result)
    
    [[2 4 6]
    [5 7 9]]

##### Broadcasting com arrays de dimensões diferentes
O broadcasting também pode ser aplicado a arrays com dimensões diferentes. O NumPy expandirá automaticamente as dimensões menores para corresponder às dimensões maiores.
    
    import numpy as np

    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([1, 2])
    
    result = arr1 + arr2[:, np.newaxis]
    print(result)
    
    #Saida 
    [[2 3 4]
    [6 7 8]]




### Pandas
O Pandas é uma biblioteca de análise de dados em Python. Ela fornece estruturas de dados flexíveis, como Series e DataFrame, que permitem manipular e analisar dados de forma eficiente. 
O Pandas é amplamente usado em tarefas de limpeza, transformação, filtragem e análise de dados. Com o Pandas, você pode carregar dados de várias fontes, como arquivos CSV, Excel e SQL, em um DataFrame. 

O Pandas é frequentemente importado usando a convenção import pandas as pd. Ele fornece duas estruturas de dados principais: Series e DataFrame. Uma Series é uma estrutura de dados unidimensional que pode armazenar dados de tipos diferentes, semelhante a uma coluna em uma planilha. Um DataFrame é uma estrutura de dados bidimensional que pode armazenar dados de tipos diferentes em colunas, semelhante a uma planilha ou tabela de banco de dados.

#### Carregando dados
O Pandas permite carregar dados de várias fontes, como arquivos CSV, Excel, SQL, entre outros. Para carregar dados de um arquivo CSV, você pode usar a função pd.read_csv() e fornecer o caminho do arquivo como argumento. 

    import pandas as pd

    data = pd.read_csv('caminho/para/arquivo.csv')

#### Explorando dados
Com o Pandas, você pode realizar várias operações para explorar e entender seus dados. Algumas das operações mais comuns incluem:
<ul>
<li>Visualizando os primeiros registros do DataFrame: data.head()</li>
<li>Visualizando os últimos registros do DataFrame: data.tail()</li>
<li>Obtendo informações sobre o DataFrame: data.info()</li>
<li>Obtendo estatísticas resumidas do DataFrame: data.describe()</li>
<li>Acessando colunas específicas do DataFrame: data['coluna']</li>
<li>Filtrando registros com base em condições: data[data['coluna'] > valor]</li>
<li>Agrupando e agregando dados: data.groupby('coluna').agg()</li>
</ul>

#### Manipulação de Dados
O Pandas oferece uma ampla gama de funcionalidades para manipular dados, como:

<ul>
<li>Adicionar colunas ao DataFrame: data['nova_coluna'] = valores</li>
<li>Remover colunas do DataFrame: data.drop('coluna', axis=1)</li>
<li>Preencher valores ausentes: data.fillna(valor)</li>
<li>Ordenar o DataFrame com base em uma coluna: data.sort_values('coluna')</li>
<li>Combinar DataFrames: pd.concat([df1, df2]) ou df1.merge(df2, on='coluna')</li>
</ul>

#### Visualização de Dados
O Pandas também se integra bem com outras bibliotecas de visualização, como o Matplotlib. Você pode usar o Pandas para preparar os dados e, em seguida, criar gráficos e visualizações com o Matplotlib. Algumas das funções de visualização incluem data.plot(), data.hist(), data.boxplot(), entre outras.

### Matplotlib
O Matplotlib é uma biblioteca de visualização de dados em Python. Ele permite criar gráficos de alta qualidade, como gráficos de linhas, barras, dispersão, histogramas, entre outros. O Matplotlib é amplamente utilizado para visualizar dados e explorar padrões, tendências e relacionamentos nos dados.
