from registros_ig import ORIGIN_DATA
import sqlite3

def select_all():

    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM movements;")
    filas = res.fetchall()#datos filas
    columnas = res.description#datos columnas

    lista_diccionario=[]
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion += 1
        lista_diccionario.append(diccionario)
    con.close()
    
    return lista_diccionario
def insert(datos_form):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute("INSERT INTO movements(date,concept,quantity) VALUES(?,?,?)", datos_form)
    conexion.commit()#Valida el registro antes de guardarlo

    conexion.close()

def select_by(id):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute(f"SELECT * FROM movements WHERE id={id};")
    resultado = res.fetchall()
    return resultado[0]

def delete(id):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute(f"DELETE from movements WHERE id = {id};")
    conexion.commit()

    conexion.close()

def update_by(id,datos_form):
    conexion = sqlite3.connect(ORIGIN_DATA)
    cur = conexion.cursor()
    res = cur.execute(f"UPDATE movements SET date = ?, concept = ? , quantity = ? WHERE id ={id};", datos_form)
    conexion.commit()

    conexion.close()