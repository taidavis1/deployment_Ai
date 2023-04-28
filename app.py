from flask import Flask , render_template , redirect , url_for, request, jsonify , flash
import train
import numpy as np
import os
app = Flask(__name__ , static_folder= 'static' , template_folder= 'templates')
app.config['SECRET_KEY'] = os.urandom(10)

@app.route('/' , methods = ['GET' , 'POST'])
def Home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        temp = request.form['temp']
        humidity = request.form['humidity']
        windspeed = request.form['windspeed']
        cloudcover = request.form['cloudcover']
        train_d = train.train_run_on()
        prediction = train_d.predictions(np.array([[temp , humidity , windspeed , cloudcover]]))[0]
        return jsonify({'msg': prediction})
#########################################################
if __name__ == '__main__':
    app.run(host='127.0.0.1' , port=4000 , debug=True)