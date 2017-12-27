import psycopg2
import sys
import pprint

conn_string = "host='127.0.0.1' dbname='Fundamentos' user='root' password='042nTh891L'"

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO estudiantes (matricula, cedula, nombres, apellidos, paralelo) VALUES (%s, %s, %s, %s, %s)", ("000000000", "0000000000", "NO IDENTIFICADO", "NO IDENTIFICADO", 999))
except psycopg2.IntegrityError:
    pass

file = open("/Fundamentos/VisorFundamentos/BASEQUERIES/FUNDAMENTOS DE PROGRAMACION 107_csv.csv", encoding='latin-1')
for line in file:
    estudiante = line.split(";")
    if len(estudiante) > 1:
        nom_completo = estudiante[2].split(",")
        nombres = nom_completo[1].replace("\n", "")
        apellidos = nom_completo[0]
        try:
            cursor.execute("INSERT INTO estudiantes (matricula, cedula, nombres, apellidos, paralelo) VALUES (%s, %s, %s, %s, %s)", (estudiante[0], estudiante[1], nombres, apellidos, 107))
        except (psycopg2.IntegrityError, psycopg2.InternalError):
            continue

file = open("/Fundamentos/VisorFundamentos/BASEQUERIES/FUNDAMENTOS DE PROGRAMACION 207_csv.csv", encoding='latin-1')
for line in file:
    estudiante = line.split(";")
    if len(estudiante) > 1:
        nom_completo = estudiante[2].split(",")
        nombres = nom_completo[1].replace("\n", "")
        apellidos = nom_completo[0]
        try:
            cursor.execute("INSERT INTO estudiantes (matricula, cedula, nombres, apellidos, paralelo) VALUES (%s, %s, %s, %s, %s)", (estudiante[0], estudiante[1], nombres, apellidos, 207))
        except (psycopg2.IntegrityError, psycopg2.InternalError):
            continue
        

conn.commit()
file.close()

# Close communication with the database
cursor.close()
conn.close()
    
