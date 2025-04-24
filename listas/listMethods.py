list = []

#adicionar elementos a lista
list.append(1)
list.append("Hello")
list.append(2.5)
print(list)

#limpar a lista
# list.clear()
print(list)

#copiar a lista
listCopy = list.copy()
listCopy.append("copy")
print(listCopy , list)

#contar o numero de vezes que um elemento aparece na lista
print(list.count(1))

#extends - adicionar elementos de outra lista a lista
list.extend([10])
print(list)

#achar primeira ocorrencia de um elemento na lista
print(list.index("Hello"))

#remover ultimo elemento da lista
list.pop()
print(list)

#remover um elemento especifico da lista
list.remove(1)
print(list)

#reverter a lista
list.reverse()
print(list)