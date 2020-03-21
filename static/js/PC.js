let pc ;

function setup() {
	canvas = createCanvas(800,500) ;
	pc = new divePC();
}

function draw() {
	var time = 200
	background(150);
	var setup = pc.stepsetup();
	canvas.position(setup.x,(setup.y+400));
	pc.moves();	

	pc.liquid()
	//dont move draws 
	pc.arrow();
	pc.board();


}
document.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/_hT_zreeG8s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>');
document.write('<iframe width="560" height="315" src="https://www.youtube.com/embed/tqku9z-Wesg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>');