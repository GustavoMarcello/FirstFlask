from flask import Flask, render_template

# padrão de inicio de projeto
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/contatos/<contato_id>")
def contato_id(contato_id):
    mamada = "mamada"
    return render_template("contato.html", contato_id=mamada)


# coloca o site no ar
if __name__ == "__main__":
    app.run(debug=True)