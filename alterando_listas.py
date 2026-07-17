frutas = ["melancia", "jabuticaba", "laranja", "uva"]

# Adicionando itens (append(), insert())
# Removendo itens (del, pop(), remove())
# Organizando listas (sort(), sorted(), reverse())
# Descobrindo o tamanho da lista (len())

print(frutas)

# Add um elemento no fim da lista
frutas.append("tomate")
print(frutas)

# Add um elemento no indice escolhido, com tanto que nao seja na ultima posicao, para isso devesse usar o len() deste modo
# frutas.insert(len(frutas), "banana") POSSIVELMENTE UMA GAMBIARRA
frutas.insert(1,"banana")
print(frutas)

# Usando DEL() ele remove o elemento PS: aceita apenas o indice como parametro
del frutas[2]
print(frutas)

# Usando POP() ele remove o elemento e atribui em uma variavel para ser retornado PS: aceita apenas o indice como parametro
fruta_estoque = frutas.pop(1)
print(fruta_estoque)
print(frutas)

# Usando REMOVE, ele remove o intem da lista usando como parametro o intem em sim como "uva"
frutas.remove("uva")
print(frutas)

# Usando o REVERSE para inverter os valores da lista 
frutas.reverse()
print(frutas)


# Usando SORT para Ordenar uma lista em ordem crescente e decrescente reverse=True
# Usando SORTED para nao alterar o original

numeros_1 = [3, 4, 1, 5, 12, 11, 10, 8, 15]
numeros_1.sort
print(numeros_1)

numeros = [3, 4, 1, 5, 12, 11, 10, 8, 15]
numeros_nao_alterados = sorted(numeros)
print(numeros_nao_alterados)
# Ta meio bagunçado mas vai ficar assim 

print(numeros_nao_alterados)
numeros_nao_alterados.sort(reverse=True)
print(numeros_nao_alterados)