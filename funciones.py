libros = []
#funciones del ejercicio
def agregar_libro():
    print("AGREGAR LIBRO")
    titulo=input("Ingrese título: ")
    autor=input("Ingrese autor: ")
    anio=int(input("Ingrese año de publicación: "))
    genero=input("Ingrese género: ")
    libro={"titulo":titulo, "autor":autor, "anio":anio, "genero":genero}
    libros.append(libro)
    print("LIBRO AGREGADO CON ÉXITO")
def mostrar_libros():
    if not libros:
        print("NO EXISTEN LIBROS, POR FAVOR AGREGUE ALGUNO!")
    else:
        print("\tLISTA DE LIBROS")
        for l in libros:
            print("TÍTULO:", l['titulo'])
            print("AUTOR:", l['autor'])
            print("AÑO:", l['anio'])
            print("GÉNERO:", l['genero'])
            print()
def buscar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, POR FAVOR AGREGUE ALGUNO!")
    else:
        print("BUSCAR LIBRO")
        titulo_buscar=input("Ingrese título del libro que desea: ")
        for l in libros:
            if titulo_buscar.lower()==l["titulo"].lower():
                print("TÍTULO:", l['titulo'])
                print("AUTOR:", l['autor'])
                print("AÑO:", l['anio'])
                print("GÉNERO:", l['genero'])
                return
        print(f"NO EXISTE EL TÍTULO {titulo_buscar}.")
def modificar_libro():
    if not libros:
        print("NO EXISTEN LIBROS, POR FAVOR AGREGUE ALGUNO!")
    else:
        print("MODIFICAR LIBRO")
        titulo_modificar=input("Ingrese título del libro que desea: ")
        for l in libros:
            if titulo_modificar.lower()==l["titulo"].lower():
                l["autor"]=input("Ingrese nuevo autor: ")
                l["anio"]=int(input("Ingrese nuevo año de publicación: "))
                l["genero"]=input("Ingrese nuevo género: ")
                print("LIBRO MODIFICADO CON ÉXITO!")
                return
        print(f"NO EXISTE EL TÍTULO {titulo_modificar}.")
        
def exportar_json():
    if not libros:
        print("NO EXISTEN LIBROS, POR FAVOR AGREGUE ALGUNO!")
    else:
        nombre_archivo=input("Ingrese nombre del archivo: ")+".json"
        import json
        try:
            with open(nombre_archivo, "x",encoding="utf-8") as archivo:
                json.dump(libros,archivo,indent=4)
            print("ARCHIVO CREADO CON ÉXITO!")
        except:
            print("NOMBRE DEL ARCHIVO YA EXISTE, POR FAVOR ESCRIBA OTRO!")
def salir():
    print("GRACIAS, ADIOS!")
    exit()