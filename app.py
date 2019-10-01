from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)


@app.route('/')
def playlists_index():
    ''' Show all playlists. '''

    return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def new():
    ''' See new playlist form. '''
    return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def create():
    ''' Create a new playlist. '''

    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))turn redirect(url_for('playlists_index'))

@app.route('/playlists/:id')
def show():
    ''' See one playlist. '''

    pass

@app.route('/playlists/:id/edit')
def edit():
    ''' See an edit playlist form. '''

    pass

@app.route('/playlists/:id', methods=['PATCH', 'PUT'])
def update():
    ''' Update a playlist. '''

    pass

@app.route('/playlists/:id', methods=['DELETE'])
def destroy():
    ''' Delete a playlist. '''

    pass


if __name__ == '__main__':
    app.run(debug=True)
