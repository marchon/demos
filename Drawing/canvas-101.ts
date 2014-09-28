// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

var popUp = window.open("", "", "width=800, height=600", false);

var document = popUp.document;

var canvas = document.createElement("canvas");

canvas.setAttribute("id", "graph");
canvas.setAttribute("width", "400");
canvas.setAttribute("height", "400");

document.body.appendChild(canvas);

var context = canvas.getContext("2d");

context.beginPath();
context.moveTo(150, 100);
context.lineTo(200, 225);
context.closePath();
context.stroke();

//popUp.close();

/**
 * Called for each animation tick.
 */
function tick(time: number): void {
  
}

function terminate(time: number): boolean {
  return false;
}

function setUp() {
  
}

function tearDown(e: Error) {
  
}

eight.animationRunner(tick, terminate, setUp, tearDown, popUp).start();