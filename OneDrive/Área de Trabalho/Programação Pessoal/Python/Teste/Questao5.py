def inverter_string(string):
    """Função que inverte os caracteres de uma string."""


    # Converte a string em uma lista de caracteres
    lista_caracteres = list(string)

    # Obtém o tamanho da lista de caracteres
    tamanho = len(lista_caracteres)

    # Inicializa um índice para o início da lista
    inicio = 0

    # Inicializa um índice para o fim da lista
    fim = tamanho - 1

    # Enquanto o índice de início for menor que o índice de fim
    while inicio < fim:

        # Troca os caracteres de posição usando uma variável temporária
        temp = lista_caracteres[inicio]
        lista_caracteres[inicio] = lista_caracteres[fim]
        lista_caracteres[fim] = temp
        # Move o índice de início para a direita
        inicio += 1
        # Move o índice de fim para a esquerda
        fim -= 1

    # Converte a lista de caracteres de volta para uma string
    string_invertida = ''.join(lista_caracteres)
    return string_invertida


# Exemplo de uso
string_original = "Hello, World!"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
