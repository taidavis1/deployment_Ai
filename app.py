from flask import Flask , render_template , redirect , url_for, request, jsonify
import backend
app = Flask(__name__ , static_folder= 'static' , template_folder= 'templates')
@app.route('/' , methods = ['GET' , 'POST'])
def Home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        input1 = request.args.get('input1')
        input2 = request.args.get('input2')
        input3 = request.args.get('input3')
        input4 = request.args.get('input4')
        predict = backend.predictions(input1 , input2 , input3 , input4)
        print(predict)
        return "Hello"
###################################################
if __name__ == '__main__':
    app.run(host='127.0.0.1' , port=8000 , debug=True)