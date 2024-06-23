def cifrado(texto, contraseña, archivo):

    print(f"Cifrando el archivo")
    abecedario_numeros = 'abcdefghijklmnopqrstuvwxyz0123456789'
    diccionario_posiciones_numeros = {caracter: i+1 for i, caracter in enumerate(abecedario_numeros)}

    texto_cifrado = ''
    posicion_contraseña = 0
    for caracter in texto:
        if caracter.lower() in diccionario_posiciones_numeros:
            if posicion_contraseña >= len(contraseña):
                posicion_contraseña = 0
            
            posicion_caracter = diccionario_posiciones_numeros[caracter.lower()]
            posicion_contraseña_letra = diccionario_posiciones_numeros[contraseña[posicion_contraseña].lower()]
            nueva_posicion = (posicion_caracter + posicion_contraseña_letra) % len(abecedario_numeros)
            
            if caracter.isupper():
                texto_cifrado += abecedario_numeros[nueva_posicion - 1].upper()
            else:
                texto_cifrado += abecedario_numeros[nueva_posicion - 1]
                
            posicion_contraseña += 1
        else:
            texto_cifrado += caracter

    archivo.seek(0)
    archivo.write(texto_cifrado)
    archivo.truncate()
    
    print(f"Archivo cifrado")


def descifrado(texto_cifrado, contraseña, archivo):
    print(f"Descifrando el archivo")
    abecedario_numeros = 'abcdefghijklmnopqrstuvwxyz0123456789'
    diccionario_posiciones_numeros = {caracter: i+1 for i, caracter in enumerate(abecedario_numeros)}

    texto_descifrado = ''
    posicion_contraseña = 0
    for caracter in texto_cifrado:
        if caracter.lower() in diccionario_posiciones_numeros:
            if posicion_contraseña >= len(contraseña):
                posicion_contraseña = 0
            
            posicion_caracter = diccionario_posiciones_numeros[caracter.lower()]
            posicion_contraseña_letra = diccionario_posiciones_numeros[contraseña[posicion_contraseña].lower()]
            nueva_posicion = (posicion_caracter - posicion_contraseña_letra) % len(abecedario_numeros)
            
            if caracter.isupper():
                texto_descifrado += abecedario_numeros[nueva_posicion - 1].upper()
            else:
                texto_descifrado += abecedario_numeros[nueva_posicion - 1]
                
            posicion_contraseña += 1
        else:
            texto_descifrado += caracter
    
    archivo.seek(0)
    archivo.write(texto_descifrado)
    archivo.truncate()

    print(f"Archivo descifrado")
