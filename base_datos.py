import sqlite3
#bd = base de datos
def cargar_campo_bd(nombre, score):
    '''brief: carga el nombre y score en la base de datos'''
    with sqlite3.connect("base_datos\data_base.db") as conexion:
        try:
            # sentencia = '''
            #             create table Score
            #             (
            #                 id integer primary key autoincrement,
            #                 nombre text,
            #                 puntaje integer
            #             )
            #             '''
            sentencia = '''
                        insert into Score (nombre, puntaje) values (?,?)
                        '''
            conexion.execute(sentencia, (nombre,score))
            print('cargado correctamente')
            return True 
        except Exception as e:
            print("Error al cargar el campo en la base de datos:", e)
            return False

def buscar_top_10_bd():
    '''brief: clasifica por puntaje el top 10 con mejor score'''
    with sqlite3.connect("base_datos\data_base.db") as conexion:
        try:
            cursor = conexion.cursor()
            sentencia = "SELECT nombre, puntaje FROM Score ORDER BY puntaje DESC LIMIT 10"
            cursor.execute(sentencia)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
                print("Error al buscar el top 10 en la base de datos:", e)
                return False