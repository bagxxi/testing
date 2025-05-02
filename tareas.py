from datetime import datetime

class Tareas:
    def __init__(self, db):
        self.db = db

    def crear_tarea(self, titulo, descripcion, fecha_vencimiento, estado="Pendiente", creada_por=None):
        try:
            fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.db.cursor.execute(
                "INSERT INTO tareas (titulo, descripcion, fecha_creacion, fecha_vencimiento, estado, creada_por) VALUES (%s, %s, %s, %s, %s, %s)",
                (titulo, descripcion, fecha_creacion, fecha_vencimiento, estado, creada_por)
            )
            self.db.conexion.commit()
            return {"exito": True, "mensaje": "Tarea creada correctamente", "id_tarea": self.db.cursor.lastrowid}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error al crear tarea: {e}"}

    def editar_tarea(self, id_tarea, datos):
        try:
            self.db.cursor.execute("SELECT * FROM tareas WHERE id = %s", (id_tarea,))
            if not self.db.cursor.fetchone():
                return {"exito": False, "mensaje": "Tarea no encontrada"}
            campos_permitidos = ["titulo", "descripcion", "fecha_vencimiento", "estado", "asignada_a"]
            campos = []
            valores = []
            for campo, valor in datos.items():
                if campo in campos_permitidos:
                    campos.append(f"{campo} = %s")
                    valores.append(valor)
            valores.append(id_tarea)
            query = f"UPDATE tareas SET {', '.join(campos)} WHERE id = %s"
            self.db.cursor.execute(query, valores)
            self.db.conexion.commit()
            if self.db.cursor.rowcount > 0:
                return {"exito": True, "mensaje": "Tarea actualizada correctamente"}
            else:
                return {"exito": False, "mensaje": "No se realizaron cambios en la tarea"}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error al editar tarea: {e}"}

    def eliminar_tarea(self, id_tarea):
        try:
            self.db.cursor.execute("SELECT * FROM tareas WHERE id = %s", (id_tarea,))
            if not self.db.cursor.fetchone():
                return {"exito": False, "mensaje": "Tarea no encontrada"}
            self.db.cursor.execute("DELETE FROM tareas WHERE id = %s", (id_tarea,))
            self.db.conexion.commit()
            return {"exito": True, "mensaje": "Tarea eliminada correctamente"}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error al eliminar tarea: {e}"}