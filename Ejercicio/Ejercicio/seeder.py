import os
import random
from datetime import datetime, timedelta
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Conexión a la base de datos MySQL desplegada en Docker
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    port=int(os.getenv("MYSQL_PORT", 3306)),
    user="root",
    password=os.getenv("MYSQL_ROOT_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)
cursor = db.cursor()

cursor.execute("SELECT id FROM categorias")
categoria_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM usuarios")
usuario_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id, precio_venta FROM productos")
productos = cursor.fetchall()

if not productos:
    print("No hay productos en la base de datos. Ejecuta el SQL inicial primero.")
    exit()

metodos_pago = ['efectivo', 'tarjeta', 'transferencia']
num_ventas = 300
print(f"Generando {num_ventas} ventas ficticias...")

fecha_inicio = datetime.now() - timedelta(days=180)

for _ in range(num_ventas):
    dias_aleatorios = random.randint(0, 180)
    horas_aleatorias = random.randint(8, 20)
    minutos_aleatorios = random.randint(0, 59)
    fecha_venta = fecha_inicio + timedelta(days=dias_aleatorios, hours=horas_aleatorias, minutes=minutos_aleatorios)

    usuario_id = random.choice(usuario_ids)
    metodo = random.choice(metodos_pago)
    cursor.execute(
        "INSERT INTO ventas (usuario_id, total, metodo_pago, fecha) VALUES (%s, %s, %s, %s)",
        (usuario_id, 0.0, metodo, fecha_venta.strftime('%Y-%m-%d %H:%M:%S'))
    )
    venta_id = cursor.lastrowid

    # Insertar entre 1 y 5 productos en el detalle de esta venta
    total_venta = 0.0
    num_items = random.randint(1, 5)
    productos_seleccionados = random.sample(productos, min(num_items, len(productos)))

    for prod_id, precio_venta in productos_seleccionados:
        cantidad = random.randint(1, 10)
        precio_unitario = float(precio_venta)
        subtotal = round(cantidad * precio_unitario, 2)
        total_venta += subtotal

        cursor.execute(
            """INSERT INTO detalle_ventas
                   (venta_id, producto_id, cantidad, precio_unitario, subtotal)
               VALUES (%s, %s, %s, %s, %s)""",
            (venta_id, prod_id, cantidad, precio_unitario, subtotal)
        )

    cursor.execute(
        "UPDATE ventas SET total = %s WHERE id = %s",
        (round(total_venta, 2), venta_id)
    )

db.commit()
print("¡Seeder completado con éxito! Se agregaron nuevos registros de ventas.")
cursor.close()
db.close()