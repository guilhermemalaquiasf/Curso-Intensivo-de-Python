# ANOTAÇÕES - CURSO INTENSIVO DE PYTHON

Anotações e resolução dos exercícios do livro Curso Intensivo de Python, do Eric Matthes.

## CAP 2 - VARIÁVEIS E TIPOS DE DADOS SIMPLES

### STRINGS

- texto.title(): Somente primeiras letras maiúsculas, resto minúsculas.
- texto.upper(): Tudo maiúsculo.
- texto.lower(): Tudo minúsculo.
- f"{texto1} {texto2}": f-strings, junta strings e strings de variáveis.
- texto.rstrip(): Retorna string sem espaço a direita.
- texto.lstrip(): Retorna string sem espaço à esquerda.
- texto.strip(): Retorna string sem espaço de ambos os lados.
- texto.removeprefix('prefixo'): Retorna string sem um prefixo (no início).
- texto.removesuffix('sufixo'): Retorna string sem um sufixo (no fim).

## CAP 3 - TRABALHANDO COM LISTAS

### Listas

**Inserção e remoção**

- lista.append(valor): Adiciona um valor no fim da lista.
- lista.insert(posição, valor): Insere um novo elemento em qualquer posição.
- del lista[posição]: remove o elemento da posição definida.
- lista.pop(): Remove o último elemento e retorna o seu valor. 
    - Também é possível remover qualquer posição com lista.pop(posição).
- lista.remove(valor): Remove da lista o elemento com o valor especificado.

**Ordenação**

- lista.sort(): Ordena a lista por ordem alfabética (tabela Unicode). 
    - lista.sort(reverse=True) ordena ao contrário.
- sorted(lista): Retorna uma lista ordenada alfabeticamente (tabela Unicode), sem alterar a original.
    - sorted(lista, reverse=True) ordena ao contrário.
- lista.reverse(): Inverte a ordem da lista.
- len(lista): Retorna tamanho da lista.

## CAP 4 - TRABALHANDO COM LISTAS

**for**

```python
gatos = ['Preto', 'Nina', 'Bolão']
for gato in gatos:
    print(gato)
```

**Métodos**

- range(a,b): Gera uma série de números, de a até b - 1.
    - range(a, b, c): Gera uma série de números de a até b - 1, de c em c.
- list(a) : Converte a para uma lista.
- min(digitos): Retorna o menor número de uma lista.
- max(digitos): Retorna o maior número de uma lista.
- sum(digitos): Faz o somatório de uma lista de números.

**List comprehensions**

- No exemplo a seguir de uma list comprehension, é criada uma lista dos quadrados dos primeiros números de 1 a 10.
```python
quadrados = [numero**2 for numero in range(1,11)]
```

- O equivalente sem list comprehension, ficaria:
```python
quadrados = []
for numero in range(1,11):
    quadrados.append(numero**2)
```

**Fatiando uma lista - slicing**

- A sintaxe de slicing de listas no python é: lista[início:fim:passo]
- Os índices são como no método range(), para ir até o último elemento da lista, é necessário ir um número além do índice. Por exemplo, o seguinte código imprime ['a', 'b', 'c'], ou seja, os elementos 0, 1 e 2:
```python
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[0:3])
```

- Com a omissão do primeiro índice, inicia-se no primeiro elemento. Com a omissão do último, finaliza-se no último.
- Também funcionam os índices negativos. No seguinte exemplo, serão apresentados os últimos elementos da lista: ['c', 'd', 'e']].
```python
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[-3:])
```

- Se você omitir o início e o fim, deixando apenas os dois pontos, ele percorre a lista inteira:
```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Pega do começo ao fim, pulando de 2 em 2
print(numeros[::2])
# Saída: [0, 2, 4, 6, 8]
```

- Se você colocar um número negativo no passo, o Python percorre a lista de trás para frente:
```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[::-1])
# Saída: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

**Percorrendo uma fatia com for**

- Também é possível percorrer uma lista com os conceitos de fatiamento de listas. No exemplo a seguir, ao invés de percorrer toda a lista, percorremos somente os três primeiros jogadores:
```python
jogadores = ['charles', 'martina', 'michael', 'florence', 'eli']
    for jogador in jogadores[:3]:
        print(jogador)
```

**Copiando listas**

- Ao se copiar uma lista para a outra, se eu fizer lista2 = lista1, ambas as variáveis apontam para a mesma lista. Como resultado, quando adicionamos um elemento na lista2, ele é adicionado na lista1, e vice-versa.
- Para se copiar de forma independente os elementos de uma lista à outra, o correto é fazer:
```python
lista2 = lista'[:]
```

**Tuplas**

- Tuplas são listas imutáveis.
- tupla = ('a', 'b', 'c')

## CAP 5 - IF

- Para verificar se um valor está em uma lista, basta fazer if valor in lista:

- Exemplo de uso de if - elif - else:
```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
```

**Verificando se uma lista não está vazia**
- Quando o nome de uma lista é utilizado em uma instrução if, o Python retorna True se a lista contiver pelo menos um elemento; uma lista vazia é avaliada como False. Exemplo:
```python
requested_toppings = []
if requested_toppings: #Não entra, pois a variável retorna False
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
else: #Entra, pois a variável retorna False
    print("Are you sure you want a plain pizza?")
```

## CAP 6 - DICIONÁRIOS


- Para adicionar um novo par chave-valor, basta colocar o nome do dicionário seguido pela nova chave entre colchetes, com o valor novo:
 ```python
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
```

- Para modificar um valor em um dicionário, basta colocar o nome do dicionário com a chave entre colchetes e, em seguida, o valor novo
que deseja associar a essa chave:
 ```python
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'
```

- Para remover um valor no dicionário, basta utilizar o del:
 ```python
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
```

- É possível utilizar o get() para acessar valores de dicionários, para definirmos uma saída padrão se a chave solicitada não existir:
 ```python
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
```

**Percorrendo os pares chave-valor de um dicionário com um laço**

- Para percorrer todos os pares chave-valor de um dicionário com um laço usamos 2 variáveis, uma para a chave e outra para o valor, e o método items(), que retorna uma sequência de pares chave-valor: 
 ```python
for key, value in user.items():
 ```

**Percorrendo as chaves de um dicionário com um laço**

- Para percorrer todas as chaves de um dicionário com um laço, usamos o método keys(), que retorna as chaves, ou omitindo o método keys (ele é utilizado por padrão):
 ```python
for name in favorite_languages.keys():
#ou então:
for name in favorite_languages:
```

**Percorrendo os valores de um dicionário com um laço**

- Para percorrer todos os valores de um dicionário com um laço, usamos o método values(), que retorna os valores. 
 ```python
for language in favorite_languages.values():
```

- Para retornar uma coleção de valores únicos, tirando os duplicados, podemos utilizar o método set():
 ```python
for language in set(favorite_languages.values()):
```
