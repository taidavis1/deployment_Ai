from flask import Flask , render_template , redirect , url_for

app = Flask(__name__ , static_folder= 'staitc' , template_folder= 'templates')


################################################
if __name__ == '__main__':
    app.run(host='127.0.0.1' , port=3306 , debug=True)