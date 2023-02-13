from flask import Flask, render_template, request
from TuclaseExamen import TuclaseExamen

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/procesar", methods=["POST"])
def resultado():
    problemas = request.form.getlist('operaciones')
    ver_solucion = request.form.get('ver_solucion')

    obj = TuclaseExamen()

    resultado = obj.arithmetic_arranger(problemas, ver_solucion, True)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)