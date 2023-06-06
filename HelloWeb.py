from flask import Flask, request
from jinja2 import Environment, PackageLoader, select_autoescape
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
   username = request.args.get("name")
   if username == None:
      htmlFile = open('loginPage.html', 'r')
      content = htmlFile.read()
      htmlFile.close()
      return content
   helloPage = open('webPage.html', 'r')
   content = helloPage.read()
   environment = Environment()
   template = environment.from_string(content)
   return template.render(name=username)

if __name__ == '__main__':
   app.run()