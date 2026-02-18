from registros_ig import app
from flask import render_template,request,redirect
from registros_ig.models import *
from datetime import date

def validar_formulario(datos_formulario):
    hoy = str(date.today())
    if datos_formulario["quantity"] != "":
        monto_int = float(datos_formulario["quantity"])
    errores = []
    if datos_formulario["date"] > hoy:
        errores.append("La fecha no puede ser mayor a la actual")
    if datos_formulario["concept"] == "":
        errores.append("El concepto no puede ir vacio")
    if datos_formulario["quantity"] == "" or monto_int == 0:
        errores.append("El monto debe ser distinto de 0 o vacío")
    return errores

@app.route("/")
def index():
    registros = select_all()
    return render_template("index.html",datos=registros)

@app.route("/new", methods=["GET","POST"])
def create():
    if request.method == "GET":
        return render_template("create.html",dataForm={},boton="Guardar",url_post="/new")
    else:
        errores = validar_formulario(request.form)
        if errores:
            return render_template("create.html",errors=errores,dataForm=request.form,boton="Guardar",url_post="/new")
        insert([request.form ["date"],request.form ["concept"],request.form ["quantity"]])
        
        return redirect("/")

@app.route("/delete/<int:id>",methods=["GET","POST"])
def remove(id):
    if request.method == "GET":
        resultado = select_by(id)
        return render_template("delete.html", data = resultado)
    else:
        delete(id)
        return redirect("/")


@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
    if request.method == "GET":
        resultado = select_by(id)
        resultado_dic = {}
        resultado_dic["id"]= resultado[0]
        resultado_dic["date"]= resultado[1]
        resultado_dic["concept"]= resultado[2]
        resultado_dic["quantity"]= resultado[3]
        return render_template("update.html",dataForm=resultado_dic,boton="Actualizar",url_post=f"/update/{id}")
    else:
        update_by(id,[ request.form["date"],request.form["concept"],request.form["quantity"]])

        return redirect("/")