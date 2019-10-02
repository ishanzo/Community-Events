from flask import *
from app import app
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/results',methods=['GET','POST'])
def shodata():
    userdata= dict(request.form)
    print(userdata)
    return render_template('results.html', name=userdata['name'][0],)

@app.route('/api_request',methods=['GET','POST'])
def api_request():
    return render_template('api_request.html')

@app.route('/api_data',methods=['GET','POST'])
def api_data():
    api_data= dict(request.form)

    return render_template('api_data.html',data=data)
