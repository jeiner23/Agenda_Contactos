
def mostrar_menu():
    print("\nAgenda De Contactos")
    print("1. Agregar Nuevo Contacto")
    print("2. Eliminar Contacto")
    print("3. Buscar Contacto")
    print("4. Lista De Contacto")
    print("5. Salir De La Agenda")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Ingrese su nombre: ")
    celular = input("Ingrese su numero de celular: ")
    email = input("Ingrese su correo electronico: ")
    agenda[nombre] = {"Celular": celular, "Email": email}
    print("\n")
    print(f"¡Se ha guardado el contacto '{nombre}' exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Dijite el contacto que desea eliminar: ")
    print("\n")
    if nombre in agenda:
        del agenda[nombre]
        print("\n")
        print(f"¡El contacto '{nombre}' ha sido eliminado!")
    else:
        print(f"¡No existe el contacto '{nombre}'!")

def buscar_contacto(agenda):
    nombre = input("Dijite el contacto que desea buscar: ")
    print("\n")
    print("Informacion del contacto")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Celular: {agenda[nombre]['Celular']}")
        print(f"Email: {agenda[nombre]['Email']}")
    else:
        print("\n")
        print(f"El contacto '{nombre}' no ha sido encontrado")

def listar_contacto(agenda):
    if agenda:
        print("\nLista De Contactos")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Celular: {info['Celular']}")
            print(f"Email: {info['Email']}")
            print("-" * 20)
    else:
        print("\n")
        print("La Agenda Aun Esta Vacia")

def agenda_contacto():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Elija Una Opcion: ")
        print("\n")
        if opcion == "1":
            print("Digite la siguiente informacion")
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contacto(agenda)
        elif opcion == "5":
            print("\n")
            print("La agenda de contacto se ha cerrado")
            break
        else:
            print("Elija Una Opcion Valida(del 1 al 5)")

agenda_contacto()

