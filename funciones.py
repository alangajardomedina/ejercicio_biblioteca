libros = []
#funciones del ejercicio
def agregar_libro():
    print("AGREGAR LIBRO")
    titulo = input("Ingrese titulo : ")
    autor = input("Ingrese autor : ")
    anio = int(input("Ingrese año de publicacion : "))
    genero = input("Ingrese género : ")
    libro = {"titulo":titulo,
             "autor": autor,
             "anio": anio,
             "genero":genero}
    libros.append(libro)
    print("LIBRO AGREGADO CON ÉXITO!")

def mostrar_libros():
    if not libros:
        print("NO HAY LIBROS AGREGADOS!!")
    else:
        print("\t LISTA DE LIBROS")
        for li in libros:    #que tipo de datos  es li == diccionario
            print("TITULO: ",li["titulo"])
            print("AUTOR: ",li["autor"])
            print("AÑO: ",li["anio"])
            print("GENERO: ",li["genero"])
            print()



def buscar_libro():
    if not libros:
        print("NO HAY LIBROS AGREGADOS!!")
    else:
        print("BUSCAR LIBRO")
        titulo_buscar = input("Ingrese el titulo del libro a buscar : ")
        for li in libros:    #que tipo de datos  es li == diccionario
            if titulo_buscar.lower()==li["titulo"].lower():
                print("TITULO: ",li["titulo"])
                print("AUTOR: ",li["autor"])
                print("AÑO: ",li["anio"])
                print("GENERO: ",li["genero"])
                return
        print(f"EL LIBRO {titulo_buscar} NO SE ENCUENTRA!")
              

def modificar_libro():
    if not libros:
        print("NO HAY LIBROS AGREGADOS!!")
    else:
        print("MODIFICAR LIBRO")
        titulo_modificar = input("Ingrese el titulo del libro a buscar : ")
        for li in libros:    #que tipo de datos  es li == diccionario
            if titulo_modificar.lower()==li["titulo"].lower():
                li["autor"] = input("Ingrese nuevo autor : ")
                li["anio"] = int(input("Ingrese nuevo año : "))
                li["genero"] = input("Ingrese nuevo genero : ")
                print("LIBRO MODIFICADO CON ÉXITO!")
                return
        print(f"EL LIBRO {titulo_modificar} NO SE ENCUENTRA!")

def exportar_json():
    if not libros:
        print("NO EXISTEN LIBROO")
    else:
        nombre_archivo = input("Ingrese nombre del archivo : ")+".json"
        import json
        try:
            with open(nombre_archivo, "w") as archivo:
                json.dump(libros, archivo, indent=2)
                print("ARCHIVO CREADO CON ÉXITO!!")
        except:
            print("EL NOMBRE DEL ARCHIVO YA EXISTE, ESCRIBA OTRO!!")


def salir():
    print(" GRACIOS, ADIOS!!")
    exit()