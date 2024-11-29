from flask import Flask, render_template
from services.binance import data_cripto



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Rommel", message="¡Bienvenido a Flask!")

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cripto', methods=['GET'])
def lista_cripto():
    # Llama a la función que obtiene los datos de Binance
    data = data_cripto()
    return render_template('data_cripto.html', data_cripto=data)

if __name__ == '__main__':
    app.run(debug=True)
