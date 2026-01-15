from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/albums')
def albums():
    return render_template('albums.html')

@app.route('/favoriteSongs')
def favorite_songs():
    return render_template('favorite-songs.html')


if __name__ == '__main__':
    app.run(debug=True)