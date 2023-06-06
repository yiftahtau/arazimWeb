from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'

@app.route('/', methods=['GET'])
def hello_world():
   username = request.args.get("name")
   return render_template('webPage.html', name=username)

@app.route('/newyork.jpg')
def bg_img ():
   img_file = open('upload/newyork.jpg', 'rb')
   return img_file.read()

if __name__ == '__main__':
   app.run()