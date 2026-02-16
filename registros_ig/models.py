import sqlite3

def select_all():

    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM movements;")
    filas = res.fetchall()
    columnas = res.description

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
 