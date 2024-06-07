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
   cd hamburguesasIt
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

**EDUCACIONIT**


