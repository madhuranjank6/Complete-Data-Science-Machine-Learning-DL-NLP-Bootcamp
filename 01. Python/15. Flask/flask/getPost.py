from flask import Flask, render_template, request

'''
The below line of  the code creates an instance of the flask class, which will be our WSGI (Web Server Gateway Interface) application
'''

## WSGI application
app = Flask(__name__) ## Creating the instance of the flask app

@app.route("/")
def welcome():
    return """<html>
                <h1> Welcome to the Flask App </h1>
           </html>"""

@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}"
    return render_template("form.html")

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}"
    return render_template("form.html")


## Setting the entry point of the application
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
