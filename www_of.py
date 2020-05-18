import subprocess
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
import sqlite3
#==================================================================================================== librararis ====================================================================================================#

app=Flask(__name__)
app.secret_key = "mysecretkey"
"""
POSTGRES = {
    'user': 'postgres',
    'db': 'wwwofish',
    'host': 'localhost',
    'port': '5000',
}

app.config['SQLAlchemy_DATABASE_URI'] =  POSTGRES"""
app.config['SECRET_KEY']
db=SQLAlchemy(app)
def p(*args):
	for i in args:
		print("\n"*2,i,"\n"*2)

def selctimg(rows,imgdir,id):
	img = ""
	imgs =[]
	count = 0
	col = 0
	for elements in range(len(os.listdir(imgdir))):#number of items in db
		for i in rows:
			while count <  len(os.listdir(imgdir)) and  i == imgdir+str(count):
				img = os.path.join(imgdir+str(count)) 
			if col == len(rows):
				p(col)
				photoname = i
				p(photoname)
			col +=1
			p(i)
		count +=1 
		imgs.append(count)
	return [img ,count,imgs,photoname]
def shortcut():
	#try:
	#	POSTGRES = psycopg2.connect(database='wwwofish',user='postgres',password='8_>370', host='localhost')
	#except:
	#	subprocess.run("systemctl start postgresql.service", shell =True)
	#db=POSTGRES.cursor()
	connection = sqlite3.connect('wwwofish')
	db = connection.cursor()
	db.execute(" SELECT * FROM wwwoftable4;")
	return db
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
		
#==================================================================================================== postgres shortcuts ====================================================================================================#

#replace for other files and oop or funtional pardig
#==================================================================================================== funtion in python ====================================================================================================#

webpage = "/www_of"
@app.route(webpage+"/")
def index():
	return render_template("www_of/index.html") 
@app.route(webpage+"/donacionbtc.html")
def donacionbtc():
	return render_template("www_of/essential/donacionbtc.html")
@app.route(webpage+"/planeacion.html")
def planeacion():
	return render_template("www_of/planeacion_y_informes/planeacion.html") 

@app.route(webpage+"/divePC.html")
def divePC():
	return render_template("www_of/divePC.html") 
	
@app.route(webpage+"/informe_de_ensayos.html")
def informe_de_ensayos():
	return render_template("www_of/planeacion_y_informes/informe_de_ensayos.html")

@app.route(webpage+"/tecnologias.html") 
def tecnologias():
	return render_template("www_of/planeacion_y_informes/tecnologiasmap.html")

@app.route(webpage+"/valores.html") 
def valores():
	return render_template("www_of/planeacion_y_informes/valores.html")
#================================================== documentate ==================================================#

@app.route(webpage+"/drawFISHTANK.html")
def drawFISHTANK():
	return render_template("www_of/drawFISHTANK/drawFISHTANK.html") 

@app.route(webpage+"/calcupH.html")
def calcuph():
	return render_template("www_of/ph.html") 


#================================================== howproyects ==================================================#
howproyects = "/howproyects"
@app.route(webpage+howproyects+"/howcalcupH.html")
def howcalcuph():
	return render_template("www_of"+howproyects+"/howcalcupH_js.html") 
@app.route(webpage+howproyects+"/howdrawFISHTANK.html")
def howdrawfishtank():
	return render_template("www_of"+howproyects+"/howDrawfishtank.html") 
@app.route(webpage+howproyects+"/howcurapeces.html")
def howcurapeces():
	return render_template("www_of"+howproyects+"/howcurapeces.html") 
@app.route(webpage+howproyects+"/howfishdb.html")
def howfishdb():
	return render_template("www_of"+howproyects+"/howfishdb.html") 

#================================================== caculators ==================================================#

@app.route(webpage+"/fish_p5js.html")
def fish_p5js():
	return render_template("www_of/fish_p5js.html") 
	#little ornament for page

#================================================== other ==================================================#
#==================================================================================================== liltle proyects ====================================================================================================#
#boton a sub pagina para omitir el error de usuario pa que pueda medirlo cuando quiera


@app.route(webpage+"/data_basecsv.html", methods=['GET','POST'])
def data_basecsv():

	imgepath = []
	db = shortcut()
	db.execute(" SELECT * FROM wwwoftable4;")
	rows = db.fetchall()
	imgdir = "./static/"+webpage+"/img/saved_db_img/"
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
		photoname2 = str(len(os.listdir(imgdir)))
		photoname = str(imgdir+photoname2)
		photonameid = imgdir+photoname2 +scientific_name
		os.rename(imgdir+photoname1,photoname)
		counter = 0
		while counter <  len(os.listdir(imgdir)):
			imgepath.append(os.path.join(imgdir+str(counter)))
			#print("\n"*3,counter,"\n",imgepath)
			counter +=1
		#photoimg = cv2.imread(photo)
		#cv2.imwrite(imgdir+photoname,photoimg)
		photo = photoname #this for return name in case to serarch
		file = photo# this for return file
		

#=================== put in db ===================#
		waterforce = recommended_filtering

		fishdata = [scientific_name ,common_name ,minph  ,maxph  ,mingh  ,maxgh  ,mintemperature ,maxtemperature  ,weight  ,large_of_fish_in_centimeters ,needed_liters  ,recommended_filtering  ,eats   ,can_eat  ,reproduction ,kill ,breathing ,mouth ,latitude  ,longitude  , country  , state   ,city      ,waterenv  ,temperament ,behavior ,swimming_zone  ,vel , light  ,gravel ,habitats, habits   ,structural  , ornaments ,waterforce , ecosistem ,withpalnts ,forms_surroundings, photo ,description , water  ,photoname ]

		fishdatastr = ["scientific_name" ,"common_name" ,"minph"  ,"maxph"  ,"mingh"  ,"maxgh"  ,"mintemperature" ,"maxtemperature"  ,"weight"  ,"large_of_fish_in_centimeters" ,"needed_liters"  ,"recommended_filtering  ","eats"   ,"can_eat"  ,"reproduction" ,"kill ","breathing" ,"mouth ","latitude  ","longitude  ", "country"  , "state"   ,"city      ","waterenv  ","temperament ","behavior ","swimming_zone"  ,"vel ", "light  ","gravel ","habitats", "habits"   ,"structural  ", "ornaments ","waterforce" , "ecosistem" ,"withpalnts ","forms_surroundings ","photo" ,"description ", "water " ,"photoname"]
		
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
		db.close()

	return render_template("www_of/data_basecsv/data_basecsv.html", form = db, fishes=rows ,imgs =imgepath) 
@app.route(webpage+"/data_basecsv/delete/<string:id>", methods = ['GET','POST'])
def delete(id):
	db = shortcut()
	db.execute('DELETE  FROM wwwoftable4 WHERE id = {0};'.format(id))
	db.connection.commit()
	flash('you delete that')
	return redirect(webpage+"/data_basecsv.html")




@app.route(webpage+'/data_basecsv/actualisar<string:id>', methods = ['GET','POST'])
def update_fish(id):
	db = shortcut()
	imgdir = "./static"+webpage+"/img/saved_db_img/"
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
		photo = request.files["photo"]
		#print(photo)

#=================== DB READ PHOTO   ===================#
		for i in range(len(os.listdir(imgdir))):
			image  = selctimg(rows[0],imgdir,i)
			name = image[1]
			img = image[0]
			namephoto = str(image[3])
		#namephoto = "5"
		photoname1 = str(photo).replace("<FileStorage: '","")
		photoname1 = str(photoname1).replace("' ('image/jpeg')>","")
		photoname1 = str(photoname1).replace("' ('image/png')>","")
		photoname1 = str(photoname1).replace("' ('image/jpg')>","")
		#print("\n"*2,photoname1 ,"\n"*2)
		"""
		dirphotoname1 = imgdir+photoname1
		os.rename(dirphotoname1,photoname)
		photo.save(dirphotoname1)
		"""
		aftersave = str(len(os.listdir(imgdir)))
		dirphotoname1 = imgdir+photoname1
		#p(imgdir+photoname1)
		photo.save(imgdir+photoname1)#name

		photoname2 = str(len(os.listdir(imgdir)))#+1
		photoname = str(imgdir+photoname2)#dir+1
		#photonameid = imgdir+photoname2 +scientific_name
		p(namephoto)
		print("save",str(imgdir+photoname1))
		print("rename",str(imgdir+namephoto))
		p(imgdir+photoname2)
		p(str(imgdir+aftersave))
		p(imgdir+photoname1)
		
		#os.remove(namephoto)
		os.rename(imgdir+photoname1,namephoto)
		#os.remove(imgdir+photoname1)
		photo = photoname1 
		photoname = namephoto
		#photoimg = cv2.imread(photo)
		#cv2.imwrite(imgdir+photoname,photoimg)

#=================== DB READ PHOTO   ===================#
		"""
#take the previous image

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

		"""
#=================== put in db ===================#
		waterforce = recommended_filtering

		fishdata = [scientific_name ,common_name ,minph  ,maxph  ,mingh  ,maxgh  ,mintemperature ,maxtemperature  ,weight  ,large_of_fish_in_centimeters ,needed_liters  ,recommended_filtering  ,eats   ,can_eat  ,reproduction ,kill ,breathing ,mouth ,latitude  ,longitude  , country  , state   ,city      ,waterenv  ,temperament ,behavior ,swimming_zone  ,vel , light  ,gravel ,habitats, habits   ,structural  , ornaments ,waterforce , ecosistem ,withpalnts ,forms_surroundings, photo ,description , water  ,photoname ]

		fishdatastr = ["scientific_name" ,"common_name" ,"minph"  ,"maxph"  ,"mingh"  ,"maxgh"  ,"mintemperature" ,"maxtemperature"  ,"weight"  ,"large_of_fish_in_centimeters" ,"needed_liters"  ,"recommended_filtering  ","eats"   ,"can_eat"  ,"reproduction" ,"kill ","breathing" ,"mouth ","latitude  ","longitude  ", "country"  , "state"   ,"city      ","waterenv  ","temperament ","behavior ","swimming_zone"  ,"vel ", "light  ","gravel ","habitats", "habits"   ,"structural  ", "ornaments ","waterforce" , "ecosistem" ,"withpalnts ","forms_surroundings ","photo" ,"description ", "water " ,"photoname"]
		db = db.connection.cursor()
		"""		
		strfishatributes = ""
		count = 0
		for i in fishdatastr:
			if len(fishdatastr)-1 == count:
				strfishatributes += i
			else:
				strfishatributes += i +","
			count +=1
		
		fishdatalist = []
		for i in fishdata:
			fishdatalist.append(i)
		for i in fishdatastr:
			fishdatalist.append(i)
		"""
		fishupdatestr = ""
		fishupdatelts = []
		count = 0
		#for in fishdata:
		for i,j  in zip(fishdatastr,fishdata):
			str(j).replace(",","")
			if len(fishdatastr)-1 == count:
				add = i+"= '{}'".format(str(j))
				fishupdatestr += str(i)+" =' {}' ".format(str(j))
				fishupdatelts.append(add)
			else:
				add = i+"= '{}'".format(str(j))
				fishupdatestr += str(i)+" =' {}' ".format(str(j))+","
				fishupdatelts.append(add)
			count += 1
		#fishupdatestr = fishupdatestr.title()
		#p("UPDATE wwwoftable4 SET {} WHERE id = {} ".format(tuple(fishupdatelts), id))
		#fishupdatelts=tuple(fishupdatelts)
		"""
		fishupdate = ""
		count = 0
		#for in fishdata:
		for i,j  in zip(fishdatastr,fishdata):
			if len(fishdatastr)-1 == count:
				fishupdate.append(str(i)+"= {}".format(j))
			else:
				fishupdate.append(str(i)+"= {}".format(j))
			count +=1
		for i in fishdatastr:
			for j in fishdata:
				if len(fishdatalist)-1 == count:
					fishdatalist.append(i)
					fishdatalist.append(j)
				else:
					fishdatalist.append(i +",") 
				count +=1 """
		#db.execute("UPDATE wwwoftable4 SET scientific_name = %s,ph = %s, temperature = %s, large_of_fish_in_centimeters = %s,needed_liters = %s, fish_diet = %s , fish_conduct= %s,location = %s, common_name = %s WHERE id = %s ;", (str(scientific_name),ph,temperature,needed_liters,large_of_fish_in_centimeters,str(fish_diet),str(fish_conduct),str(location),str(common_name),id))
		#db.execute(" INSERT INTO wwwoftable4 ( {} ) VALUES {};".format(strfishatributes,tuple(fishdata)))
		#db.execute("UPDATE wwwoftable4 SET %s WHERE id = %s ",(tuple(fishupdatelts), id))
		#db.execute(f"UPDATE wwwoftable4 SET {fishupdatelts} WHERE id = {id} ")
		update = "UPDATE wwwoftable4 SET {} WHERE id = {} ".format(fishupdatestr, id)
		#update = str(update)
		#update.replace(" [","")
		#update.replace("] ","")
		p(update)		
		db.execute(update)
		flash(' Updated Successfully')
		db.connection.commit()

		return redirect(webpage+'/data_basecsv.html')


@app.route(webpage+'/data_basecsv/<string:id>', methods = ['POST', 'GET'])
def get_fish(id):
	#imgchange = ""
	img = ""
	count = 0
	imgdir = "./static/www_of/img/saved_db_img/"
	imgepath = []
	db = shortcut()
	db.connection.cursor()
	db.execute('SELECT * FROM wwwoftable4 WHERE id = {}'.format(id))
	rows = db.fetchall()
	img = selctimg(rows[0],imgdir,len(os.listdir(imgdir)))
	name = str(img[1])
	imgae = img[0]
	imgs = img[2]
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
	return render_template(webpage+'/data_basecsv/updatefish.html', fish = rows[0],strcounter = name,test=imgs)#, imgpath=imgchange)

#====================================================================================================  add fish db ====================================================================================================#

	
@app.route(webpage+"/curapeces.html" , methods=['GET','POST'])
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
			sickness = "/static/www_of/img/prediccionerror.jpg"	
	return render_template('www_of/curapeces.html',prediccion=sickness)#,file=file)

	#==================================================================================================== curapeces ====================================================================================================#


	#====================================================================================================  web executing ====================================================================================================#

if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0")
