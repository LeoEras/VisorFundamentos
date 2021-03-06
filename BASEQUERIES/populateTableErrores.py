from git import Repo
import psycopg2
import os
import pprint
import xml.etree.ElementTree as xml
import sys

listErrorPython = ['StandardError', 'ArithmeticError', 'BufferError', 'LookupError', 'EnvironmentError',
					   'AssertionError', 'AttributeError', 'EOFError',
					   'FloatingPointError', 'GeneratorExit', 'IOError', 'ImportError', 'IndexError', 'KeyError',
					   'KeyboardInterrupt', 'MemoryError',
					   'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'ReferenceError', 'RuntimeError',
					   'StopIteration', 'SyntaxError',
					   'IndentationError', 'TabError', 'SystemError', 'SystemExit', 'TypeError', 'UnboundLocalError',
					   'UnicodeError', 'UnicodeEncodeError',
					   'UnicodeDecodeError', 'UnicodeTranslateError', 'ValueError', 'VMSError', 'WindowsError',
					   'ZeroDivisionError', 'FileNotFoundError']

def getID(user_identification, estudiantes):
    for record in estudiantes:
        if str(user_identification) in str(record[1])or str(user_identification) in str(record[2]):
            return record[0]
    return 1

conn_string = "host='localhost' dbname='Fundamentos' user='postgres' password='gPw19KX3_'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

cursor.execute("SELECT * FROM estudiantes")
estudiantes = cursor.fetchall()

base_path = os.path.dirname(os.path.realpath(__file__))
folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]
for item in folders:
    if "master" in item:
        continue
    real_folder_path = os.path.dirname(os.path.realpath(item)) + "\\" + item
    project_folders = [f for f in os.listdir(real_folder_path) if os.path.isdir(os.path.join(real_folder_path, f))]
    for folder in project_folders:
        if ".git" in folder:
            continue
        else:
            project_path = os.path.dirname(os.path.realpath(item + "\\" + folder)) + "\\" + folder
            log = project_path + "\\log.xml"
            error_caller_file = []
            try:
                element = xml.parse(log).getroot()
                for atype in element.findall('log_project'):
                    list_of_possible_error_files = []
                    name_proy = atype.get('name_project')
                    if atype.text is not None:
                        date = atype.get('date')
                        log_id = atype.get('id')
                        pro_name = atype.get('name_project')

                    if atype.text is None:
                        continue

                    for line in atype.text.splitlines():
                        for error in listErrorPython:
                            if error in line:
                                line_error = line.replace("\'", "")
                                error_thrown = error
                                
                    for line in atype.text.splitlines():
                        if "File" in line and "line" in line and ".py" in line and name_proy in line:
                            line = line.replace('"', "")
                            line = str.split(line, "/")
                            for word in line:
                                if ".py" in word:
                                    word = word.split(",")
                                    list_of_possible_error_files.append(word[0])

                        if len(list_of_possible_error_files) > 0:
                            error_caller_file = list_of_possible_error_files[-1]
                            error_caller_file = item + "\\" + folder + "\\" + error_caller_file
                        else:
                            error_caller_file = None

                    cursor.execute("INSERT INTO errores(user_id, fecha, proyecto, error, tipo_error, ruta_archivo) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", (getID(item, estudiantes), date, pro_name, line_error, error_thrown, error_caller_file))
            except:
                print(sys.exc_info())

conn.commit()
cursor.close()
conn.close()
