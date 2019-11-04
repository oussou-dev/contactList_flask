from flask import Flask
from flask import render_template, request, redirect, url_for

app = Flask(__name__)

contact_list=[{"nom":"Einstein","prenom":"Albert","tel":"06.00.00.00.00","mail":"albert@emc2.com"},
              {"nom":"Shannon","prenom":"Claude","tel":"06.00.00.00.00","mail":"claude@fesup2fmax.com"},
              {"nom":"Fourier","prenom":"Joseph","tel":"09.00.03.00.01","mail":"joseph@maserie.fr"}
              ]


@app.route('/')
def index():
    return render_template("index.html",contact_list=contact_list)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('create.html', contact=None)
    
    if request.method == "POST":
        contact_list.append(request.form.todict())
        return redirect(url_for('index'))
        
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.methd == 'GET':
        return contact = contact_list[id-1]
    
    if request.method == 'POST':
        contact_list[id-1] = request.form.todict()
        return redirect(url_for('index'))
        
@app.route('/delete/<int:id>', methodes=['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        return render_template('delete.html', contact = contact_list[id-1])
        
    if request.method =='POST':
        del contact[id-1]
        return redirect (url_for('index'))