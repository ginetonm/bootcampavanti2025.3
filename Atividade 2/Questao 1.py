# Escreva uma função que receba uma lista de números e retorne outra lista 
# com os números ímpares.

def filtrar_impares(numeros):
    impares = [n for n in numeros if n % 2 != 0]
    return impares


# Exemplo:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
resultado = filtrar_impares(lista)

print("Números ímpares:", resultado)