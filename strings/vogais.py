def conta_vogais(texto):
    # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    texto = "aeiouAEIOU"
    # TODO: Inicialize um contador para contar as vogais:
    
    contador = 0
    # Iteramos pelos caracteres da string
    for char in texto:
        # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char == "e" and "e" and "i" and "o" and "u" and "E" and "I" and "O" and "U" and "a" and "A":
            contador += 1
    return contador


texto = "testa"
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")