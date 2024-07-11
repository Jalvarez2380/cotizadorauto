from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cotizar', methods=['POST'])
def cotizar():
    nombre = request.form['nombre']
    marca = request.form['marca']
    modelo = request.form['modelo']
    anio = request.form['anio']
    precio = float(request.form['precio'])
    extras = float(request.form['extras'])
    provincia = request.form['provincia']

    valor_total = precio + extras

    if provincia == 'Azuay':
        tasa = 0.03
    elif provincia == 'Cañar':
        tasa = 0.025
    elif provincia == 'Guayas':
        tasa = 0.028
    else:
        tasa = 0.03

    prima_neta = valor_total * tasa
    supercias = prima_neta * 0.035
    seguro_campesino = prima_neta * 0.005
    derechos_emision = 5
    subtotal = prima_neta + supercias + seguro_campesino + derechos_emision
    iva = subtotal * 0.12
    prima_total = subtotal + iva

    pago_descuento = prima_total * 0.95
    pago_6_meses = prima_total / 6
    pago_9_meses = prima_total / 9
    pago_12_meses = (prima_total * 1.088) / 12

    return render_template('index.html',
                           prima_neta=round(prima_neta, 2),
                           supercias=round(supercias, 2),
                           seguro_campesino=round(seguro_campesino, 2),
                           derechos_emision=round(derechos_emision, 2),
                           subtotal=round(subtotal, 2),
                           iva=round(iva, 2),
                           prima_total=round(prima_total, 2),
                           pago_descuento=round(pago_descuento, 2),
                           pago_6_meses=round(pago_6_meses, 2),
                           pago_9_meses=round(pago_9_meses, 2),
                           pago_12_meses=round(pago_12_meses, 2))

if __name__ == '__main__':
    app.run(debug=True)
