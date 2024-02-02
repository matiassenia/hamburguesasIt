
import time
import sqlite3
import os

conn = sqlite3.connect("comercio.sqlite")
cursor = conn.cursor()

 
 
#Función para que ingrese un str obligatorio
def ingreso_str(mensaje, error):
    dato = input(mensaje)
    while dato == "":
        print(error)
        dato = input(mensaje)
    return dato  

#Función para que ingrese un int obligatorio
def ingreso_int(mensaje, error):
    while True:
        try:
            dato = int(input(mensaje))
            return dato
        except ValueError:
            print(error)
            
#Función para que ingrese un float         
def ingreso_float(mensaje, error):
    while True:
        try:
            dato = float(input(mensaje))
            return dato
        except ValueError:
            print(error)            

#Función para ingresar el nombre de encargado
def ingreso_encargado():
   print ("----------Bienvenido a Hamburguesas IT------------")
   nombre = input("Ingrese su nombre encargad@: ")
   return nombre
#nombreEncargado = ingreso_encargado()


#Función saludo luego de ingresar str nombre de encargado 
def saludo(nombre_encargado):
    print ("----------Bienvenido a Hamburguesas IT------------ \n Encargado: -> " + nombre_encargado)
    print("\n")
    print(">>> Recuerda, siempre hay que recibir al cliente con una sonrisa :) <<<)")
#saludo(nombreEncargado)

def ingresar():
    print("\n")
    print("-----------Bienvenido a Hamburguesas IT-------------")
    print("\n")
    nombre = ingreso_str("Ingrese su nombre encargad@: ","Error, campo vacio.")
    print("\n")
    return nombre

#Función impresión menú en pantalla
def mostrar_menu():
    print("\n🍔🍟🥤 ¡Bienvenido a Hamburguesas IT! 🥤🍟🍔")
    print("========================================")
    print("   Opciones:")
    print("   1 - Ingresar Nuevo Pedido")
    print("   2 - Cambio de Turno")
    print("   3 - Apagar Sistema")
    print("========================================")

#mostrar_menu()

#Función para confirmar o no el pedido
def confirmar():
    while True:
        respuesta = ingreso_str("Confirma pedido? Y/N (Y: para confirmar, N: para denegar): ", "Error, campo vacío")
        respuesta = respuesta.lower()  # Convertir la respuesta a minúsculas para comparación
        if respuesta == "y" or respuesta == "yes":
            return True
        elif respuesta == "n" or respuesta == "no":
            return False
        else:
            print("Ingrese únicamente Y o N")
       
#Funcion para guardar los datos de la venta
def guardarVenta(pedido):
    with open("ventas.txt", "a") as archivo:
        archivo.write(f"Cliente: {pedido['Cliente']}, Fecha: {pedido['Fecha']}, Compra: {str(pedido)} , Total: ${pedido['Total']}\n")
        
#Funcion para guardar los datos del encargado 
def guardarEncargado(data):
    ingreso = "INGRESO: " + data["Ingreso"] + " Encargad@: " + data ["Nombre"] + "\n"
    egreso = "EGRESO: " + data["Egreso"] + " Encargad@: " + data ["Nombre"] + " " "Monto total:$ " + str(data["Monto total"]) + "\n"
    separador = ("#"*50)+"\n"
    archivo = open("registro.txt","a")
    archivo.write(ingreso)
    archivo.write(egreso)
    archivo.write(separador)
    archivo.close()   
    
#############################################################################    
   
#Funcion para hacer el pedido
def main():
    salir= True
    while salir:
        datos_encargado = {"Nombre" : " ","Ingreso": " ", "Egreso": " " , "Monto total":0}
        encargado = ingresar()
        inicio = time.asctime()
        datos_encargado["Nombre"] = encargado
        datos_encargado["Ingreso"] = inicio
        caja = 0
        print("\n")
        while True:
            saludo(encargado)
            mostrar_menu()
            opcion = ingreso_str(">>>","Error, campo vacio")
            if opcion == "1":
                print("\n")
                pedido = {"Cliente": "","Fecha": "","ComboSimple" :0,"ComboDoble" :0,"ComboTriple" :0,"Flurby" :0,"Total" :0}
                pedido["Cliente"] = (ingreso_str("Ingrese nombre del Cliente: ", "Error, campo vacio"))
                pedido["ComboSimple"] = (ingreso_int("Ingrese cantidad de Combo S: ", "Error, elija solo numeros"))    
                pedido["ComboDoble"] = (ingreso_int("Ingrese cantidad de Combo D: ", "Error, elija solo numeros"))
                pedido ["ComboTriple"]= (ingreso_int("Ingrese cantidad de Combo T: ", "Error, elija solo numeros"))
                pedido ["Flurby"] = (ingreso_int("Ingrese cantidad de Combo Flurby: ", "Error, elija solo numeros"))
            
                #Calcular el total del pedido
                #Precios de los articulos:
                precio_combo_simple = 5
                precio_combo_doble = 6
                precio_combo_triple = 7
                precio_flurby = 2
            
               #Suma de los articulos seleccionados multiplicados por su precio
                total_pedido = (
                        pedido["ComboSimple"] * precio_combo_simple +
                        pedido["ComboDoble"] * precio_combo_doble +
                        pedido["ComboTriple"] * precio_combo_triple +
                        pedido["Flurby"] * precio_flurby
                )
                print("Total $", total_pedido)
                abona_con = ingreso_float('Abona con: $ ', 'Error, ingrese solo números')
                vuelto = abona_con - total_pedido
                while vuelto < 0:
                    print("El monto ingresado es menor que el monto total, \n por favor ingrese un monto mas grande")
                    abona_con = ingreso_float('Ingrese un monto más grande: $ ', 'Error, ingrese solo números')
                    vuelto = abona_con - total_pedido
                print (f'Su vuelto es: $ {vuelto}')
                     
                #Cuando el cliente confirma el pedido
                if  confirmar():
                    caja += total_pedido
                    pedido["Fecha"] = time.asctime()
                    pedido["Total"] = total_pedido
                    guardarVenta(pedido)
                    print("Pedido confirmado")
                else:
                    print("Pedido cancelado")
            elif opcion == "2":
                    datos_encargado["Egreso"] = time.asctime()
                    datos_encargado["Monto total"] = caja
                    guardarEncargado(datos_encargado)
                    break
            elif opcion == "3":
                    datos_encargado["Egreso"] = time.asctime()
                    datos_encargado["Monto total"] = caja
                    guardarEncargado(datos_encargado)
                    print("¡Muchas gracias por usar nuestro programa!")
                    salir=False
                    break
            else:
                print("Opción incorrecta, vuelva a intentarlo")
                print("\n*3")
    
# Ejecutar el programa
if __name__ == "__main__":
    main()

    