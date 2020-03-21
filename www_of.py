import subprocess
subprocess.run("systemctl start postgresql.service", shell =True)
from flask import Flask, render_template, request, flash, redirect 
from flask_sqlalchemy import SQLAlchemy
#from wtforms import  BooleanField, StringField, validators ,IntegerField
import psycopg2, psycopg2.extras
#from flask_sqlalchemy import SQLAlchemy
import time
import numpy as np
import os
import urllib.request
#from werkzeug.utils import secure_filename

from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import  Convolution2D, MaxPooling2D
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from tensorflow.python.keras import backend as K
from codes_python import ordenador
#from flask_dropzone import Dropzone
from codes_python import wwwof 

#==================================================================================================== librararis ====================================================================================================#
app_root=os.path.dirname(os.path.abspath(__file__))
app=Flask(__name__)
app.secret_key = "mysecretkey"

POSTGRES = {
    'user': 'postgres',
    'pw': '98772',
    'db': 'your db',
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
def shortcut():
	POSTGRES = psycopg2.connect(database='your db',user='postgres',password='98772', host='localhost')
	db=POSTGRES.cursor()
	
	db.execute(" SELECT * FROM __your_table__;")
	return db
#==================================================================================================== postgres shortcuts ====================================================================================================#

#replace for other files and oop or funtional pardig
#==================================================================================================== funtion in python ====================================================================================================#
@app.route("/")
def index():
	return render_template("index.html") 
@app.route("/planeacion.html")
def planeacion():
	return render_template("planeacion.html") 

@app.route("/divePC.html")
def divePC():
	return render_template("divePC.html") 
	
@app.route("/informe_de_ensayos.html")
def informe_de_ensayos():
	return render_template("informe_de_ensayos.html") 
#================================================== documentate ==================================================#

@app.route("/dibuja_acuario.html")
def dibuja_acuario():
	return render_template("wwwof_calcular_litros.html") 

@app.route("/calcupH.html")
def calcuph():
	return render_template("ph.html") 


@app.route("/bechmarck.html")
def bechmarck():
	return render_template("/bechmarck.html")
@app.route("/bechmarck/bechmarckmulticore.html")
def bechmarckmulticore():
	start = time.time()
	nm=8500
	w = wwwof.wwwof()
	result = w.matrix(-nm,nm,(nm,nm))
	finish = time.time()
	return render_template("bechmarckmulticore.html", start = start , finish = finish, reply = result)
@app.route("/bechmarck/bechmarcksinglecore.html")
def bechmarcksinglecore():
	start = time.time()
	result = 10**10**6 # not nesari import wwwof code for 1 line 
	finish = time.time()
	print(finish-start)
	return render_template("bechmarcksinglecore.html", start = start , finish = finish, reply = result)
#================================================== caculators ==================================================#

@app.route("/fish_p5js.html")
def fish_p5js():
	return render_template("fish_p5js.html") 

@app.route("/criptoforyou.html")
def criptoforyou():
	return render_template("criptoforyou.html") 


#================================================== other ==================================================#
#==================================================================================================== liltle proyects ====================================================================================================#





#boton a sub pagina para omitir el error de usuario pa que pueda medirlo cuando quiera

@app.route("/enter-a-fish.html", methods=['GET','POST'])
def enter_a_fish():
	db=shortcut()
	rows = db.fetchall() 
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
		#db.execute('INSERT INTO __your_table__  VALUES ({},{},{},{}, {},{},{},{})'.format(str(cientific_name),ph,temperature,needed_liters,large_of_fish_in_centimeters,str(fish_diet),str(fish_conduct),str(location),str(common_name)) ,(cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,location,common_name,fish_conduct))
		db.execute("INSERT INTO __your_table__(cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,fish_conduct,location,common_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s) ;" ,(str(cientific_name),ph,temperature,needed_liters,large_of_fish_in_centimeters,str(fish_diet),str(fish_conduct),str(location),str(common_name)))
		#db.execute("INSERT INTO __your_table__ VALUES (cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,fish_conduct,location,common_name) " ,(cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,fish_conduct,location,common_name))
		#db.execute('INSERT INTO __your_table__ (cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,fish_conduct,location,common_name) VALUES ({},{},{},{}, {},{},{},{})'.format(str(cientific_name),ph,temperature,needed_liters,large_of_fish_in_centimeters,str(fish_diet),str(fish_conduct),str(location),str(common_name)) ,(cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,location,common_name,fish_conduct))
		#db.execute("INSERT INTO __your_table__(cientific_name,ph,temperature,needed_liters,large_of_fish_in_centimeters,fish_diet,fish_conduct,location,common_name,) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);" ,(str(cientific_name),ph,temperature,needed_liters,large_of_fish_in_centimeters,str(fish_diet),str(fish_conduct),str(location),str(common_name)))

		db.connection.commit()
		flash('you edit that')
		
	return render_template("enter-a-fish.html", form = db, fishs=rows) 
@app.route("/enter-a-fish/delete/<string:id>", methods=['GET','POST'])
def delete(id):
	db=shortcut()
	db.execute('DELETE FROM __your_table__WHERE id = {0}'.format(id))
	db.connection.commit()
	flash('you delete that')
	return redirect("/enter-a-fish.html")
def chose_predeiction(diases):
	if diases == 0:
		sickness="prediccion:  atcado o tumor y deformidad"
	elif diases ==1 :
		sickness="prediccion: branquias "
	elif diases ==2 :
		sickness="prediccion: girodactilo "
	elif diases == 3:
		sickness="prediccion: gusano lernea "
	elif diases ==4 :
		sickness="prediccion: hidropecia "
	elif diases == 5:
		sickness="prediccion: hongos"
	elif diases ==6 :
		sickness="prediccion: huecos en la cabesa"
	elif diases == 7 :
		sickness="prediccion: ich "
	elif diases ==8 :
		sickness="prediccion: no es un pez"
	elif diases == 9:
		sickness="prediccion: ojo picho "
	elif diases == 10:
		sickness="parasito en la lengua"
	elif diases == 11:
		sickness="prediccion: podredumbre de aletas "
	elif diases == 12:
		sickness="prediccion: quemadura de bagre "
	elif diases == 13:
		sickness="prediccion: es un pez sano"
	return sickness
		
	
@app.route("/curapeces.html" , methods=['GET','POST'])

#====================================================================================================  add fish db ====================================================================================================#

def curapeces():
	import curapeces
	curapeces_class=curapeces.curapeces()
	predict=curapeces.predict()
	
	#predict=curapeces.predict()
	#curapeces_class.image()
	#curapeces_class.nn()
	#curapeces_class.save_nn()
	#predict=predict()
	#predict.display_image()
	#print(predict.predict())
	#print(predict.model)
	sickness=""
	if not sickness=="":
		sickness=""
	if not predict.pez=="":
		sickness
	if request.method == 'POST':
		#import curapeces
		#curapeces_class=curapeces.curapeces()
		file = request.files["file"]
		
		predict.pez =file
		print(predict.pez)
		prediccion=predict.predict()
		diases=prediccion
		sickness=chose_predeiction(diases)
		
		"""
		if not prediccion=="":
			prediccion=""
		if not predict.pez=="":
			prediccion"""
		
	return render_template('/curapeces.html',prediccion=sickness)#,file=file)

#==================================================================================================== curapeces ====================================================================================================#



#====================================================================================================  web executing ====================================================================================================#

if __name__=='__main__':
	app.run(debug=True)
