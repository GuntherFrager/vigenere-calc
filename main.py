def main():
    
    # Solicitar la ruta del archivo .txt
    file_path = input("Por favor, indique la ruta del archivo (.txt): ")

    # Verificar si la ruta del archivo existe y es válida
    try:
        archivo = open(file_path, 'r')
        print(f"El archivo {file_path} se ha abierto correctamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo en la ruta: {file_path}")
        return
    except Exception as e:
        print(f"Ocurrió un error al intentar abrir el archivo: {e}")
        return

    # Solicitar la contraseña
    password = input('Por favor, ingrese la contraseña: ')
    
    # cifrado
    from funciones import cifrado
    from funciones import descifrado
    
    action = input("Desea cifrar o descifrar el archivo? [C/D]")
    if action.upper() == "C":
        texto = archivo.read()
        archivo_nuevo = 'archivo_cifrado.txt'
        archivo_nuevo = open(archivo_nuevo, 'w')
        cifrado(texto, password, archivo_nuevo)
    elif action.upper() == "D":
        texto = archivo.read()
        archivo_nuevo = 'archivo_descifrado.txt'
        archivo_nuevo = open(archivo_nuevo, 'w')
        descifrado(texto, password, archivo_nuevo)
    else:
        print("La orden indicada no es valida, o bien ha ocurrido algun error inesperado")

    input("Presione Enter para salir...")


if __name__ == "__main__":
    main()
