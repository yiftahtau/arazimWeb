from flask import Flask, request, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'

@app.route('/', methods=['GET'])
def hello_world():
   username = request.args.get("name")
   return render_template('webPage.html', name=username)

if __name__ == '__main__':
   app.run()