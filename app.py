from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/playlists')
def index():
    ''' See all playlists. '''

    return render_template('home.html', msg='Flask is cool!!')

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
