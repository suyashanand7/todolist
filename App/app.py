from flask import Flask, request, render_template
from pymongo import MongoClient 
import json
app = Flask(__name__)
connect = MongoClient('localhost',27017)
db = connect['api_data']
collection1 = db["data"]
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/display")
def disp():
    if(request.method=='GET'):
        arr=[]
        for ab in collection1.find():
            arr.append(ab)
    return render_template("display.html",output=(arr))
@app.route('/add',methods=['GET','POST'])
def add():
    return render_template("add.html")
@app.route('/AddData',methods=['POST'])
def adddata():
    name = request.form.get("job")
    des = request.form.get("desc")
    ar = {"job":name,"description":des}
    collection1.insert_one(ar)
    return render_template("index.html")
@app.route('/delete',methods=['GET','POST'])
def rem():
    return render_template("delete.html")
@app.route('/deletedata',methods=['GET','POST'])
def remdata():
    a = request.form.get("job")
    b = {"job":a}
    collection1.delete_one(b)
    return render_template("index.html")
@app.route('/update',methods=['GET','POST'])
def up():
    return render_template("update.html")
@app.route('/updata',methods=['GET','POST'])
def upd():
    old = request.form.get("job")
    ol = {"job":old}
    j = request.form.get("job2")
    d = request.form.get("desc")
    ol2 = {"job":j,"description":d}
    collection1.update_one(ol,{"$set":ol2})
    return render_template("index.html")
app.run(port=5000,host="0.0.0.0",debug=True)