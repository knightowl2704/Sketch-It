# Sketch-It
Convolutional Neural Network trained on Google's Quick Draw Dataset to recognize hand drawn doodle images. The CNN model predictions are exposed using a REST API with Flask server and requests are made to the model from an in-browser canvas element using JavaScript.

## Requirements
All the Requirements are listed in `requirements.txt`. 

OpenCV, Keras, Numpy, PIL.

## Browser Sketch Canvas

The `canvas.js` file handles the DOM manipulation for drawing and clearing the Canvas element and all the requests are sent to the Flask server for the current state of the canvas when Submit button is clicked. 
Clear button clears the canvas contents. 

![Empty Canvas](https://github.com/knightowl2704/Sketch-It/blob/main/README%20Statics/image.jpg)

## Predictions 

Server runnning on local host. Run the `server.py` file first. Make sure all the libraries and packages are available. 

### Apple 
![Apple](https://github.com/knightowl2704/Sketch-It/blob/main/README%20Statics/apple.jpg)

### Clock 
![clock](https://github.com/knightowl2704/Sketch-It/blob/main/README%20Statics/clock.jpg)

### Hexagon 
![Hexagon](https://github.com/knightowl2704/Sketch-It/blob/main/README%20Statics/hexagon.jpg)

### Skull
![Skull](https://github.com/knightowl2704/Sketch-It/blob/main/README%20Statics/skull.jpg)
