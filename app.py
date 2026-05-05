from flask import Flask, request, jsonify, render_template
from bot import responder

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.json
    pregunta = data.get("pregunta")
    respuesta = responder(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    # IMPORTANTE: host 0.0.0.0 permite conexiones externas
    app.run(debug=True, host="0.0.0.0", port=5000)
