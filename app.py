from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

from bson.objectid import ObjectId

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

    return render_template('playlists_new.html', playlist={}, title='New Playlist')

@app.route('/playlists', methods=['POST'])
def create():
    ''' Create a new playlist. '''

    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlist_id = playlists.insert_one(playlist).instered_id
    return redirect(url_for('playlists_show', playlist_id=playlist_id))

@app.route('/playlists/<playlist_id>')
def show(playlist_id):
    ''' See one playlist. '''
    
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_edit.html', playlist=playlist, title='Edit Playlist')


@app.route('/playlists/<playlist_id>/edit')
def edit(playlist_id):
    ''' See an edit playlist form. '''

    paylist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_edit.html', playlist=playlist)

@app.route('/playlists/<playlist_id>', methods=['POST'])
def update():
    ''' Update a playlist. '''

    updated_playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.update_one(
        {'_id': ObjectId(playlist_id)},
        {'$set': updated_playlist}
    )

    return redirect(url_for('playlists_show', playlist_id=playlist_id))

@app.route('/playlists/:id', methods=['DELETE'])
def destroy():
    ''' Delete a playlist. '''

    pass


if __name__ == '__main__':
    app.run(debug=True)
