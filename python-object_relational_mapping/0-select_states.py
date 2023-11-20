""" Importar el módulo MySQLdb """
import MySQLdb
import sys

def main():
    """ Verificar la cantidad correcta de argumentos """
    if len(sys.argv) != 4:
        print("Uso: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    """ Obtener los argumentos de la línea de comandos """
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Conectar a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Crear un cursor para ejecutar consultas
    cursor = db.cursor()

    # Ejecutar la consulta SQL
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Obtener y mostrar los resultados
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Cerrar la conexión
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
