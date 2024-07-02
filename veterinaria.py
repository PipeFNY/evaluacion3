import os
os.system("cls")

menu = """
1. REGISTRAR MASCOTA
2. LISTAR MASCOTAS REGISTRADAS
3. IMPRIMIR FICHA DE REGISTRO
4. SALIR
Elija una opcion: 
"""
mascotas = []
especie = ["perro","gato","otro"]

registro = """ 
-----------------------------------------------------------------------------
  ESPECIE     NOMBRE     PESO     COST.INICIAL     IMP.SALUD     COST.TOTAL
----------------------------------------------------------------------------- 
"""
def registrar():
    while True:
        try:
            especie = input("ESPECIE: ")
            nombre = input("NOMBRE: ")
            peso = int(input("PESO: "))
            costo_inicial = int(input("COSTO INICIAL: "))
            costo_salud = int(input("COSTO SALUD: "))
            costo_total = int(input("COSTO TOTAL: "))
            mascotas.append([especie,nombre,peso,costo_inicial,costo_salud,costo_total])
            input("MASCOTA RESGISTRADA CON EXITO!!")
            break
        except Exception as e:
            input("excepcion al registrar:")

def listarMascotas():
    salida = registro
    for t in mascotas:
        salida += f" {t[0]} {t[1]} {t[2]}
        {t[3]} {t[4]} {t[5]} \n"
        print(salida)
        return salida
    
def imprimir():
    with open("listado.txt","w") as archivo:
        archivo.write(listarMascotas())
        input("FICHA DE REGISTRO IMPRESA!!")

#PROGRAMA PRINCIPAL
while True:
    try:
        opc = input(menu)
        if opc == "4":
            break
        elif opc == "1":
            registrar()
        elif opc == "2":
            listarMascotas()
        elif opc == "3":
            imprimir()
        else:
            input("OPCION INVALIDA!!")
    except Exception as e:
        input(f"excepcion al ejecutar: {str(e)}")






