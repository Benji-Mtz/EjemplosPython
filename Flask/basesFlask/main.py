from flask import Flask
# Importamos el archivo index.html asi:
from flask import render_template, request


# Para fases de desarrollo se agrega debug=True
# De esa forma el servidor esta a la escucha de errores
# Ademas se reinicia solo tipo Angular o React
app = Flask(__name__)

@app.before_request
def before_request():
    print('Antes de la peticion')

@app.after_request
def after_request(response):
    print('Después de la peticion')
    return response

# Creamos una ruta para hacer una fn
@app.route('/')
def index():
    name= 'Benji Mtz'
    course = 'Python Web'
    is_premium=False
    courses = ['Python', 'Java', 'Ruby', 'C#']

    return render_template('index.html', username=name, curso=course, is_premium=is_premium, courses=courses)

@app.route('/about')
def about():
    print('Estamos en el about')
    return render_template('about.html')

@app.route('/usuario/<last_name>/<name>/<int:age>') #strings
def usuario(last_name, name, age):
    return 'Hola: ' + last_name +' '+ name+ ' ' + str(age)

@app.route('/datos')
def datos():
    # Query strings
    nombre = request.args.get('nombre', '') #Dic
    curso = request.args.get('curso', '') #Dic
    return 'Listado de datos: ' + nombre + ' Curso: ' + curso



if __name__ == '__main__':
    app.run(debug=True, port=9000)
