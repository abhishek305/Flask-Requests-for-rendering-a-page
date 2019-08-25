import requests
import json

from flask import Flask,render_template
app=Flask(__name__)

url='https://jsonplaceholder.typicode.com/users'

req=requests.get(url)
json_form=req.json()


@app.route("/")

@app.route('/home')
def home():
    return render_template('home.html',data=json_form)

if __name__ == '__main__':
    app.run()    
    

