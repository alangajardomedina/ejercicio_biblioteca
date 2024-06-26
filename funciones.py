import json

libros = []

#funciones del ejercicio
def agregar_libro():
    print("AGREGAR LIBRO:")
    titulo = input("Ingrese título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    anio = int(input("Ingrese el año de publicación del libro: "))
    genero = input("Ingrese el género del libro: ")

    libro = {
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "genero": genero
    }

    libros.append(libro)
    print("Libro agregado con éxito!")
def mostrar_libros():
    if not libros:
        print("ERROR! debe agrear libros en la opción 1")
    else:
        print("\tLISTA DE LIBROS")
        for li in libros: #¿Que tipo de dato es li? -> Lista
            print(f"Título: {li['titulo']}")
            print(f"Autor: {li['autor']}")
            print(f"Año de publicación: {li['anio']}")
            print(f"Género: {li['genero']}")
            print()

def buscar_libro():
    if not libros:
        print("ERROR! debe agrear libros en la opción 1")
    else:
        print("\tBUSCAR LIBRO") #cambia el titulo
        titulo_buscar = input("Ingrese tìtulo del libro que desea: ") #se agrega el input del libro que buscamos
        for li in libros: #¿Que tipo de dato es li? -> Lista
            if titulo_buscar.lower() == li['titulo'].lower(): #Comparar el título buscado con algún título existente.
                print(f"Título: {li['titulo']}")
                print(f"Autor: {li['autor']}")
                print(f"Año de publicación: {li['anio']}")
                print(f"Género: {li['genero']}")
                return
        print(f"ERROR! libro {titulo_buscar} no encontrado!")
    
def modificar_libro():
    if not libros:
        print("ERROR! debe agrear libros en la opción 1")
    else:
        print("\tMODIFICAR LIBRO") #cambia el titulo
        titulo_modificar = input("Ingrese tìtulo del libro que quiere modificar: ") #se agrega el input del libro que buscamos
        for li in libros: #¿Que tipo de dato es li? -> Lista
            if titulo_modificar.lower() == li['titulo'].lower(): #Comparar el título buscado con algún título existente.
                li['autor'] = input("Ingrese nuevo autor: ")
                li['anio'] = int(input("Ingrese nuevo año de publicación: "))
                li['genero'] = input("Ingrese nuevo género: ")
                print("Libro modificado con éxito!")
                return
        print(f"ERROR! libro {titulo_modificar} no encontrado!")
    
def exportar_json():
    if not libros:
        print("ERROR! no existen libros, agregue un libro en la opción 1.")
    else:
        print("EXPORTAR JSON")
        nomrbe_archivo = input("Ingrese nombre del archivo") +".json"
        
        try:
            with open(nomrbe_archivo, "a", encoding="utf-8") as archivo:
                json.dump(libros, archivo, indent=4)
        except FileExistsError:
            print("ERROR! el nombre del archivo ya existe!")
        print("Archivo creado con éxito!")

def salir():
    print("Gracias, adiós!")
    exit()