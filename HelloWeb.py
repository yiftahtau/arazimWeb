from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   htmlFile = open('webPage.html', 'r')
   content = htmlFile.read()
   htmlFile.close()
   return content

if __name__ == '__main__':
   app.run()