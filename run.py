from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    

    '''
    <abrir fichero> #Recordar como se manejaban ficheros csv
    <mientras haya registros>
        registro = leerFichero
        registro. separar.por comas
        procesar ventas totales y beneficios totales

    Montar respuesta
    devolver respuesta.
    '''
