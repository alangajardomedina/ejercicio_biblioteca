libros = []
#funciones del ejercicio
def agregar_libro():
    print("Agregar libro")
    titulo=input("ingrese nombre: ")
    autor=input("ingrese autor: ")
    anio=int(input("ingrese año: "))
    genero=input("ingrese genero: ")
    libro={"titulo":titulo,
            "autor":autor,
            "anio":anio,
            "genero":genero}
    libros.append(libro)
    print("libro agregado")

def mostrar_libros():
    if not libros:
        print("NO existe libros")
    else:
        print("\t lista de libros")
        for li in libros:
            print("Titulo",li["titulo"])
            print("Autor",li["autor"])
            print("AÑO",li["anio"])
            print("Genero",li["genero"])

def buscar_libro():
    if not libros:
        print("NO existe libros")
    else:

        print("\t Buscar libros")
        titulo_buscar=input("ingrese titulo que desea: ")
        for li in libros:
            if titulo_buscar.lower()==li["titulo"].lower():
                print("Titulo",li["titulo"])
                print("Autor",li["autor"])
                print("AÑO",li["anio"])
                print("Genero",li["genero"])
                break

def modificar_libro():
    if not libros:
        print("NO existe libros")
    else:

        print("\t modificar libros")
        titulo_mod=input("ingrese titulo que desea: ")
        for li in libros:
            if titulo_mod.lower()==li["titulo"].lower():
                li["autor"]=input("ingrese nuevo autor: ")
                li["anio"]=int(input("ingrese nuevo año: "))
                li["genero"]=input("ingrese nuevo genero: ")
                print("libro modificado")
                break

def exportar_json():
    if not libros:
        print("NO existen libros")
    else:
        nombre_archivo=input("ingrese nombre archivo: ")+".json"
        import json
        with open (nombre_archivo,"w") as archivo:
            json.dump(libros,archivo,indent=2)
        print("archivo creado")
def salir():
    print("Adios")
    exit()