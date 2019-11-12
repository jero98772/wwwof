
var wwwof ='word wide web of fish';
document.write('<center><p style="font-size:40px">wwwof </p><b><h2>',wwwof,'</h2><b></center>') ;
let canvas;
let texto_lado1,texto_lado2,texto_lado3,figura;
let entrada_lado_1,entrada_lado_2,entrada_lado_3;
let cubica,prisma_rectangular,prisma_triangular;
let parrafo;
let Select,selected,select;
let l,r,R,w,h;
let litros ,acuarium;
let angle;
let y,x;
let half_torus,torusVOL,radius1,radius2,fishtank_classic,cilindro,perimetro;
let minisegundos=10000;

function calcular_litros() {
canvas=createCanvas(350, 350, WEBGL);
//x=650
x = (windowWidth - width) / 2;
//y = (windowHeight - height ) / 2;
y=215;
canvas.position(x, y);

figura=document.getElementById("figura");
texto_lado1=document.getElementById("lado01");
texto_lado2=document.getElementById("lado02");
texto_lado3=document.getElementById("lado03");
texto_lado4=document.getElementById("lado04");
entrada_lado_1=document.getElementById("entrada_lado_1");
entrada_lado_2=document.getElementById("entrada_lado_2");
entrada_lado_3=document.getElementById("entrada_lado_3");

parrafo=document.getElementById('parrafo');
Select = document.From2.Selecion2;
Select=document.getElementById('Selecion1');
selected = Select.options[Select.selectedIndex].value;
if (selected=='prisma_rectangular') {
	l=parseFloat(entrada_lado_1.value)
	w=parseFloat(entrada_lado_2.value)
	h=parseFloat(entrada_lado_3.value)
	litros=(l*h*w)/1000;
	console.log(litros)

	parrafo.innerHTML=litros+"  litros"
	figura.innerHTML='prisma_rectangular'
	texto_lado1.innerHTML='largo cm'
	texto_lado2.innerHTML='alto cm'
	texto_lado3.innerHTML='ancho cm'
	acuarium=setInterval(dibujarcubo(l,w,h,0,0),minisegundos);
}
	
if (selected=='cubica'){
	l=parseFloat(entrada_lado_1.value)
	litros=(l**3)/1000;

	console.log(litros);
	figura.innerHTML='cubica'
	texto_lado1.innerHTML='largo (solamente) cm '
	texto_lado2.innerHTML='no es neseario'
	texto_lado3.innerHTML='no es neseario'
	parrafo.innerHTML=litros+" litros"
	acuarium=setInterval(dibujarcubo(l),minisegundos);
}
/*if (selected=='fishtank_classic'){
	radius1=parseFloat(entrada_lado_1.value);
	R=radius1;
	radius2=parseFloat(entrada_lado_2.value);
	r=radius2;
	h=parseFloat(entrada_lado_3.value);
	
	torusVOL=PI*R*(r**2);
	half_torus=torusVOL/2;
	cilindro=R*(PI**2)*h;
	fishtank_classic=cilindro+half_torus
	litros=fishtank_classic/1000
	print(torusVOL)
	print(half_torus)
	print(cilindro)
	print(fishtank_classic)
	print(litros)
	
	//volumen_sphere=(4/3)*PI*(R**3)
	//healment_sphere=((1/3)*PI*(h**2))*((3*r)-h)

	//total_healments=healment_sphere*2
	figura.innerHTML='fishtank_classic'
	texto_lado1.innerHTML='big radio R'
	texto_lado2.innerHTML='small radio r -big radio R'
	texto_lado3.innerHTML='height'
	parrafo.innerHTML=litros
	draw_fishtank_clasic(R,r,h);
}*/
if (selected=='prisma_triangular'){
	b=parseFloat(entrada_lado_1.value)
	Hbase=parseFloat(entrada_lado_2.value)
	h=parseFloat(entrada_lado_3.value)
	//perimetro=l1+l2+l3
	litros=((b*Hbase)/2)*h
	litros=	litros/1000
	texto_lado1.innerHTML='largo base cm'
	texto_lado2.innerHTML='altura de la base cm'
	texto_lado3.innerHTML='altura 3 cm'
	parrafo.innerHTML=litros+"litros"+"<h1>dibuja el lado 1</h1>"
	dibujar_prisma(b,h,3)
}
if (selected=='cilindro'){
	R=parseFloat(entrada_lado_1.value)
	h=parseFloat(entrada_lado_2.value)
	litros=(R**2)*h
	litros=	litros/1000
	texto_lado1.innerHTML='radio cm'
	texto_lado2.innerHTML='alto cm'
	texto_lado3.innerHTML='no es neseario'
	parrafo.innerHTML=litros+" PI litros"
	dibujar_prisma(R,h,24)
}
}

function dibujarcubo(l,w,h,x,y) {
	frameCount;
	background(200);
	rotateX(frameCount * 0.01);
  	rotateY(frameCount * 0.01);
	acuarium=box(l,w,h,x,y);
//	draw=document.getElementById('draw');
//	draw.innerHTML=acuarium;
}

/*
function draw_fishtank_clasic(R,r,h){
	frameCount;
	background(200);
	rotateX(frameCount * 0.01);
  	rotateY(frameCount * 0.01);
	translate(0, 0);

	rotateX(frameCount * 0.01);
  	rotateY(frameCount * 0.01);
	ellipsoid(R,h,R);
}
*/
function dibujar_prisma(R,h,s){
	frameCount;
	background(200);
	/*
	rotateX(frameCount * 0.01);
  	rotateY(frameCount * 0.01);
	translate(0, 0);*/

	rotateX(frameCount * 0.01);
  	rotateY(frameCount * 0.01);
	cylinder(R,h,s);
}
setInterval(calcular_litros,minisegundos);
