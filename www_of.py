from flask import Flask, render_template,request, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import  BooleanField, StringField, validators ,IntegerField

#from flask_table import Table, Col
import psycopg2, psycopg2.extras

app=Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
    'user': 'postgres',
    'pw': 'your password here',
    'db': 'your database here',
    'host': 'localhost',
    'port': '5000',
}

app.config['SQLAlchemy_DATABASE_URI'] =  POSTGRES
db=SQLAlchemy(app)
cientific_name = db.Column(db.String(100))
ph = db.Column(db.Integer, primary_key = True)
temperature = db.Column(db.Integer, primary_key = True)
needed_liters= db.Column(db.Integer, unique=True)
large_of_fish_in_centimeters= db.Column(db.Integer, unique=True)
fish_diet = db.Column(db.String(20), unique=True)
fish_conduct = db.Column(db.String(20))
common_name = db.Column(db.String(50))

@app.route("/")
def index():
	return render_template("index.html") 

@app.route("/dibuja_acuario.html")
def dibuja_acuario():
	return render_template("wwwof_calcular_litros.html") 

@app.route("/calcupH.html")
def calcuph():
	return render_template("ph.html") 

@app.route("/enter-a-fish.html", methods=['GET','POST'])
def enter_a_fish():
	POSTGRES = psycopg2.connect(database='wwwofish',user='postgres',password='98772', host='localhost')

	db=POSTGRES.cursor()
	db.execute(" SELECT * FROM you_table_here ;")
	rows = db.fetchall() #data from database
	print(rows)



	if request.method == 'POST':
		cientific_name=str(request.form["cientific_name"])
		ph=int(request.form["ph"])
		temperature=int(request.form["temperature"])
		needed_liters=int(request.form["needed_liters"])
		large_of_fish_in_centimeters=int(request.form["large_of_fish_in_centimeters"])
		fish_diet=str(request.form["fish_diet"])
		location=str(request.form["location"])
		common_name=str(request.form["common_name"])
		fish_conduct=str(request.form["fish_conduct"])
		db.execute("INSERT INTO you_table_here (cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,fish_conduct,location,common_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s) ;" ,(str(cientific_name),ph,temperature,needed_liters,large_of_fish_in_centimeters,str(fish_diet),str(fish_conduct),str(location),str(common_name)))
		
		db.connection.commit()
		
	return render_template("enter-a-fish.html", form = db, fishes=rows) 

if __name__=='__main__':
	app.run(debug=True)