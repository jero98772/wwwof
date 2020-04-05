import subprocess
subprocess.run("systemctl start postgresql.service", shell =True)
from flask import Flask, render_template, request, flash, redirect 
from flask_sqlalchemy import SQLAlchemy
#from wtforms import  BooleanField, StringField, validators ,IntegerField
import psycopg2, psycopg2.extras
from psycopg2.extensions import AsIs
#from flask_sqlalchemy import SQLAlchemy
import time
import numpy as np
import os
import urllib.request
import cv2
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
    'pw': '8_>370',
    'db': 'wwwofish',
    'host': 'localhost',
    'port': '5000',
}

app.config['SQLAlchemy_DATABASE_URI'] =  POSTGRES
db=SQLAlchemy(app)
def selctimg(rows,imgdir):
	img = ""
	count = 0
	for elements in range(43):#number of items in db
		for i in rows:
			while count <  len(os.listdir(imgdir))+1 and  i == imgdir+str(count):
				#print("\n"*3,i,count,"\n"*3)
				img = os.path.join(imgdir+str(count))
				#img = count
				#img = str(imgdir+str(count))

				break

		count +=1 
	return [img ,count]
def shortcut():
	POSTGRES = psycopg2.connect(database='wwwofish',user='postgres',password='8_>370', host='localhost')
	db=POSTGRES.cursor()
	
	db.execute(" SELECT * FROM wwwoftable4;")
	return db

#==================================================================================================== postgres shortcuts ====================================================================================================#

#replace for other files and oop or funtional pardig
#==================================================================================================== funtion in python ====================================================================================================#
@app.route("/")
def index():
	return render_template("index.html") 
@app.route("/planeacion.html")
def planeacion():
	return render_template("planeacion_y_informes/planeacion.html") 

@app.route("/divePC.html")
def divePC():
	return render_template("divePC.html") 
	
@app.route("/informe_de_ensayos.html")
def informe_de_ensayos():
	return render_template("planeacion_y_informes/informe_de_ensayos.html")

@app.route("/tecnologias.html") 
def tecnologias():
	return render_template("planeacion_y_informes/tecnologiasmap.html")

@app.route("/valores.html") 
def valores():
	return render_template("planeacion_y_informes/valores.html")
#================================================== documentate ==================================================#

@app.route("/drawFISHTANK.html")
def drawFISHTANK():
	return render_template("drawFISHTANK/drawFISHTANK.html") 

@app.route("/calcupH.html")
def calcuph():
	return render_template("ph.html") 


@app.route("/bechmarck.html")
def bechmarck():
	return render_template("bechmarck/bechmarck.html")

@app.route("/bechmarck/bechmarckmulticore.html")
def bechmarckmulticore():
	start = time.time()
	nm=8500
	w = wwwof.wwwof()
	result = w.matrix(-nm,nm,(nm,nm))
	finish = time.time()
	return render_template("bechmarck/bechmarckmulticore.html", start = start , finish = finish, reply = result)

@app.route("/bechmarck/bechmarcksinglecore.html")
def bechmarcksinglecore():
	start = time.time()
	result = 10**10**6 # not nesari import wwwof code for 1 line 
	finish = time.time()
	print(finish-start)
	return render_template("bechmarck/bechmarcksinglecore.html", start = start , finish = finish, reply = result)
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


@app.route("/data_basecsv.html", methods=['GET','POST'])
def data_basecsv():
	imgepath = []
	db = shortcut()
	rows = db.fetchall() 
	imgdir = "./static/img/saved_db_img/"
	if request.method == 'POST':
#=================== name STRINGS ===================#
		scientific_name = str(request.form["scientific_name"])
		common_name = str(request.form["common_name"])
#=================== FLOATS of  environment ===================#
		minph = float(request.form["minph"]) 
		maxph = float(request.form["maxph"])

		mingh = float(request.form["mingh"]) 
		maxgh = float(request.form["maxgh"])

		mintemperature = float(request.form["mintemperature"])
		maxtemperature = float(request.form["maxtemperature"])

#=================== FLOATS of  fish ===================#

		weight = float(request.form["weight"])
		large_of_fish_in_centimeters = float(request.form["large_of_fish_in_centimeters"])
		
#=================== FLOATS for  fish ===================#
		
		needed_liters = float(request.form["needed_liters"])
		recommended_filtering = needed_liters*5
		#recommended_filtering = float(request.form["recommended_filtering"])

#=================== STRINGS for  fish ===================#

		eats = str(request.form["eats"])
		can_eat = str(request.form["can_eat"])
		
		reproduction = str(request.form["reproduction"])
		kill = str(request.form["kill"])

		
		breathing = str(request.form["breathing"])
		#print("\n"*3,breathing)
		if breathing == "fresh water and Anabantoidei":
			water = "fresh water"
			#print(water)
		if breathing == "fresh water":
			water = "fresh water"
			#print(water)
		if breathing == "breathing in the sea":
			water = "salt water"
			#print(water)
		mouth = str(request.form["mouth"])

#=================== STRINGS for  Location ===================#

		latitude = str(request.form["latitude"])
		longitude = str(request.form["longitude"])

		country = str(request.form["country"])
		state = str(request.form["state"])

		city = str(request.form["city"])
		waterenv = str(request.form["waterenv"])

#=================== STRINGS for  fish behavior ===================#
		
		temperament = str(request.form["temperament"])
		behavior = str(request.form["behavior"])

		swimming_zone = str(request.form["swimming_zone"])
		vel = str(request.form["vel"])

		light = str(request.form["light"])
		gravel = str(request.form["gravel"])

#=================== STRINGS for  fish ecosistem ===================#


		habitats = str(request.form["habitats"])
		habits = str(request.form["habits"])

		structural = str(request.form["structuralshape"])
		ornaments = str(request.form["ornaments"])

		ecosistem = str(request.form["ecosistem"])

		withpalnts = str(request.form["withpalnts"])
		if withpalnts =="'yes'":
			withpalnts = "can live with aquatic plants"
		elif withpalnts =="'no'":
			withpalnts = "cant live with aquatic plants"
		forms_surroundings = str(request.form.get("forms_surroundings"))

#=================== STRINGS for  GENERAL INFORMATION  ===================#

		description = str(request.form["description"])
		photo = request.files["photo"]

#=================== DB READ PHOTO   ===================#

		#print("\n"*2,photo ,"\n"*2)

		#print("\n"*2,photo ,"\n"*2)
		photoname1 = str(photo).replace("<FileStorage: '","")
		photoname1 = str(photoname1).replace("' ('image/jpeg')>","")
		photoname1 = str(photoname1).replace("' ('image/png')>","")
		photoname1 = str(photoname1).replace("' ('image/jpg')>","")
		#print("\n"*2,photoname1 ,"\n"*2)
		photo.save(imgdir+photoname1)
		photo = photoname1
		photoname2 = str(len(os.listdir(imgdir)))
		photoname = imgdir+photoname2
		photonameid = imgdir+photoname2 +scientific_name
		os.rename(imgdir+photoname1,photoname)
		counter = 0
		while counter <  len(os.listdir(imgdir)):
			imgepath.append(os.path.join(imgdir+str(counter)))
			#print("\n"*3,counter,"\n",imgepath)
			counter +=1
		#photoimg = cv2.imread(photo)
		#cv2.imwrite(imgdir+photoname,photoimg)


#=================== put in db ===================#
		waterforce = recommended_filtering

		fishdata = [scientific_name ,common_name ,minph  ,maxph  ,mingh  ,maxgh  ,mintemperature ,maxtemperature  ,weight  ,large_of_fish_in_centimeters ,needed_liters  ,recommended_filtering  ,eats   ,can_eat  ,reproduction ,kill ,breathing ,mouth ,latitude  ,longitude  , country  , state   ,city      ,waterenv  ,temperament ,behavior ,swimming_zone  ,vel , light  ,gravel ,habitats, habits   ,structural  , ornaments ,waterforce , ecosistem ,withpalnts ,forms_surroundings, photo ,description , water  ,photoname ]

		fishdatastr = ["scientific_name" ,"common_name" ,"minph"  ,"maxph"  ,"mingh"  ,"maxgh"  ,"mintemperature" ,"maxtemperature"  ,"weight"  ,"large_of_fish_in_centimeters" ,"needed_liters"  ,"recommended_filtering  ","eats"   ,"can_eat"  ,"reproduction" ,"kill ","breathing" ,"mouth ","latitude  ","longitude  ", "country"  , "state"   ,"city      ","waterenv  ","temperament ","behavior ","swimming_zone"  ,"vel ", "light  ","gravel ","habitats", "habits"   ,"structural  ", "ornaments ","waterforce" , "ecosistem" ,"withpalnts ","forms_surroundings ","photo" ,"description ", "water " ,"photoname",]
		
		strfishatributes = ""
		count = 0
		for i in fishdatastr:
			if len(fishdatastr)-1 == count:
				strfishatributes += i
			else:
				strfishatributes += i +","
			count +=1

		#print(strfishatributes)

		db.connection.cursor()
		db.execute(" INSERT INTO wwwoftable4 ( {} ) VALUES {};".format(strfishatributes,tuple(fishdata)))

		#db.execute(" INSERT INTO wwwoftable4(scientific_name ,common_name ,minph  ,maxph  ,mingh  ,maxgh  ,mintemperature ,maxtemperature  ,weight  ,large_of_fish_in_centimeters ,needed_liters  ,recommended_filtering  ,eats   ,can_eat  ,reproduction ,kill ,breathing ,mouth ,latitude  ,longitude  , country  , state   ,city      ,waterenv  ,temperament ,behavior ,swimming_zone  ,vel , light  ,gravel ,habitats, habits   ,structural  , ornaments ,waterforce , ecosistem ,withpalnts ,forms_surroundings ,photo ,description , water  ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s );",(scientific_name ,common_name ,minph  ,maxph  ,mingh  ,maxgh  ,mintemperature ,maxtemperature  ,weight  ,large_of_fish_in_centimeters ,needed_liters  ,recommended_filtering  ,eats   ,can_eat  ,reproduction ,kill ,breathing ,mouth ,latitude  ,longitude  , country  , state   ,city      ,waterenv  ,temperament ,behavior ,swimming_zone  ,vel , light  ,gravel ,habitats , habits   ,structural  , ornaments ,waterforce , ecosistem ,withpalnts ,forms_surroundings ,photo ,description , water ))


		db.connection.commit()
		#flash('you edit that')
		#print(imgepath,2*"\n")
	return render_template("data_basecsv/data_basecsv.html", form = db, fishes=rows ,imgs =imgepath) 
@app.route("/data_basecsv/delete/<string:id>", methods = ['GET','POST'])
def delete(id):
	db=shortcut()
	db.execute('DELETE FROM wwwoftable4 WHERE id = {0}'.format(id))
	db.connection.commit()
	flash('you delete that')
	return redirect("/data_basecsv.html")




@app.route('/data_basecsv/actualisar<string:id>', methods = ['GET','POST'])
def update_fish(id):
	db = shortcut()
	imgdir = "./static/img/saved_db_img/"
	rows = db.fetchall() 
	imgepath = []
	if request.method == 'POST':
#=================== name STRINGS ===================#
		scientific_name = str(request.form["scientific_name"])
		common_name = str(request.form["common_name"])
#=================== FLOATS of  environment ===================#
		minph = float(request.form["minph"]) 
		maxph = float(request.form["maxph"])

		mingh = float(request.form["mingh"]) 
		maxgh = float(request.form["maxgh"])

		mintemperature = float(request.form["mintemperature"])
		maxtemperature = float(request.form["maxtemperature"])

#=================== FLOATS of  fish ===================#

		weight = float(request.form["weight"])
		large_of_fish_in_centimeters = float(request.form["large_of_fish_in_centimeters"])
		
#=================== FLOATS for  fish ===================#
		
		needed_liters = float(request.form["needed_liters"])
		recommended_filtering = needed_liters*5
		#recommended_filtering = float(request.form["recommended_filtering"])

#=================== STRINGS for  fish ===================#

		eats = str(request.form["eats"])
		can_eat = str(request.form["can_eat"])
		
		reproduction = str(request.form["reproduction"])
		kill = str(request.form["kill"])

		
		breathing = str(request.form["breathing"])
		#print("\n"*3,breathing)
		if breathing == "fresh water and Anabantoidei":
			water = "fresh water"
			#print(water)
		if breathing == "fresh water":
			water = "fresh water"
			#print(water)
		if breathing == "breathing in the sea":
			water = "salt water"
			#print(water)
		mouth = str(request.form["mouth"])

#=================== STRINGS for  Location ===================#

		latitude = str(request.form["latitude"])
		longitude = str(request.form["longitude"])

		country = str(request.form["country"])
		state = str(request.form["state"])

		city = str(request.form["city"])
		waterenv = str(request.form["waterenv"])

#=================== STRINGS for  fish behavior ===================#
		
		temperament = str(request.form["temperament"])
		behavior = str(request.form["behavior"])

		swimming_zone = str(request.form["swimming_zone"])
		vel = str(request.form["vel"])

		light = str(request.form["light"])
		gravel = str(request.form["gravel"])

#=================== STRINGS for  fish ecosistem ===================#


		habitats = str(request.form["habitats"])
		habits = str(request.form["habits"])

		structural = str(request.form["structuralshape"])
		ornaments = str(request.form["ornaments"])

		ecosistem = str(request.form["ecosistem"])

		withpalnts = str(request.form["withpalnts"])
		if withpalnts =="'yes'":
			withpalnts = "can live with aquatic plants"
		elif withpalnts =="'no'":
			withpalnts = "cant live with aquatic plants"
		forms_surroundings = str(request.form.get("forms_surroundings"))

#=================== STRINGS for  GENERAL INFORMATION  ===================#

		description = str(request.form["description"])
		#photo = request.files["photo"]

#=================== DB READ PHOTO   ===================#

#take the previous image
		print(photo)
		image  = selctimg(rows[0],imgdir)
		name = image[1]
		img = image[0]
		print("\n"*2,img ,"\n"*2,name)
		#print("\n"*2,photo ,"\n"*2)
		photoname1 = str(photo).replace("<FileStorage: '","")
		photoname1 = str(photoname1).replace("' ('image/jpeg')>","")
		photoname1 = str(photoname1).replace("' ('image/png')>","")
		photoname1 = str(photoname1).replace("' ('image/jpg')>","")
		#remove

		photo.save(photoname1)
		photo = photoname1
		photoname2 = str(len(os.listdir(imgdir))+1)
		photoname = imgdir+photoname2
		photonameid = imgdir+photoname2 +scientific_name
		os.rename(imgdir+photoname1,photoname)


		name = imgdir + name
		os.rename(photoname,name)
#=================== put in db ===================#
		waterforce = recommended_filtering

		fishdata = [scientific_name ,common_name ,minph  ,maxph  ,mingh  ,maxgh  ,mintemperature ,maxtemperature  ,weight  ,large_of_fish_in_centimeters ,needed_liters  ,recommended_filtering  ,eats   ,can_eat  ,reproduction ,kill ,breathing ,mouth ,latitude  ,longitude  , country  , state   ,city      ,waterenv  ,temperament ,behavior ,swimming_zone  ,vel , light  ,gravel ,habitats, habits   ,structural  , ornaments ,waterforce , ecosistem ,withpalnts ,forms_surroundings, photo ,description , water  ,photoname ]

		fishdatastr = ["scientific_name" ,"common_name" ,"minph"  ,"maxph"  ,"mingh"  ,"maxgh"  ,"mintemperature" ,"maxtemperature"  ,"weight"  ,"large_of_fish_in_centimeters" ,"needed_liters"  ,"recommended_filtering  ","eats"   ,"can_eat"  ,"reproduction" ,"kill ","breathing" ,"mouth ","latitude  ","longitude  ", "country"  , "state"   ,"city      ","waterenv  ","temperament ","behavior ","swimming_zone"  ,"vel ", "light  ","gravel ","habitats", "habits"   ,"structural  ", "ornaments ","waterforce" , "ecosistem" ,"withpalnts ","forms_surroundings ","photo" ,"description ", "water " ,"photoname",]
		
		strfishatributes = ""
		count = 0
		for i in fishdatastr:
			if len(fishdatastr)-1 == count:
				strfishatributes += i
			else:
				strfishatributes += i +","
			count +=1

		db = db.connection.cursor()

		fishdatalist = []
		for j in fishdata:
			for i in fishdatastr:
				if len(fishdatastr)-1 == count:
					strfishatributes += str(i)+"={}".format(j)
				else:
					strfishatributes += str(i)+"%s".format(j)+","
				count +=1
		"""
		for i in fishdatastr:
			for j in fishdata:
				if len(fishdatalist)-1 == count:
					fishdatalist.append(i)
					fishdatalist.append(j)
				else:
					fishdatalist.append(i +",") 
				count +=1 """
		#db.execute("UPDATE wwwoftable4 SET scientific_name = %s,ph = %s, temperature = %s, large_of_fish_in_centimeters = %s,needed_liters = %s, fish_diet = %s , fish_conduct= %s,location = %s, common_name = %s WHERE id = %s ;", (str(scientific_name),ph,temperature,needed_liters,large_of_fish_in_centimeters,str(fish_diet),str(fish_conduct),str(location),str(common_name),id))

		for indb in fishdatastr:
			db.execute("UPDATE wwwoftable4 SET {} WHERE id = {} ;".format(indb, id))
		flash(' Updated Successfully')
		db.connection.commit()

		return redirect('/data_basecsv.html')


@app.route('/data_basecsv/<string:id>', methods = ['POST', 'GET'])
def get_fish(id):
	#imgchange = ""
	img = ""
	count = 0
	imgdir = "./static/img/saved_db_img/"
	imgepath = []
	db = shortcut()
	db.connection.cursor()
	db.execute('SELECT * FROM wwwoftable4 WHERE id = {}'.format(id))
	rows = db.fetchall()
	img = selctimg(rows[0],imgdir)
	img = img[0]
	"""
	for elements in range(43):#number of items in db
		for i in rows[0]:
			while count <  len(os.listdir(imgdir))+1 and  i == imgdir+str(count):
				print("\n"*3,i,count,"\n"*3)
				img = os.path.join(imgdir+str(count))
				#img = count
				#img = str(imgdir+str(count))

				break

		count +=1 
	"""

	db.close()
	return render_template('data_basecsv/updatefish.html', fish = rows[0],image = img)#, imgpath=imgchange)

#====================================================================================================  add fish db ====================================================================================================#
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
def curapeces():
	import curapeces
	curapeces_class=curapeces.curapeces()
	predict = curapeces.predict()
	predict2 = curapeces.predict()
	#predict2 = curapeces.predict()
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

		file = request.files["file"]
		#print(file)
		
		predict.pez = file
		#print(predict.pez)
		predict.numfolders = 3
		prediccion = predict.predict()
		diases = prediccion
		sickness0 = chose_predeiction(diases)

		predict2.pez = file
		predict2.numfolders = 2
		#print(predict2.pez)
		prediccion2 = predict2.predict()
		diases2 = prediccion2
		sickness2 = chose_predeiction(diases2)

		if sickness0 == sickness2 :
			sickness = sickness0
		else :
			sickness = "/static/img/prediccionerror.jpg"	
	return render_template('/curapeces.html',prediccion=sickness)#,file=file)

#==================================================================================================== curapeces ====================================================================================================#


#====================================================================================================  web executing ====================================================================================================#

if __name__=='__main__':
	app.run(debug=True)
