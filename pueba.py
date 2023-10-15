arbitros = ["Brayan","Diego (No creo que este disponible la novia le pega)","Yoffer"  ]


def menu():
    
    while True:
        print("""
    1) Mostrar arbitros.
    2) Agregar arbitros.
    3) Eliminar arbitros.
    4) salir
    """)
        opc= int(input("Por favor ingresa una opcion"))

        if opc==1:
            Mos_arbitros()
            break
        
        elif opc==2:
            agregar_arbitros()
            break
        
        elif opc==3:
            Eliminar()
            break

        elif opc==4:
            print("vete a la verga")
            break

        else:
            print ("opcion invalida")
            break



def agregar_arbitros():
    Nombre= input("Por favor ingrese el nombre del arbitro")

    arbitros.append(Nombre)
    print(f"Estos son Los arbitros {Nombre} ingresas")

    volver=input("desea volver al inicio S/N").upper()

    if volver=="S":
        menu()

    else:
        print("Bay Bay")



def Eliminar():
    print("Estos son los arbitros a eliminar")

    for i, Nombre in enumerate(arbitros):
        print(f"{i+1},{Nombre}")

    if arbitros:
        opc = input("Por favor ingresar el numero del arbitro que desea eliminar")

        try:
            opc= int(opc)
            if 1 <= opc <= len(arbitros):
                Eliminar= arbitros.pop(opc -1)
                print(f"Arbitro{Eliminar} eliminado.")
            
            else:
                print("opcion invalida mamahuevo")

        except ValueError:
            print("opcion invalida, ingrese un numero")

    else:
        print("No se encuentra ningun arbitro en estos momentos")

    volver=input("desea volver al inicio S/N").upper()

    if volver=="S":
        menu()

    else:
        print("Bay Bay")


def Mos_arbitros():
    if arbitros:
        print("Estos son los arbitros disponibles")

        for i, Nombre in enumerate(arbitros):
            print(f"{i+1},{Nombre}")

    else:
        print("No se encuentran arbitros disponibles")

    volver=input("desea volver al inicio S/N").upper()

    if volver=="S":
        menu()

    else:
        print("Bay Bay")
