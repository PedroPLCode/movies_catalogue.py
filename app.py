from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return render_template("homepage.html", movies=list(range(0, 4)))

if __name__ == '__main__':
    app.run(debug=True)