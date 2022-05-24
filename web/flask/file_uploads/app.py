from flask import Flask, render_template, request
from uuid import uuid4
import pathlib
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
app.config['MAX_CONTENT_PATH'] = 100000

@app.route('/app/upload')
def upload():
    return render_template('upload.html')
	
@app.route('/api/upload_file', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        # Generate a random ID for the file name
        id = uuid4()
        # Grab the original file suffix
        extension = pathlib.Path(f.filename).suffix
        f.save('{}.{}'.format(id, extension))
        return 'file uploaded successfully'