from flask import Flask
from flask import render_template, request, redirect, url_for
app = Flask(__name__)

# Как это вообще работает

@app.route('/')
def index():
    return 'Main page'

@app.route('/hi')
def hi():
    return 'Hi!'

@app.route('/hello')
def hello():
    return '<html><body><p>Hello, world!</p></body></html>'

# Как работают переменные
# Вводить значение переменной можно прямо в строке

@app.route('/user/<user>')
def user_index(user):
    return 'This is the page of ' + user

# Надо указывать тип переменной

import datetime

@app.route('/time/<int:shift>')
def time_page(shift):
    h = datetime.datetime.today().hour
    h += shift
    return 'Time in your country:' + str(h)

#  Прикрутили к адресу шаблон
#  Получилось збс: получаем форму, если пустая, заполняем, если нет - получаем новую страницу

@app.route('/form')
def form():
    if request.args:
        name=request.args['name']
        age=request.args['age']
        pwd=request.args['pwd']
        student=True if 'student' in request.args else False
        return render_template('gratia.html', name=name, age=age, pwd=pwd, student=student)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

