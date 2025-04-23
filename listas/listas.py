frutas = ["banana", "manzana", "pera", "kiwi"]
print(frutas)
letras = list("jesse")
print(letras)


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][1])


list = ["p" , "y" , "t" , "h" , "o" , "n"]


#começo : fim : step(salto)
print(list[0:3]) # imprime p y t
print(list[2:5]) # imprime t h o
print(list[0:3:2]) 
print(list[::2])
print(list[::-1]) # imprime la lista al reves

carros = ["ford", "toyota", "honda", "chevrolet"]

for carro in carros:
    print(carro)
    

for i , carro in enumerate(carros):
    print(i, carro)