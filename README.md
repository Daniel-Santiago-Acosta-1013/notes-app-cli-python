# Notas App

Esta aplicación permite a los usuarios gestionar notas de texto. Las notas pueden ser creadas, leídas, actualizadas y eliminadas. Además, los usuarios pueden buscar y filtrar notas por palabras clave y etiquetas, así como exportar e importar notas en formato JSON.

## Requisitos

- Python 3.7 o superior
- SQLAlchemy
- PostgreSQL
- python-dotenv

## Instalación

- Clone este repositorio.
- Instale las dependencias: `pip install -r requirements.txt`
- Copie el archivo `.env.example` a un nuevo archivo llamado `.env` y configure las variables de entorno según su configuración de base de datos.
- Ejecute python `main.py` para iniciar la aplicación.

## Estructura del proyecto
- `config.py`: Configuración de la base de datos y carga de variables de entorno.
- `database/db.py`: Configuración de la base de datos con SQLAlchemy.
- `models/note.py`: Modelo de la tabla notes en la base de datos.
- `models/tag.py`: Modelo de la tabla tags en la base de datos y relación note_tag.
- `operations/create.py`: Función para crear una nueva nota.
- `operations/read.py`: Funciones para mostrar, buscar, filtrar, exportar e importar notas.
- `operations/update.py`: Función para actualizar una nota existente.
- `operations/delete.py`: Función para eliminar una nota existente.
- `main.py`: Menú principal y bucle de la aplicación.

## Uso
- Ejecute python main.py para iniciar la aplicación.
- Seleccione una opción del menú para realizar la acción deseada.

## Las opciones del menú son las siguientes:

- Crear nota
- Mostrar notas
- Actualizar nota
- Eliminar nota
- Buscar y filtrar notas
- Exportar notas
- Importar notas
- Salir

Por favor, siga las instrucciones en pantalla para cada opción.
