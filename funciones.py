libros = []
#funciones del ejercicio
def agregar_libro():
    print("AGREGAR LIBRO")
    titulo = input("Ingrese Título: ")
    autor = input("Ingrese autor: ")
    anio = int(input("Ingrese año: "))
    genero = input("ingrese género: ")
    libro={"titulo":titulo, "autor":autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print("LIBRO AGREGADO CON ÉXITO!")

def mostrar_libros():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        print("\tLISTA DE LIBROS")
        for li in libros:
            print("TÍTULO:",li["titulo"])
            print("AUTOR:",li["autor"])
            print("AÑO:",li["anio"])
            print("GÉNERO:",li["genero"])
            print("")

def buscar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        print("\tBUSCAR LIBRO")
        titulo_buscar=input("Ingrese título del libro que desea: ")

        for li in libros:
            if titulo_buscar.lower()==li["titulo"].lower():
                print("TÍTULO:",li["titulo"])
                print("AUTOR:",li["autor"])
                print("AÑO:",li["anio"])
                print("GÉNERO:",li["genero"])
                return
        print(f"NO EXISTE EL TÍTULO {titulo_buscar}")

def modificar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, FAVOR AGREGUE ALGUNO!")
    else:
        print("\tMODIFICAR LIBRO")
        titulo_modificar=input("Ingrese título del libro que desea: ")

        for li in libros:
            if titulo_modificar.lower()==li["titulo"].lower():
                li["autor"]=input("Ingrese nuevo autor: ")
                li["anio"]=int(input("Ingrese nuevo año de publicación: "))
                li["genero"]=input("Ingrese nuevo género: ")
                print("LIBRO MODIICADO CON ÉXITO!")
                return
        print("NO EXISTE EL TÍTULO",modificar_libro)

def exportar_json():
    if not libros:
        print("NO EXISTEN LIBROS, FAVO AGREGUE ALGUNO!")
    else:
        nombre_archivo=input("ingrese nombre del archivo: ")+".json"
        import json
        try:
            with open(nombre_archivo,"X", enconding="utf-8") as archivo:
                json.dump(libros,archivo,indent=2)
            print("ARCHIVO CREADO CON ÉXITO!")
        except FileExistsError:
            print("NOMBRE DEL ARCHIVO YA EXISTE, FAVOR ESCRIBA OTRO!")
def salir():
    print("GRACIAS, ADIOS!")
    exit()