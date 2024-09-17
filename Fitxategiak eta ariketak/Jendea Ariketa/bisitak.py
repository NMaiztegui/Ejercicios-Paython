import os
# a+ abre el contenido con el cursor al fianl si existe el archivo, si no lo crea y escribe al principio

def file_read (file):
    file.seek(0)
    irakurri = file.readlines()
    print(irakurri)

def parametro(cont,file):
    parametro= input("Sartu G edo K")

    if parametro == "G":
        cont +=1
        print(f"Kontadorearen balioa {cont}")
    elif parametro== "K":
            cont -=1
            print(f"Kontadorearen balioa {cont}")
    else:
        print(f"Kontadorearen balioa {cont}")

    vaciar_file(cont)
    file_read(file)
    return cont #devolver el nuevo valor de cont

def vaciar_file(cont):
    with open ("bisitak.txt", mode="w") as file:
        file.write(f"Kontadorea:{cont} \n")

def valor_contador (file):
    file.seek(0)  # Asegurarse de estar al principio del archivo
    lines = file.readlines()
    for line in lines:
        if "Kontadorea:" in line:  # Buscar la línea que contiene el contador
            # Extraer el valor numérico después de "Kontadorea:"
            valor = line.split(':')[1].strip()
            return int(valor)  # Devolver el valor como entero




#comprobar si la direccion del archivo existe, si existe leer su conteido
def main ():
    if os.path.exists("bisitak.txt"):
        with  open ("bisitak.txt", mode="r+") as file:
            cont = valor_contador(file)
            file_read(file)
            parametro(cont,file) #actualizar cont con el nuevo
    else:
        with open ("bisitak.txt", mode="a+")  as file:
            cont = 0
            file.write(f"Kontadorea:{cont} \n")
            file_read(file)
            parametro(cont,file) #actualizar cont con el nuevo
        
    


main()


