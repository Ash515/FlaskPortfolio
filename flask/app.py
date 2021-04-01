from flask import Flask, render_template,url_for,redirect, request, redirect
from bson import ObjectId
from  pymongo import MongoClient
import os  
app=Flask(__name__)
client=MongoClient("mongodb://127.0.0.1:27017")
db=client.myform
form=db.friends

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        name=request.values.get("name")
        email=request.values.get("email")
        message=request.values.get("message")
        form.insert({'name':name,'email':email,'message':message})
        return "<h1>sent successfully!</h1>"
if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)