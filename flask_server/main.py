from re import A
from flask import Flask, jsonify, flash, request, send_from_directory
from werkzeug.utils import secure_filename
import pyjokes
from os import environ, path

UPLOAD_FOLDER = '/upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "key"
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        name = "John Doe"     
        result = {"name": name}
        return jsonify(result)
    else:
        return jsonify({'Error':"This is a GET API method"})

@app.route("/home",methods=['GET','POST'])
def home():
    if request.method=='GET': 
        msg = "You R Home"     
        result = {"message": msg}
        return jsonify(result)
    else:
        return jsonify({'Error':"This is a GET API method"})



@app.route('/user/<username>')
def show_user_profile(username):
    user = {
        "name": username,
        "email": username + "@mail.com"
    }
    return jsonify(user)

@app.route('/joke')
def get_joke():
    joke = {
        "joke": pyjokes.get_joke()
    }
    return jsonify(joke)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Upload The file with curl
# curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@test.txt"  http://localhost:8080/uploadfile
@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return jsonify({"error": "no File Uploaded"})

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return jsonify({"error": "No File Selected"})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({
                "upload": True,
                "filename": filename
            })
            

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'], path=filename, as_attachment=True)




if __name__ == '__main__':
    debug = False
    if environ.get('DEBUG') is not None and environ.get('DEBUG') == "True":
        debug = True

    app.run(debug=debug, host='0.0.0.0', port=8080)
