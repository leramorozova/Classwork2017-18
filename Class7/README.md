### ЧТО Я ВЫНЕСЛА ИЗ СЕМИНАРА:

1. Одна функция - одна страница. В ретурн помещается текст страницы, путь в **@app.route('')**

2. **@app.route('/')** - стартовая страница

3. Нельзя создавать две страницы с одинаковым адресом, выйдет ошибка.

4. Название функции лучше = название страницы (то, что после /). Если функция hello, то адрес /.../hello (но это все не обязательно

5. Путь может содержать переменные, для их заполнения не надо вызывать функцию, можно прямо в адресе заполнять. 
Тип переменной, кроме строки, надо отдельно указывать. <int; x>

6. Формы обязательно должны содержать submit.

7. Идеальный пак импорта: **from** **flask** **import** **render** _**template,** **request,** **redirect,** **url** _**for**