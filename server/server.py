import flask
from flask import json , request
import numpy as np 
import base64
from io import BytesIO
import re
from PIL import Image
from flask import jsonify
from flask_cors import CORS
from numpy.lib.type_check import imag
import cv2

from tensorflow.keras.models import load_model

rev_class_map = {0: 'apple', 1: 'bee', 2: 'banana', 3: 'bus', 4: 'cake', 5: 'clock', 6: 'cup', 7: 'door', 8: 'elephant', 9: 'eyeglasses', 10: 'fish', 11: 'flower', 12: 'guitar', 13: 'hexagon', 14: 'ice cream', 15: 'mouse', 16: 'spoon', 17: 'strawberry', 18: 'scissors', 19: 'postcard', 20: 'pineapple', 21: 'skull', 22: 'owl', 23: 'radio', 24: 'paintbrush', 25: 'snake'}
emoji_map = {'apple': '🍎', 'banana': '🍌', 'bee': '🐝', 'bus': '🚌','cake': '🎂','clock': '🕑','cup': '🥤','door': '🚪','elephant': '🐘','eyeglasses': '👓','fish': '🐟','flower': '🌸','guitar': '🎸','hexagon': '🔷','ice cream': '🍨','mouse': '🐁','owl': '🦉','paintbrush': '🖌️','pineapple': '🍍','postcard': '🪧','radio': '📻','scissors': '✂️','skull': '💀','snake': '🐍','spoon': '🥄','strawberry': '🍓'}

model = load_model('server//v5.h5', compile = False)

app = flask.Flask(__name__)
CORS(app)

@app.route('/predict', methods = ['GET','POST'])
def predict():

    # print('We are on predict route')
    data = request.json
    b64 = data['b64']    
    im = Image.open(BytesIO(base64.b64decode(re.search(r'base64,(.*)', b64).group(1))))
    
    def performImageProcessing(PIL_image):
        imgarr = np.array(PIL_image)


        gray = cv2.cvtColor(imgarr, cv2.COLOR_BGR2GRAY)
        # cv2_imshow(gray)
        ret, binary = cv2.threshold(gray, 100, 255, 
            cv2.THRESH_OTSU)
        # cv2_imshow(binary)
        inverted_binary = ~binary

        # cv2_imshow(inverted_binary)

        contours, hierarchy = cv2.findContours(inverted_binary,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE)

        # first_contour = cv2.drawContours(imgarr, contours, 0,(255,0,255),3)
        # cv2_imshow(contours[0])
        for c in contours:
            x, y, w, h = cv2.boundingRect(contours[0])
            # first_contour = cv2.rectangle(first_contour,(x,y), (x+w+5,y+h+5), (255,150,0), 5)

        imfinal = gray[y:y+h,x:x+w]
        img_resized = cv2.resize(imfinal, (28, 28))
        return img_resized

    new = performImageProcessing(im)
    new = np.array(new) 
    import matplotlib.pyplot as plt 
    # plt.imsave('1.png', new)


    preds = model.predict((255-new).reshape(1,28,28,1))
    predict_class = np.argmax(preds, axis=1)
    
    predictions = {
        'Predictions' : 'Not Recognised'
    }
    if rev_class_map[predict_class[0]]:
        predictions['Predictions'] = rev_class_map[predict_class[0]].capitalize() + ' ' + emoji_map[rev_class_map[predict_class[0]]]

    return jsonify(predictions)

app.run(port='8888')
