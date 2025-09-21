#Escreva uma função que receba uma lista de números e retorne 
# outra lista com os números primos presentes.

def filtrar_primos(lista):

    primos = []

    for n in lista:
        if n < 2:
            continue

        
        primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                primo = False
                break

        if primo:
            primos.append(n)

    return primos

# Exemplo:
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
resultado = filtrar_primos(lista)
print("Números primos:", resultado)
