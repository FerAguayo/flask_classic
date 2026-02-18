from registros_ig import ORIGIN_DATA
from registros_ig.conexion import Conexion
import sqlite3

def select_all():

    connect = Conexion("SELECT * FROM movements;")
    filas = connect.res.fetchall()#datos filas
    columnas = connect.res.description#datos columnas

    lista_diccionario=[]
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion += 1
        lista_diccionario.append(diccionario)
    connect.con.close()
    
    return lista_diccionario
def insert(datos_form):
    connectInsert = Conexion("INSERT INTO movements(date,concept,quantity) VALUES(?,?,?)", datos_form)
    connectInsert.con.commit()#Valida el registro antes de guardarlo

    connectInsert.con.close()

def select_by(id):
    connectSelectBy = Conexion(f"SELECT * FROM movements WHERE id={id};")
    resultado = connectSelectBy.res.fetchall()
    return resultado[0]

def delete(id):
    connectDelete = Conexion(f"DELETE from movements WHERE id = {id};")
    connectDelete.con.commit()

    connectDelete.con.close()

def update_by(id,datos_form):
    connectUpdate = Conexion(f"UPDATE movements SET date = ?, concept = ? , quantity = ? WHERE id ={id};", datos_form)
    connectUpdate.con.commit()

    connectUpdate.con.close()