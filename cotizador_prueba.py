from flask import Flask, render_template, request

app = Flask(__name__)

tasas_especificas = {
    "Azuay": 0.024,
    "Bolívar": 0.024,
    "Cañar": 0.024,
    "Carchi": 0.024,
    "Chimborazo": 0.024,
    "Cotopaxi": 0.024,
    "El Oro": 0.026,
    "Esmeraldas": 0.024,
    "Galápagos": 0.024,
    "Guayas": 0.032,
    "Imbabura": 0.024,
    "Loja": 0.024,
    "Los Ríos": 0.032,
    "Manabí": 0.024,
    "Morona Santiago": 0.024,
    "Napo": 0.024,
    "Orellana": 0.024,
    "Pastaza": 0.024,
    "Pichincha": 0.034,
    "Santa Elena": 0.032,
    "Santo Domingo de los Tsáchilas": 0.024,
    "Sucumbíos": 0.024,
    "Tungurahua": 0.024,
    "Zamora Chinchipe": 0.024
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        marca_vehiculo = request.form['marca_vehiculo']
        modelo_vehiculo = request.form['modelo_vehiculo']
        anio_vehiculo = int(request.form['anio_vehiculo'])
        precio_vehiculo = float(request.form['precio_vehiculo'])
        precio_extras = float(request.form['precio_extras'])
        provincia = request.form['provincia']

        valor_total_vehiculo = precio_vehiculo + precio_extras
        tasa_provincia = tasas_especificas[provincia]
        prima_neta = valor_total_vehiculo * tasa_provincia
        superintendencia = prima_neta * 0.035
        seguro_campesino = prima_neta * 0.005
        derechos_emision = 5
        subtotal = prima_neta + superintendencia + seguro_campesino + derechos_emision
        iva = subtotal * 0.15
        prima_total = subtotal + iva

        # Calculos de pagos
        pago_descuento = prima_total * 0.95
        pago_6_meses = prima_total / 6
        pago_9_meses = prima_total / 9
        pago_12_meses = (prima_total * 1.088) / 12

        return render_template('index.html',
                               nombre_cliente=nombre_cliente,
                               marca_vehiculo=marca_vehiculo,
                               modelo_vehiculo=modelo_vehiculo,
                               anio_vehiculo=anio_vehiculo,
                               provincia=provincia,
                               valor_total_vehiculo=round(valor_total_vehiculo, 2),
                               tasa_provincia=tasa_provincia,
                               prima_neta=round(prima_neta, 2),
                               superintendencia=round(superintendencia, 2),
                               seguro_campesino=round(seguro_campesino, 2),
                               derechos_emision=round(derechos_emision, 2),
                               subtotal=round(subtotal, 2),
                               iva=round(iva, 2),
                               prima_total=round(prima_total, 2),
                               pago_descuento=round(pago_descuento, 2),
                               pago_6_meses=round(pago_6_meses, 2),
                               pago_9_meses=round(pago_9_meses, 2),
                               pago_12_meses=round(pago_12_meses, 2)
                               )
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
