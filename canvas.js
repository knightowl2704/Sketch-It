var canvas = document.createElement('canvas');
document.body.appendChild(canvas)
document.body.style.backgroundColor = "#F5F5F5";
canvas.className = 'canvasele';
var coords = [];

var p = document.getElementById('preds')
p.className = 'predspara';
const CANVASCOLOR = '#FFFFFF';
const W = 250;
const H = 250;

canvas.style.position = 'fixed';
canvas.width  = W;
canvas.height = H;


var ctx = canvas.getContext('2d');
ctx.strokeRect(0, 0, canvas.width, canvas.height);

colorCanvas();

var pos = {
    x:0,
    y:0
};
    

var Predictions = {
    'Predictions': 'No Sketch found / Not Recognisible'
}
p.innerHTML = Predictions['Predictions'];


var clearButton = document.getElementById('clearbutton');
var submitButton = document.getElementById('submitbutton');

window.addEventListener('resize', resize);
document.addEventListener('mousemove', draw);
document.addEventListener('mousedown', setPosition);
document.addEventListener('mouseenter',setPosition);



clearButton.addEventListener('click', clear);
submitButton.addEventListener('click', submitCanvas)


function colorCanvas(){
    ctx.fillStyle = CANVASCOLOR;
    ctx.fillRect(0,0,W,H);
}

function submitCanvas(e){

    const dpi = window.devicePixelRatio;
    
    var canvasData = canvas.toDataURL('image/png');  
    console.log(canvasData)
    fetch('http://127.0.0.1:8888/predict',{
        method: "post",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      
        //make sure to serialize your JSON body
        body: JSON.stringify({
          b64: canvasData
        })
      })
    .then(response => response.json())
    .then(data => {p.innerHTML = data['Predictions']})
    console.log(Predictions)
}



function clear(e){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    colorCanvas();
    clearPredictions();    
}


function setPosition(e){
    pos.x = e.clientX - canvas.offsetLeft;
    pos.y = e.clientY - canvas.offsetTop;
};
function resize(){
    ctx.canvas.width = W;
    ctx.canvas.height = H;
    colorCanvas();
};

function draw(e){
    if (e.buttons !== 1)return;

    ctx.beginPath();
    ctx.lineWidth = 10;
    ctx.lineCap = 'round';
    ctx.strokeStyle = '#000000';

    ctx.moveTo(pos.x, pos.y);
    setPosition(e);
    ctx.lineTo(pos.x, pos.y); // to

    ctx.stroke();

};

function clearPredictions(){
    Predictions = {
        'Predictions': 'No Sketch found / Not Recognisible'
    }
    p.innerHTML = Predictions['Predictions']
}

