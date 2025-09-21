#Escreva uma função que receba duas listas e retorne outra 
# lista com os elementos que estão presentes em apenas uma das listas.

def elementos_apenas_em_uma(lista1, lista2):

    resultado = []

    for item in lista1:
        if item not in lista2:
            resultado.append(item)

    for item in lista2:
        if item not in lista1:
            resultado.append(item)

    return resultado


# Exemplo:
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 4, 5, 6, 7]

resultado = elementos_apenas_em_uma(lista_1, lista_2)
print("Elementos que estão em apenas uma das listas:", resultado)