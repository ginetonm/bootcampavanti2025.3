#Crie uma função que receba uma lista de tuplas, 
# cada uma contendo o nome e a idade de uma pessoa, 
# e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def pegar_nome(pessoa):
    return pessoa[0]

def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=pegar_nome)


# Exemplo:
lista_tuplas = [("Carlos", 25), ("Ana", 30), ("Daniela", 28), ("Bruno", 20)]
resultado = ordenar_por_nome(lista_tuplas)

print("Lista ordenada pelo nome:", resultado)