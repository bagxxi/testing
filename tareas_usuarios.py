class TareasUsuarios:
    def __init__(self, db):
        self.db = db

    def asignar_tarea(self, id_tarea, id_usuario):
        try:
            self.db.cursor.execute("SELECT * FROM tareas WHERE id = %s", (id_tarea,))
            if not self.db.cursor.fetchone():
                return {"exito": False, "mensaje": "Tarea no encontrada"}
            self.db.cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id_usuario,))
            if not self.db.cursor.fetchone():
                return {"exito": False, "mensaje": "Usuario no encontrado"}
            self.db.cursor.execute("UPDATE tareas SET asignada_a = %s WHERE id = %s", (id_usuario, id_tarea))
            self.db.conexion.commit()
            return {"exito": True, "mensaje": "Tarea asignada correctamente"}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error al asignar tarea: {e}"}

    def ver_tareas(self, fecha=None, estado=None, id_usuario=None):
        try:
            query = "SELECT * FROM tareas WHERE 1=1"
            parametros = []
            if fecha:
                query += " AND fecha_vencimiento = %s"
                parametros.append(fecha)
            if estado:
                query += " AND estado = %s"
                parametros.append(estado)
            if id_usuario:
                query += " AND asignada_a = %s"
                parametros.append(id_usuario)
            self.db.cursor.execute(query, parametros)
            tareas = []
            for fila in self.db.cursor.fetchall():
                tarea = {
                    "id": fila[0],
                    "titulo": fila[1],
                    "descripcion": fila[2],
                    "fecha_creacion": fila[3],
                    "fecha_vencimiento": fila[4],
                    "estado": fila[5],
                    "creada_por": fila[6],
                    "asignada_a": fila[7]
                }
                tareas.append(tarea)
            return {"exito": True, "mensaje": f"Se encontraron {len(tareas)} tareas", "tareas": tareas}
        except Exception as e:
            return {"exito": False, "mensaje": f"Error al buscar tareas: {e}"}