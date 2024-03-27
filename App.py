from flask import Flask, redirect, render_template, request, send_file, url_for
from Scrapper import Scrapper
from helpers.temporizador import Temporizador

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Si la solicitud es GET, renderiza el formulario HTML
    return render_template('index.html')


@app.route('/scrap', methods=['POST'])
def run_scrapper():
    try:
        temporizador = Temporizador()
        temporizador.start()
        unScrapper = Scrapper(handlessMode=True, excelAutoName=True, seleccionarDatos=False)
        # excel_id = unScrapper.run(request.form.get('email'), request.form.get('password'))
        excel_id = unScrapper.run("abel.angel96@outlook.es", "TrabajosIt2023")
        temporizador.end()
        return send_file(excel_id, as_attachment=True)
    except Exception as e:
        # Renderiza un template de error y muestra el mensaje de error
        return render_template('error.html', error=str(e))

def pagina_no_encontrada(error):
    # Redirecciona a la página principal en caso de error 404
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Manejo de errores 404
    app.register_error_handler(404, pagina_no_encontrada)
    # Ejecución de la aplicación Flask en modo de depuración en el puerto 5000
    app.run(debug=True, port=5000)

