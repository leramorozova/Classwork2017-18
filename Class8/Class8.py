#на всех страницах есть кликабельная ссылка на главную и на страницу с формой.

from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)


def dict_generator():
    with open ('lang_codes.csv', 'r', encoding='UTF-8') as file:
        table=file.read()
        arr=table.split('\n')
        d={}
        for el in arr:
            if el!='':
                el=el.split(',')
                key=el[0]
                d[key]=el[1]
    return d


@app.route('/')
def main_page():
    d=dict_generator()
    return render_template('table.html', d=d, )

# если введенного языка нет в списке, пользователь попадает на страницу 127.0.0.1:5000/not_found с
# соответствующим сообщением,

@app.route('/not_found')
def not_found():
    return render_template('not_found.html')

# если зайти на страницу вида 127.0.0.1:5000/langs/какие-то_буквы, то на этой странице выведется список только тех
# языков, коды которых начинаются с этих букв. Например, если зайти на 127.0.0.1:5000/codes/jp, то выведется японский
# и еврейско-персидский, а если зайти на 127.0.0.1:5000/codes/j, то японский, еврейско-персидский, еврейско-арабский
# и яванский.

@app.route('/lang/')
def emply_letter():
    return '<html><body><p> Введите код, пожалусто. </p></body></html>'

@app.route('/lang/<letter>')
def letters(letter=None):
    found = []
    first_letter = {}
    d = dict_generator()
    if letter in d:
        for key in d:
            if d[letter][0] == d[key][0]:
                key2=key
                first_letter[key2]=0
    else:
        for key in d:
            if d[key][:len(letter)] == letter:
                found.append(key)
    if len(found) == 0 and len(first_letter) == 0:
        return redirect ('/not_found')
    elif len(first_letter)==0:
        return '''
            <html>
            <body>
            <p>Языки, код которых начинается с"''' + letter + '''":    '''\
                + ', '.join(found) + '''</p>
                <h3><a href="/form">Кстати! А вот ссылка на страницу с формой!</h3>
                    </body></html>
                    '''
    else:
        return render_template('result.html', lang=letter, code=d[letter], first_letter=first_letter)


# есть форма на странице 127.0.0.1:5000/form, в которой есть поле "Язык". В это поле пользователь будет вводить
# название языка, например "японский". Когда пользователь нажимает кнопку "Отправить",
#    - если введенного языка нет в списке, пользователь попадает на страницу 127.0.0.1:5000/not_found
#    с соответствующим сообщением,
#    - если введенный язык есть в списке, пользователь должен попасть на страницу 127.0.0.1:5000/lang/код_языка.
#    На этой странице должно выводиться следующее: название введенного языка, код введенного языка, названия всех языков,
#    код которых начинается на ту же букву.


@app.route('/form')
def form():
    d=dict_generator()
    if request.args:
        name = request.args['name']
        if name not in d:
            return redirect('/not_found')
        return redirect('lang/'+name)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)