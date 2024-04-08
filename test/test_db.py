import psycopg2
import os, dotenv

dotenv.load_dotenv('../docker/postgres/.env')

import subprocess

def test_database_connection():
    # Obtener las variables de entorno
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    database = os.getenv("POSTGRES_DB")

    # Verificar si las variables de entorno están configuradas
    assert user is not None, "La variable de entorno POSTGRES_USER no está configurada"
    assert password is not None, "La variable de entorno POSTGRES_PASSWORD no está configurada"
    assert database is not None, "La variable de entorno POSTGRES_DB no está configurada"
    
    # Verificar si el contenedor de PostgreSQL está en ejecución
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    assert "postgres" in result.stdout, "El contenedor de PostgreSQL no está en ejecución"

    try:
        # Conectarse a la base de datos
        conn = psycopg2.connect(
            host="localhost",
            database=database,
            user=user,
            password=password
        )

        # Crear un cursor
        cur = conn.cursor()

        # Ejecutar una consulta para verificar la conexión
        cur.execute('SELECT 1')

        # Obtener los resultados
        results = cur.fetchall()

        # Verificar los resultados
        assert len(results) == 1 and results[0][0] == 1, "La conexión a la base de datos falló"

        # Cerrar la conexión
        conn.close()

    except Exception as e:
        assert False, f"Error al conectarse a la base de datos: {e}"