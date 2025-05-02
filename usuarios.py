import hashlib
from datetime import datetime

class Usuarios:
    def __init__(self, db):
        self.db = db

    def registrar_usuario(self, nombre, email, password):
        try:
            self.db.cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            if self.db.cursor.fetchone():
                return {"exito": False, "mensaje": "El correo electrónico ya está registrado"}
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.cursor.execute("INSERT INTO usuarios (nombre, email, password, fecha_registro) VALUES (%s, %s, %s, %s)",
                                   (nombre, email, password_hash, fecha_registro))
            self.db.conexion.commit()
            return {"exito": True, "mensaje": "Usuario registrado correctamente", "id_usuario": self.db.cursor.lastrowid}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error al registrar usuario: {e}"}

    def login(self, email, password):
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            self.db.cursor.execute("SELECT id, nombre FROM usuarios WHERE email = %s AND password = %s",
                                   (email, password_hash))
            usuario = self.db.cursor.fetchone()
            if usuario:
                return {"exito": True, "mensaje": "Inicio de sesión exitoso", "id_usuario": usuario[0], "nombre": usuario[1]}
            else:
                return {"exito": False, "mensaje": "Credenciales incorrectas"}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error al iniciar sesión: {e}"}