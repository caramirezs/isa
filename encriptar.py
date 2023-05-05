def encrypt(frase):
    # creamos un diccionario con las letras del alfabeto y sus respectivos valores encriptados
    alfabeto = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9',
                'j': '0', 'k': '!', 'l': '@', 'm': '#', 'n': '$', 'o': '%', 'p': '&', 'q': '*', 'r': '(', 's': ')',
                't': '-', 'u': '+', 'v': '/', 'w': '=', 'x': ':', 'y': ';', 'z': '<',
                'á': '1', 'é': '5', '5': '9', 'ó': '%', 'ú': '+', 'ñ': '$'}
    # convertimos la frase a minúsculas
    frase = frase.lower()
    # creamos una lista con las letras de la frase
    letras = list(frase)
    # recorremos la lista de letras y las sustituimos por sus valores encriptados
    for i in range(len(letras)):
        if letras[i] in alfabeto:
            letras[i] = alfabeto[letras[i]]
    # mezclamos las letras de la frase

    # convertimos la lista de letras en una cadena
    frase_encriptada = ''.join(letras)
    return frase_encriptada


frase_original = 'Regresar al inicio'
frase_encriptada = encrypt(frase_original)
print(frase_encriptada)
