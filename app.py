from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = ['raz', 'dwa', 'trzy']
    return render_template("homepage.html", movies=movies) #range() ?

if __name__ == '__main__':
    app.run(debug=True)