import pymysql
from flask.helpers import url_for
from flask import Flask,render_template,request,redirect,flash

app = Flask(__name__)

@app.route('/')
def index():
   #return "Hello World - UNI _FIEE"
   return render_template('index.html')

@app.route("/demo")
def demo():
   return render_template("demo/index.html")

@app.route("/ventas")
def ventas():
   return render_template("paginas/ventas.html")

#if __name__=="__main__":
#   app.run(host='0.0.0.0', port=8000, debug=True)
