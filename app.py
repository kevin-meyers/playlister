from flask import Flask, render_template

app = Flask(__name__)

playlists = [
    {'title': 'cat_videos', 'description': 'Cats being cats'},
    {'title': '80\'s music', 'description': 'Don\'t stop believing!'}
]

@app.route('/')
def playlists_index():
    ''' Show all playlists. '''

    return render_template('playlists_index.html', playlists=playlists)

@app.route('/playlists/new')
def new():
    ''' See new playlist form. '''

    pass

@app.route('/playlists', methods=['POST'])
def create():
    ''' Create a new playlist. '''

    pass

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
