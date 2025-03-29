#forma de interpolar strings depreciada
nome = "Jesse"
age = 20

print("Olá , meu nome é %s e tenho %d anos" % (nome, age)) #s -> strings %d -> inteiro %f -> float

print ("Olá , meu nome é {} e tenho {} anos".format(nome, age)) #forma de interpolar strings nova

print(f"Olá , meu nome é {nome} e tenho {age} anos") #forma de interpolar strings mais nova, a partir do python 3.6

PI = 3.14159265358979323846

print(f"PI = {PI:.2f}") #apenas duas casas decimais
