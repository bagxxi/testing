from base_datos import BaseDatos
from usuarios import Usuarios
from tareas import Tareas
from tareas_usuarios import TareasUsuarios
from datetime import datetime

if __name__ == "__main__":
    db = BaseDatos(host='localhost', user='root', password='', database='taskpro')
    usuarios = Usuarios(db)
    tareas = Tareas(db)
    tareas_usuarios = TareasUsuarios(db)

    resultado_registro = usuarios.registrar_usuario("Juan Pérez", "juan@example.com", "password123")
    print("Registro:", resultado_registro)

    resultado_login = usuarios.login("juan@example.com", "password123")
    print("Login:", resultado_login)

    if resultado_login["exito"]:
        id_usuario = resultado_login["id_usuario"]
        fecha_vencimiento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado_tarea = tareas.crear_tarea("Implementar login", "Crear pantalla de login con validación", fecha_vencimiento, creada_por=id_usuario)
        print("Crear tarea:", resultado_tarea)

        if resultado_tarea["exito"]:
            id_tarea = resultado_tarea["id_tarea"]
            resultado_asignacion = tareas_usuarios.asignar_tarea(id_tarea, id_usuario)
            print("Asignar tarea:", resultado_asignacion)

            resultado_ver_tareas = tareas_usuarios.ver_tareas(estado="Pendiente")
            print("Ver tareas:", resultado_ver_tareas)

            datos_actualizados = {"titulo": "Login y registro", "estado": "En Progreso"}
            resultado_edicion = tareas.editar_tarea(id_tarea, datos_actualizados)
            print("Editar tarea:", resultado_edicion)

            resultado_eliminacion = tareas.eliminar_tarea(id_tarea)
            print("Eliminar tarea:", resultado_eliminacion)

    db.cerrar()