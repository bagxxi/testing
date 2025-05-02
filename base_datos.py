import mysql.connector

class BaseDatos:
    def __init__(self, host='localhost', user='root', password='', database='taskpro'):
        try:
            self.conexion = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conexion.cursor(buffered=True)
            self.crear_tablas()
        except mysql.connector.Error as err:
            print(f"Error al conectar a MySQL: {err}")
            raise

    def crear_tablas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            fecha_registro DATETIME NOT NULL
        )''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tareas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL,
            descripcion TEXT,
            fecha_creacion DATETIME NOT NULL,
            fecha_vencimiento DATETIME NOT NULL,
            estado VARCHAR(20) NOT NULL,
            creada_por INT,
            asignada_a INT,
            FOREIGN KEY (creada_por) REFERENCES usuarios(id),
            FOREIGN KEY (asignada_a) REFERENCES usuarios(id)
        )''')
        self.conexion.commit()

    def cerrar(self):
        if self.conexion:
            self.conexion.close()