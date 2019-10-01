import os

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

from bson.objectid import ObjectId

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)


@app.route('/')
def playlists_index():
    ''' Show all playlists. '''
    
    return 'KILL ME PLEASE'

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
def playlists_show(playlist_id):
    ''' See one playlist. '''
    
    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_edit.html', playlist=playlist, title='Edit Playlist')


@app.route('/playlists/<playlist_id>/edit')
def playlists_edit(playlist_id):
    ''' See an edit playlist form. '''

    playlist = playlists.find_one({'_id': ObjectId(playlist_id)})
    return render_template('playlists_edit.html', playlist=playlist)

@app.route('/playlists/<playlist_id>', methods=['POST'])
def playlists_update():
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

@app.route('/playlists/<playlist_id>/delete', methods=['POST'])
def destroy():
    ''' Delete a playlist. '''

    playlists.delete_one({'_id': ObjectId(playlist_id)})
    return redirect(url_for('playlists_index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000)))
