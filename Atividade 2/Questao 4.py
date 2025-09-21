#Dada uma lista de números inteiros, escreva uma função 
# para encontrar o segundo maior valor na lista.

def segundo_maior(lista):

    if len(lista) < 2:
        raise ValueError("A lista deve ter pelo menos dois elementos.")
    
    maior = segundo = float('-inf')

    for num in lista:
        if num > maior:
            segundo = maior
            maior = num
        elif num > segundo and num != maior:
            segundo = num
    
    if segundo == float('-inf'):
        raise ValueError("Não há segundo maior valor na lista.")
    
    return segundo


# Exemplo:
lista = [5, 8, 10, 15, 20, 20]
resultado = segundo_maior(lista)
print("O segundo maior valor é:", resultado)