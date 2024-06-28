**PROYECTO INTEGRADOR EN PYTHON >** 
**EDUCACIONIT**

# Sistema de Pedidos de Hamburguesas IT

Este es un sistema de pedidos desarrollado en Python con interfaz gráfica utilizando Tkinter. Permite gestionar los pedidos de hamburguesas y llevar un registro de las ventas y del personal encargado.

## Funcionalidades

- **Hacer un pedido**: Permite al usuario ingresar la cantidad de diferentes tipos de combos y postres para realizar un pedido. El sistema calcula automáticamente el total a pagar en función de los precios configurados y el tipo de cambio del dólar.
- **Cancelar pedido**: Ofrece la opción de cancelar el pedido en caso de que el usuario decida no confirmarlo.
- **Registro de ventas**: Guarda en una base de datos SQLite los detalles de cada venta, incluyendo el nombre del cliente, la fecha, la cantidad de cada ítem del pedido y el total facturado en pesos argentinos.
- **Registro de encargados**: Registra la entrada y salida de cada encargado del sistema, registrando la fecha y el total facturado durante su turno.

## Requisitos

- Python 3.x
- Tkinter (generalmente viene preinstalado con Python)
- SQLite (incluido en Python por defecto)
- Requests (instalable a través de pip: `pip install requests`)

## Instalación

1. Clonar el repositorio o descargar el código fuente.
2. Asegurarse de tener los requisitos previamente mencionados instalados.
3. Ejecutar el script principal `hamburgesasit.py` para iniciar la aplicación.

## Uso

1. Al iniciar la aplicación, se abrirá una ventana donde se podrá ingresar el nombre del encargado y realizar los pedidos.
2. Se puede ingresar la cantidad de cada tipo de combo y postre, así como el nombre del cliente.
3. Una vez confirmado el pedido, se mostrará el total a pagar en pesos.
4. Se puede cancelar el pedido en cualquier momento antes de confirmarlo.
5. La aplicación guarda automáticamente los detalles de cada venta y el registro de los encargados.

1. **Clona el repositorio:**
```bash
   git clone https://github.com/matiassenia/hamburguesasIt.git
   cd hamburguesasit
```

2. **Crea y activa el entorno virtual:**

```bash
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En Unix or MacOS
   source venv/bin/activate
```

3. **Instala las dependencias necesarias:**

```bash
   pip install requests
```

4. **Corre el programa:**

```bash
   python hamburguesasit.py

```

## Interfaz Gráfica

La interfaz gráfica permite realizar las siguientes acciones:

1. **Ingresar el nombre del encargado y la cantidad de cada tipo de combo (simple, doble, triple) y Flurby.**
2. **Ingresar el nombre del cliente.**
3. **Hacer Pedido:** Registra el pedido.
4. **Cancelar Pedido:** Permite cancelar el pedido actual.
5. **Salir seguro:** Guarda los datos del turno y cierra el programa de manera segura.

## Funcionalidades

### Ingreso de Pedido:

- Permite registrar el nombre del cliente y la cantidad de cada tipo de combo y Flurby.
- Calcula el total del pedido y muestra el resultado en una ventana emergente.
- Guarda los detalles del pedido en la base de datos SQLite.

### Cambio de Turno:

- Registra la salida del encargado actual y el total facturado durante su turno.
- Guarda los datos de inicio y fin de turno en la base de datos.

### Apagado del Sistema:

- Guarda los datos del turno actual y cierra el programa.

## Base de Datos

El programa utiliza SQLite para almacenar los datos de ventas y los registros de turnos. Si las tablas necesarias no existen, el programa las crea automáticamente.

### Tabla 'ventas':

- **id:** Identificador único.
- **cliente:** Nombre del cliente.
- **fecha:** Fecha del pedido.
- **ComboS:** Cantidad de combos simples.
- **ComboD:** Cantidad de combos dobles.
- **ComboT:** Cantidad de combos triples.
- **Flurby:** Cantidad de Flurbys.
- **total:** Total del pedido.

### Tabla 'registro':

- **id:** Identificador único.
- **encargado:** Nombre del encargado.
- **fecha:** Fecha del evento.
- **evento:** Tipo de evento (IN o OUT).
- **caja:** Total facturado.


### 

# IT Burger Ordering System

This is a burger ordering system developed in Python with a graphical interface using Tkinter. It allows managing burger orders and keeping a record of sales and personnel in charge.

## Features

- **Place an Order**: Allows the user to enter the quantity of different types of combos and desserts to place an order. The system automatically calculates the total amount to be paid based on the configured prices and the exchange rate of the dollar.
- **Cancel Order**: Provides the option to cancel the order if the user decides not to confirm it.
- **Sales Record**: Saves the details of each sale in an SQLite database, including the customer's name, date, quantity of each item in the order, and the total billed in Argentine pesos.
- **Staff Record**: Registers the entry and exit of each staff member, recording the date and the total billed during their shift.

## Requirements

- Python 3.x
- Tkinter (generally comes pre-installed with Python)
- SQLite (included with Python by default)
- Requests (installable via pip: `pip install requests`)

## Installation

1. Clone the repository or download the source code.
2. Ensure you have the aforementioned requirements installed.
3. Run the main script `hamburguesasit.py` to start the application.

## Usage

1. When starting the application, a window will open where you can enter the staff member's name and place orders.
2. Enter the quantity of each type of combo and dessert, as well as the customer's name.
3. Once the order is confirmed, the total amount to be paid in pesos will be displayed.
4. You can cancel the order at any time before confirming it.
5. The application automatically saves the details of each sale and the staff record.

### Clone the repository:
```bash
git clone https://github.com/matiassenia/hamburguesasIt.git
cd hamburguesasit
```
## Create and activate the virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```
## Install the necessary dependencies:
```bash
pip install requests
```
## Run the program:
```bash
python hamburguesasit.py
```

## Graphical Interface
# The graphical interface allows you to perform the following actions:

1.Enter the staff member's name and the quantity of each type of combo (simple, double, triple) and Flurby.
2.Enter the customer's name.
3.Place Order: Registers the order.
4.Cancel Order: Allows canceling the current order.
5.Safe Exit: Saves shift data and safely closes the program.

## Features
# Order Entry:
-Allows registering the customer's name and the quantity of each type of combo and Flurby.
-Calculates the total order and displays the result in a pop-up window.
-Saves the order details in the SQLite database.

# Shift Change:
-Registers the exit of the current staff member and the total billed during their shift.
-Saves the shift start and end data in the database.

# System Shutdown:
Saves the current shift data and closes the program.

## Database
The program uses SQLite to store sales data and shift records. If the necessary tables do not exist, the program creates them automatically.

# 'sales' Table:
-id: Unique identifier.
-customer: Customer's name.
-date: Order date.
-ComboS: Quantity of simple combos.
-ComboD: Quantity of double combos.
-ComboT: Quantity of triple combos.
-Flurby: Quantity of Flurbys.
-total: Total order amount.

# 'record' Table:
-id: Unique identifier.
-staff: Staff member's name.
-date: Event date.
-event: Type of event (IN or OUT).
-cash: Total billed.



