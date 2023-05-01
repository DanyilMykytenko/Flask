from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def index():
    films = get_films()
    return render_template('hello.html', films=films, title="check")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<string:name>')
def greetings(name:str):
    return f'Hello, {name}'

def get_films():
    return [
        {
            'id': 1,
            'title': 'Harry Potnyi'
        },
        {
            'id': 2,
            'title': 'Jarenyi soup'
        }
    ]

if __name__ == '__main__':
    app.run()