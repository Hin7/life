from flask import Flask
from flask import render_template

from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/')
def home():
    GameOfLife(25, 25)
    return render_template('index.html')

@app.route('/live')
def live():
    game_of_life = GameOfLife()
    game_of_life.form_new_generation()
    return render_template('live.html', game=game_of_life)

if __name__ == "__main__":
    app.run()