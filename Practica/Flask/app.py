from flask import Flask, jsonify

app = Flask(__name__)

# Ruta básica que devuelve una lista de números
@app.route('/numeros', methods=['GET'])
def obtener_numeros():
    # Crear una lista de números del 1 al 10 (puedes personalizarla)
    numeros = list(range(1, 11))  # [1, 2, 3, ..., 10]
    
    # Devolver la lista como respuesta JSON
    return jsonify(numeros)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  
