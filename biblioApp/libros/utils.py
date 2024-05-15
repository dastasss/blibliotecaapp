from django.db import connection

def ejecutar_consulta_row(consulta):
    with connection.cursor() as cursor:
        cursor.execute(consulta)
        resultados = cursor.fetchone()
    return resultados