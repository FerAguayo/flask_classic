from registros_ig import ORIGIN_DATA
import sqlite3

class Conexion:
    def __init__(self,query_sql,parametros=[]):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(query_sql,parametros)