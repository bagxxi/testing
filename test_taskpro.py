import unittest
from base_datos import BaseDatos
from usuarios import Usuarios
from tareas import Tareas
from tareas_usuarios import TareasUsuarios
from datetime import datetime

class TestTaskPro(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = BaseDatos(host='localhost', user='root', password='', database='taskpro_test')
        cls.usuarios = Usuarios(cls.db)
        cls.tareas = Tareas(cls.db)
        cls.tareas_usuarios = TareasUsuarios(cls.db)

        cls.email = "test_user@example.com"
        cls.password = "testpass"
        cls.nombre = "Test User"

        cls.usuarios.db.cursor.execute("DELETE FROM usuarios WHERE email = %s", (cls.email,))
        cls.usuarios.db.conexion.commit()
        cls.user_result = cls.usuarios.registrar_usuario(cls.nombre, cls.email, cls.password)
        cls.user_id = cls.user_result.get("id_usuario")

    def test_login_exitoso(self):
        result = self.usuarios.login(self.email, self.password)
        self.assertTrue(result["exito"])
        self.assertEqual(result["nombre"], self.nombre)

    def test_creacion_tarea(self):
        fecha_vencimiento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = self.tareas.crear_tarea("Tarea de prueba", "Descripción", fecha_vencimiento, creada_por=self.user_id)
        self.assertTrue(result["exito"])
        self.__class__.tarea_id = result["id_tarea"]

    def test_asignar_tarea(self):
        self.test_creacion_tarea()
        result = self.tareas_usuarios.asignar_tarea(self.__class__.tarea_id, self.user_id)
        self.assertTrue(result["exito"])

    def test_editar_tarea(self):
        self.test_creacion_tarea()
        datos = {"titulo": "Tarea actualizada", "estado": "En Progreso"}
        result = self.tareas.editar_tarea(self.__class__.tarea_id, datos)
        self.assertTrue(result["exito"])

    def test_eliminar_tarea(self):
        self.test_creacion_tarea()
        result = self.tareas.eliminar_tarea(self.__class__.tarea_id)
        self.assertTrue(result["exito"])

    @classmethod
    def tearDownClass(cls):
        cls.db.cursor.execute("DELETE FROM tareas WHERE creada_por = %s", (cls.user_id,))
        cls.db.cursor.execute("DELETE FROM usuarios WHERE id = %s", (cls.user_id,))
        cls.db.conexion.commit()
        cls.db.cerrar()

if __name__ == "__main__":
    unittest.main()