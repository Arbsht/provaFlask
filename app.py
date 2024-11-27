from flask import Flask, redirect, render_template, request, url_for

lista_spesa = []

#inizializza l'app Flask
app = Flask(__name__)

#rotta principale
@app.route('/')
def home():
    return render_template('index.html', lista_spesa = lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    print(lista_spesa)
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    lista_spesa.clear()
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)