from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Nabin91438@database-2.ckbfrws7mpco.us-east-1.rds.amazonaws.com/db1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))


    def __init__(self, name, email, phone):

        self.name = name
        self.email = email
        self.phone = phone



#This is the index route where we are going to query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", trainee = all_data)


#This route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']


        my_data = Data(name, email, phone)
        db.session.add(my_data)
        db.session.commit()

        flash("Trainee Inserted Successfully")

        return redirect(url_for('Index'))


#This is our update route where we are going to update our trainee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']

        db.session.commit()
        flash("Trainee Updated Successfully")

        return redirect(url_for('Index'))

#This route is for deleting our trainee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Trainee Deleted Successfully")
    return redirect(url_for('Index'))

#from App import db
#db.create_all()
#print("DB created.")

if __name__ == "__main__":
    app.run(debug=True)