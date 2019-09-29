import os
from app import app
from flask import render_template, request, redirect
#importing functions from flask
from flask_pymongo import PyMongo
# username = "Period 8"
# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"},
#         {"event":"Summer Vacation", "date": "2019-12-01"}
#     ]
#name of database
app.config['MONGO_DBNAME'] = 'test'
#URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:clustering@cluster0-gwaon.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)
#INDEX home page
@app.route('/')
@app.route('/index')
 #connection to collection inside database
def index():
    #connect to database
    collection = mongo.db.events
    #query database for all events
    events = list(collection.find({}))
    #shows html file
    return render_template('index.html', events = events)
#CONNECT TO DB, ADD DATA
@app.route('/add')
def add():
    #connect to the database
    events = mongo.db.events
    #insert new data
    test.insert({'name':'last day of school'})
    #return a message to the user
    return "Added data to database!"
@app.route('/input')
def input():
    return render_template('input.html')
#results stores data from the form
@app.route('/results', methods = ["Get", "Post"])
def results():
    #gets userdata from the form and puts data in a dictionary
    userdata = dict(request.form)
    print(userdata)
    #stores the event_name, event_date, event_type as separate variables
    event_name = userdata['event_name']
    event_date = userdata['event_date']
    event_type = userdata['event_type']
    #connecting to mogno cluster
    events = mongo.db.events
    events.insert({'name': event_name, 'date': event_date, 'type': event_type})
    ##query database for all events s
    events = list(events.find({}))
    print(events)
    #Insert the name and date of the event to Mongo events database as a dictionary
    return render_template('index.html', events = events)
#delete all page
@app.route('/delete_all')
def delete_all():
    events = mongo.db.events
    #removes all documents that match the filter from a collection
    events.delete_many({})
    return ""
