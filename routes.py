from flask import Flask 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/flask')
def flak():
    return "Hi Flask!"

@app.route('/say/michael')
def michael():
    return "Hi Michael!"

@app.route('/say/john')
def john():
    return "Hi John!"

@app.route('/repeat/<id>/<item>')
def hello(id,item):
    id=int(id)
    return item *id 

if __name__=="__main__":
    app.run(debug=True)
