libros = []
#funciones del ejercicio
def agregar_libro():
    print("agregar libro")
    titulo = input("ingrese titulo:")
    autor = input("ingrese autor:")
    anio = input("ingrese año de publicacion :")
    genero = input("ingrese genero:")
    libro = {"titulo":titulo, "autor": autor, "anio":anio, "genero":genero}
    libros.append(libro)
def mostrar_libros():
    if not libros:
        print("no existen libros,porfavor agrege")
    else:
        print("\tlista de libros")
        for li in libros:
            print("titulo", li['titulo'])
            print("autor", li['autor'])
            print("año", li['anio'])
            print("genero", li['genero'])
            print()
def buscar_libro():
    if not libros:
        print("no existen libros,porfavor agrege")
    else:
        print("buscar libro")
        titulo_buscar=input("ingrese titulo del libro que desa: ")
        for li in libros:
            if titulo_buscar.lower()==li["titulo"].lower():
                print("titulo", li['titulo'])
                print("autor", li['autor'])
                print("año", li['anio'])
                print("genero", li['genero'])
                return
        print(f"el titulo no existe {titulo_buscar}")
def modificar_libro():
    if not libros:
        print("no existen libros,porfavor agrege")
    else:
        print("buscar libro")
        modificar_titulo=input("ingrese titulo del libro que desa: ")
        for li in libros:
            if modificar_titulo.lower()==li["titulo"].lower():
                print("titulo", li['titulo'])
                print("autor", li['autor'])
                print("año", li['anio'])
                print("genero", li['genero'])
                return
        print(f"el titulo no existe{modificar_libro}")
def exportar_json():
    if not libros:
        print("no existen libros,porfavor agrege")
    else:
        nombre_archivo=input("ingrese el nombre del archivo")+".jsno"
        import json
        with open(nombre_archivo, "W")as archivo:
            json.dump(libros,archivo,indent=2)
        print("archivo creado con éxito")


def salir():
    print("gracias, adios")
    exit()