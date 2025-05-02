
# TaskPro - Sistema de Gestión de Tareas

Este es un sistema modular en Python para gestionar usuarios y tareas, con conexión a base de datos MySQL. Incluye registro, login, CRUD de tareas, asignación y visualización de tareas por usuario, fecha o estado.

## 📁 Estructura del proyecto

```
taskpro/
|├── __pycache__\
|└── .venv\
├── base_datos.py
├── usuarios.py
├── tareas.py
├── tareas_usuarios.py
├── main.py
├── test_taskpro.py
├── requirements.txt
├── .pylintrc
├── Informe Tecnicas de Testing Gabriel Balbontin.pdf 
└── test_taskpro.sql
 
```

## 🛠️ Requisitos

- Python 3.12
- MySQL Server (con base de datos `taskpro` y `taskpro_test` creadas)

## ⚙️ Configuración del entorno

### 1. Crea y activa un entorno virtual

**En Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta el sistema

```bash
python main.py
```

### 5. Ejecuta los tests

```bash
python test_taskpro.py
```

```bash
pylint main.py > pylint_taskpro_report.txt
```

### 6. Análisis de código con pylint

```bash
pylint *.py
```

## 🧪 Base de datos

Debe tener creadas las bases de datos:

```sql
CREATE DATABASE IF NOT EXISTS taskpro;
CREATE DATABASE IF NOT EXISTS taskpro_test;
```

## ✅ Dependencias

- `mysql-connector-python`
- `pylint` (solo para análisis de código)

## ✍️ Autor

Proyecto creado por `Gabriel Balbontín`  para la asignatura de `Plan de Pruebas de Software TILV21/ELE_952/V`
