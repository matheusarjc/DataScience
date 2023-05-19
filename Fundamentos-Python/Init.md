# FUNDAMENTOS PYTHON

## Variáveis e tipos de dados:
### Variáveis
Armazenamento nomeado.

    nome = "Matheus"

Possuem alguns tipos de dados embutidos como:
<ul>
<li>Números (Retorna números)</li>
<li>Strings (Retorna sequência de caracteres)</li>
<li>Boolean (Retorna verdadeiro ou falso)</li>
</ul>

Para verificar, use "type":

    idade = 25
    print(type(idade)) #Saída: <class 'int'>

#### Multidados
• Em Python, você pode atribuir valores a várias variáveis em uma única linha, separando-os por vírgulas.

    nome, idade, cidade = "João", 25, "São Paulo"
• Python também permite atribuir o mesmo valor a várias variáveis em uma única linha:

    x = y = z = 10
• Também, você pode atualizar o valor de uma variável utilizando o seu valor atual. Por exemplo:

    x = 5
    x = x + 1
    print(x)  # Saída: 6
• Python também oferece operadores de atribuição abreviados para atualizar uma variável com base em sua própria valor. Por exemplo:

    x = 5
    x += 1  # Equivalente a x = x + 1
    print(x)  # Saída: 6


### Estrutura de dados compostos
Permitem armazenar coleções de valores relacionados.
####  Listas
As listas são coleções ordenadas e mutáveis de itens. Você pode criar uma lista colocando os itens entre colchetes e 
separando-os por vírgulas.

cores = ["vermelho", "verde", "azul"]

#### Tuplas
São semelhantes às listas, mas são imutáveis, ou seja, seus elementos não podem ser alterados após a criação. São definidas
usando parenteses.

ponto = (2, 3)

#### Dicionários
São coleções de pares de chave-valor, onde cada valor é associado a uma chave única. Os dicionários são definidos usando
chaves e pares de chave-valor separados por dois-pontos.

aluno = {"nome": "Maria", "idade": 20, "curso": "Engenharia"}

### Operações e Expressões
#### Operações Matemáticas
x = 5
y = 3

soma = x + y
print(soma)  # Saída: 8

multiplicação = x * y
print(multiplicação)  # Saída: 15

exponencia = x ** y
print(resultado)  # Saída: 125

divisao_inteira = x // y
print(divisao_inteira)  # Saída: 1

divisão = x / y
print(divisão)  # Saída: 1.6666666666666667

resto = x % y
print(resto)  # Saída: 2

!!Observação: O Python permite reatribuir valores a uma variável existente. 
idade = 25
print(idade)  # Saída: 25

idade = 30
print(idade)  # Saída: 30

Uma prática comum ao trabalhar com variáveis é atribuir nomes descritivos que reflitam o seu propósito. 
Isso torna o código mais legível e compreensível. Por exemplo:

largura_retangulo = 10
altura_retangulo = 5

area_retangulo = largura_retangulo * altura_retangulo
print(area_retangulo)  # Saída: 50

!!Além disso, ao nomear variáveis em Python, é recomendado seguir as convenções de estilo PEP 8, 
que sugerem o uso de letras minúsculas e underscores para separar palavras em nomes compostos. Por exemplo:
"idade_aluno", "nome_usuario".

#### Operadores
Operadores de Comparação:
<ul>
<li>"==" (igual a): verifica se dois valores são iguais.</li>
<li>"!=" (diferente de): verifica se dois valores são diferentes.</li>
<li>">" (maior que): verifica se o valor à esquerda é maior que o valor à direita.</li>
<li>"<" (menor que): verifica se o valor à esquerda é menor que o valor à direita.</li>
<li>">=" (maior ou igual a): verifica se o valor à esquerda é maior ou igual ao valor à direita. </li>
<li>"<=" (menor ou igual a): verifica se o valor à esquerda é menor ou igual ao valor à direita. </li>
</ul>

## Estruturas de Controle em Python
As estruturas de controle permitem que você controle o fluxo de execução do seu programa com base em condições ou repetições. 

### if & else
A estrutura if-else permite que você execute um bloco de código se uma condição for verdadeira e execute um bloco 
diferente se a condição for falsa. A sintaxe básica é a seguinte:

    if condição:
        # código a ser executado se a condição for verdadeira
    else:
        # código a ser executado se a condição for falsa

Exemplo: 
    idade = 18

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

#### elif 
Além do if e do else, você também pode usar a cláusula elif (abreviação de "else if") para testar condições adicionais.
    
    if condição1:
        # código a ser executado se a condição1 for verdadeira
    elif condição2:
        # código a ser executado se a condição2 for verdadeira
    else:
        # código a ser executado se todas as condições anteriores forem falsas

Exemplo:

    nota = 85
    if nota >= 90:
        print("Nota: A")
    elif nota >= 80:
        print("Nota: B")
    elif nota >= 70:
        print("Nota: C")
    else:
        print("Nota: D")

### Loops
#### for
O loop for é usado para iterar sobre uma sequência (como uma lista, uma string, um dicionário, etc.) ou um objeto iterável.
A sintaxe básica é a seguinte:

    for elemento in sequência:
        # código a ser executado para cada elemento

Exemplo:

    frutas = ["maçã", "banana", "laranja"]
    for fruta in frutas:
        print(fruta)

Nesse exemplo, o loop for percorre a lista frutas e imprime cada elemento (fruta) em uma linha separada.
!!Observação: você pode utilizar a cláusula else em conjunto com os loops for e while. O bloco de código dentro do else 
será executado somente se o loop for concluído sem ter sido interrompido por um comando break. Por exemplo:
    
    for i in range(5):
        print(i)
    else:
        print("Loop concluído.")


#### while
O loop while é usado para repetir a execução de um bloco de código enquanto uma condição for verdadeira. 
A sintaxe básica é a seguinte:

    while condição:
    # código a ser executado enquanto a condição for verdadeira

Exemplo:
    
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1

#### break
O comando break interrompe a execução do loop atual e sai do loop por completo. Por exemplo:

    for i in range(1, 6):
    if i == 3:
        break
    print(i)

#### continue
O comando continue interrompe a execução da iteração atual do loop e passa para a próxima iteração. Por exemplo:

    for i in range(1, 6):
    if i == 3:
        continue
    print(i)


### try-except
Exceções são erros que ocorrem durante a execução do programa. Você pode lidar com exceções utilizando a estrutura 
try-except. O código que pode gerar uma exceção é colocado dentro do bloco try, e o tratamento da exceção é realizado no 
bloco except. Por exemplo:

    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("Erro: divisão por zero.")

!!Observação: Nesse exemplo, o código tenta realizar uma divisão por zero, o que resulta em uma exceção ZeroDivisionError. 
O bloco except captura essa exceção e imprime a mensagem "Erro: divisão por zero.".
