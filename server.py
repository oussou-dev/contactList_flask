from flask import Flask
from flask import render_template

app = Flask(__name__)

contact_list=[{"nom":"Einstein","prenom":"Albert","tel":"06.00.00.00.00","mail":"albert@emc2.com"},
              {"nom":"Shannon","prenom":"Claude","tel":"06.00.00.00.00","mail":"claude@fesup2fmax.com"},
              {"nom":"Fourier","prenom":"Joseph","tel":"09.00.03.00.01","mail":"joseph@maserie.fr"}
              ]

def index():
    return render_template("index.html",contact_list=contact_list)



@app.route('/')
def hello_world():
    return 'Hello, World!'