
import time
import sqlite3
import os

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

#Función saludo luego de ingresar str nombre de encargado 
def saludo(nombre_encargado):
    print ("----------Bienvenido a Hamburguesas IT------------ \n Encargado: -> " + nombre_encargado)
    print("\n")
    print(">>> Recuerda, siempre hay que recibir al cliente con una sonrisa :) <<<)")

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
def guardarVenta(data):
    #Convierte los valores del diccionario en una tupla
    datos = tuple(data.values())
    #Conecta con la base de datos
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try: 
        #Inserta los datos en la tabla ventas
        cursor.execute("INSERT INTO ventas VALUES (null,?,?,?,?,?,?,?)", datos)
    except sqlite3.OperationalError:
        #Sila tabla no existe se crea y luego se insertan los datos
        cursor.execute("""CREATE TABLE IF NOT EXISTS ventas 
        ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT,
            fecha TEXT,
            ComboS INT,
            ComboD INT,
            ComboT INT,
            Flurby INT,
            total REAL
        )   
        """)
        cursor.execute("INSERT INTO ventas VALUES (null,?,?,?,?,?,?,?)", datos)
    conn.commit()
    conn.close()
    print("Datos guardados correctamente.")




#Funcion para guardar los datos del encargado 
def guardarEncargado(data):
    datosIn = (data["Nombre"], data["Ingreso"], "Ingreso", 0)
    datosOut =(data["Nombre"], data["Egreso"], "Egreso", data ["Facturado"])
    #Convierte los valores del diccionario en una tupla
    conn = sqlite3.connect("comercio.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosIn)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosOut)
    except sqlite3.OperationalError:
        cursor.execute("""CREATE TABLE registro 
        ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Encargado TEXT,
            Fecha TEXT,
            Evento TEXT,
            Caja REAL
        )
        """)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosIn)
        cursor.execute("INSERT INTO registro VALUES (null,?,?,?,?)", datosOut)
    conn.commit()
    conn.close()
    print("Datos guardados correctamente")  
    
#############################################################################    
   
if(os.name=="nt"):
    borrar = "cls"
else:
    borrar = "clear"
    
salir = True
os.system(borrar)

while salir:
    os.system(borrar)
    datos_encargado = {"Nombre" : " ","Ingreso": " ", "Egreso": " " , "Facturado":0}
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
        os.system(borrar)
        
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
                datos_encargado["Facturado"] = caja
                guardarEncargado(datos_encargado)
                break
            
        elif opcion == "3":
                datos_encargado["Egreso"] = time.asctime()
                datos_encargado["Facturado"] = caja
                guardarEncargado(datos_encargado)
                print("¡Muchas gracias por usar nuestro programa!")
                salir=False
                break
            
        else:
            print("Opción incorrecta, vuelva a intentarlo")
            
    
# Ejecutar el programa

  

    