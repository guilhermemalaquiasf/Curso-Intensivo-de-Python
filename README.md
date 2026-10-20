# ANOTAÇÕES PARA RECORDAR

Anotações do livro Curso Intensivo de Python, do Eric Matthes.

## CAP 2 - VARIÁVEIS E TIPOS DE DADOS SIMPLES

### STRINGS

- texto.title(): Somente primeiras letras maiúsculas, resto minúsculas.
- texto.upper(): Tudo maiúsculo.
- texto.lower(): Tudo minúsculo.
- f"{texto1} {texto2}": f-strings, junta strings.
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
- lista.pop(): Remove o último elemento e retorna o seu valor. Também é possível remover qualquer posição com lista.pop(posição).
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
```
quadrados = [numero**2 for numero in range(1,11)]
```
O equivalente sem list comprehension, ficaria:
```
quadrados = []
for numero in range(1,11):
    quadrados.append(numero**2)
```

**Fatiando uma lista**

- Os índices são como no método range(), para ir até o último elemento da lista, é necessário ir um número além do índice. Por exemplo, o seguinte código imprime ['a', 'b', 'c'], ou seja, os elementos 0, 1 e 2.
```
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[0:3])
```
- Com a omissão do primeiro índice, inicia-se no primeiro elemento. Com a omissão do último, finaliza-se no último.
- Também funcionam os índices negativos. No seguinte exemplo, serão apresentados os últimos elementos da lista: ['c', 'd', 'e']].
```
lista = ['a', 'b', 'c', 'd', 'e']
print(lista[-3:])
```
