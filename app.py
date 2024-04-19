from flask import Flask, request, render_template
app = Flask(__name__)

users = {"1": {"name": "Artem", "age": 13, "adress": "СПБ"},
         "2": {"name": "NeVasya", "age": 14, "adress": "Пушкин"},
         "3": {"name": "Артвас", "age": 15, "adress": "Москва"},
         "4": {"name": 'Ширик Лудоман', "age": 45, "adress": "ДОДО"}}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/<id>")
def user(id):
    if id not in users:
        return 'Пользователь не найден'
    else:
        return f'Пользователь {users[id]["name"]}, возраст: {users[id]["age"]}, город: {users[id]["adress"]}, ваш id: {id}'

@app.route("/user/all")
def all_users():
    # result = ""
    # for i in users:
    #     result += f'id:{i}, имя: {users[i]["name"]}, возраст: {users[i]["age"]}, город: {users[i]["adress"]}' + ";" 
    # return result
    n = len(users)
    return render_template("users.html", users=users, n=n)

@app.route("/user/new/")
def new_user():
    name = request.args.get("name")
    age = request.args.get("age")
    adress = request.args.get("adress")
    users[int(max(users.keys())) + 1]={"name": name, "age": age, "adress": adress} #http://127.0.0.1:5000/user/new?name=Имя&age=Возраст&adress=Город
    return "пользователь успешно добавлен!"

if __name__ == "__main__":
    app.run(debug=True)