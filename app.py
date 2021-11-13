from flask import Flask, render_template, Request
from flask.globals import request
import pickle

app_flask = Flask(__name__)

# @app_flask.route('/') #decorator - execute the below fn automatically
# def index():
#     return 'hello world from flask !!!!'

@app_flask.route('/')
def home():
    return render_template('homepage.html')
    
@app_flask.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app_flask.route('/contact')
def contact():
    return render_template('contact.html')

@app_flask.route('/enquiry')
def enquiry():
    return render_template('enquiry.html')

@app_flask.route('/login')
def login():
    return render_template('login.html')

@app_flask.route('/predict', methods=["POST"])
def predict():
    # fname = request.form.get('firstname')
    # lname = request.form.get('lastname')
    # email = request.form.get('email')
    # phone = request.form.get('number')
    # print(fname, lname, email, phone)
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    # print(preg,plas,pres,skin,test,mass,pedi,age)
    # return render_template('predict.html')
    loaded_model = pickle.load(open('dib_78.pkl', 'rb'))
    prediction = loaded_model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if prediction[0]==1:
        print('dibatic')
        val = 'dibatic'
    else:
        print('not dibatic')
        val = 'not dibatic'

    return render_template("result.html", value = val)

if __name__=='__main__':
    app_flask.run(debug=True)

