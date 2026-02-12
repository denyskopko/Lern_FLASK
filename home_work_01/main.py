from flask import Flask
from asgiref.wsgi import WsgiToAsgi
# В задании 1 не указан путь к коротому мы обращаемся, а указана пустая строка

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return 'Hello FLASK!'


@app.route('/user/<name>')
def user(name:str):
    return  f"Hello %s!" % name

asgi = WsgiToAsgi(app)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:asgi", host='127.0.0.1', port=8050, reload=True)

