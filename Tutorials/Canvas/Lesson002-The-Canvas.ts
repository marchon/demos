/**
 * Demonstrates creating a 2D canvas and context.
 */

// Workaround to prevent TS2082 and TS2087.
// I don't know why this works.
var unused: Window = window;

class Canvas {
  private _window: Window;
  private _context;
  constructor(width: number, height: number) {
    this._window = window.open("", "", "width=" + width + ", height=" + height, false);
    
    var popDoc: Document = this._window.document;
    
    var canvas: HTMLCanvasElement = popDoc.createElement("canvas");
    
    canvas.setAttribute("id", "graph");
    canvas.setAttribute("width",  width.toString());
    canvas.setAttribute("height", height.toString());
    
    popDoc.body.appendChild(canvas);
    // Remove the margin that pushes the canvas.
    popDoc.body.style.margin = "0";
    
    this._context = canvas.getContext("2d");

    this._context.fillStyle = "#555555";
    this._context.fillRect(0, 0, width, height);
  }

  public close() {
    this._window.close();
  }
}

var canvas = new Canvas(800, 600)
