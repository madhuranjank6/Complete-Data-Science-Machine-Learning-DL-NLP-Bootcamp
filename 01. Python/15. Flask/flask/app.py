from flask import Flask

'''
The below line of  the code creates an instance of the flask class, which will be our WSGI (Web Server Gateway Interface) application
'''

## WSGI application
app = Flask(__name__) ## Creating the instance of the flask app

@app.route("/")
def welcome():
    return "Welcome to the Flask App"

@app.route("/index")
def index():
    return "Welcome to the Index Page"

## Setting the entry point of the application
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
