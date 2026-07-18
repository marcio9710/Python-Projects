#3.4 Lista de convidados: Se pudesse convidar qualquer pessoa, viva ou falecida, para um jantar,
# quem você convidaria? Crie uma lista que tenha pelo menos três pessoas que gostaria de
# convidar para um jantar. Em seguida, use sua lista a fim de exibir uma mensagem para cada
# pessoa, convidando-a para o jantar.
convidados = ["heloisa", "tesla", "jose", "Shakira"]
for i in convidados:
    print(f"{i} voçê esta convidado para a melhor festa do ano.")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


### 3.5 Mudando a lista de convidados: Você acabou de ficar sabendo que um dos convidados não
# conseguirá ir ao jantar, assim precisa enviar um conjunto novo de convites. É necessário
# convidar outra pessoa.
convidados.remove("Shakira")
convidados.append("johnny depp")
print(f"\n{convidados[-1]} voçê esta convidado para a melhor festa do ano.")
print(convidados)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


##Comece com o programa do Exercício 3.4. No final do programa, adicione um print(),
# informando o nome do convidado que não irá ao jantar
convidados = ["heloisa", "tesla", "jose", "Shakira"]
for i in convidados:
    print(f"{i} voçê esta convidado para a melhor festa do ano.")

novo_convidado = "Joelma"
print(f"\n{novo_convidado} será o convidados substituto")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#Modifique sua lista substituindo o nome do convidado que não pode
# comparecer pelo nome da pessoa nova que você está convidando.
for i, name in enumerate(convidados): 
    if name == "Shakira":
        convidados[i] = novo_convidado
print(convidados) 

## Usando a propriedade INDEX()... Apenas teste descobrindo o indice do valor

novo_convidado1 = convidados.index("Joelma")
print(novo_convidado1)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


###Exiba um segundo conjunto de mensagens de convite,  
# uma para cada pessoa que ainda não consta em sua lista.
lista_nao_convidados = ["marcos", "daiane", "samantha"]
print(lista_nao_convidados)

##3.6 Mais convidados: Você acabou de encontrar uma mesa maior de jantar, agora há mais espaço 
# disponível. Convide mais três pessoas para o jantar.
# • Comece com o programa do Exercício 3.4 ou 3.5. No final do programa, adicione um print(),
# informando às pessoas que encontrou uma mesa maior.
# • Use um insert() para adicionar um convidado novo ao início de sua lista.
# • Use um insert() para adicionar um convidado novo no meio de sua lista.
# • Use um append() para adicionar um convidado novo no final de sua lista.
# • Exiba um conjunto novo de mensagens de convite, um para cada pessoa em sua lista.
convidados.insert(0,"mary")
convidados.insert(2,"price")
convidados.append("john")
for i in convidados:
    print(f"{i} voçê esta convidado para a melhor festa do ano.")


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////


 # 3.7 Reduzindo a lista de convidados: Você acabou de descobrir que sua mesa nova de jantar não
 # chegará a tempo e agora tem espaço somente para dois convidados.
 # • Comece com o programa do Exercício 3.6. Adicione uma linha nova que exiba uma mensagem
 # que você pode convidar apenas duas pessoas para o jantar.
 # • Use o pop() para remover convidados de sua lista, um de cada vez, até que restem somente
 # dois nomes nela. Sempre que remover um nome de sua lista, exiba uma mensagem para essa
 # pessoa informando que lamenta por não poder convidá-la para o jantar.
 # • Exiba uma mensagem para cada uma das duas pessoas que ainda estão na sua lista, informando
 # que ainda estão convidadas.
 # • Use o del para remover os dois últimos nomes de sua lista, para que ela fique vazia. Exiba sua
 # lista para ter certeza de que você realmente tem uma lista vazia no final do seu programa"""
while len(convidados) > 2:
    removido = convidados.pop()
    print(f"{removido} voce foi removido da lista")
print(convidados)
for i in convidados:
    print(f"{i} voce ainda esta convidado")

# apenas exemplo
while convidados:
    del convidados[0]

# se clear()
convidados.clear()
print(convidados)


# Ordenando a lista em ordem alfabetica usando o metodo sort()
cars = ["camaro", "porshe", "celta","fusca"]
cars.sort()
print(cars)

# Ordenando a lista em ordem alfabetica usando o metodo sort() com reverse
cars.sort(reverse=True)
print(cars)


# Usando metodo sorted para apenas visualisar os elemento em ordem alfabetica --> Não altera a lista"""
print(sorted(cars))
print(sorted(cars, reverse=True))

# Inverter a oredem de uma lista usanod reverse()"""
cars.reverse()
print(f"\n\n{cars}")

"""Usando len(Nome_lista) para descobrir o numero de elementos"""
print(f"o numero de elementos na lista e {len(cars)}")


# teste"""
sorted(cars)

print(f"{", ".join(cars)} .")

print(f"{", ".join(sorted(cars, reverse=True))}.")

print(f"o numero total de carros foi de {len(cars)}".title())