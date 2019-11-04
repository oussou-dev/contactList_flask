from flask import Flask
app = Flask(__name__)

contact_list=[{"nom":"Einstein","prenom":"Albert","tel":"06.00.00.00.00","mail":"albert@emc2.com"},
              {"nom":"Shannon","prenom":"Claude","tel":"06.00.00.00.00","mail":"claude@fesup2fmax.com"},
              {"nom":"Fourier","prenom":"Joseph","tel":"09.00.03.00.01","mail":"joseph@maserie.fr"}
              ]

def index():
    #construction de la chaine html

    html="<!DOCTYPE html>\n"
    html=html+"<html>\n"
    html=html+"<head><title>Mon site de gestion de contact</title></head>\n"
    html=html+"<body>\n"
    html=html+"<h1>Mes contacts</h1>\n"
    html=html+"<table>\n"
    html=html+"<tr>\n"
    html=html+"<th>Nom</th><th>Prenom</th><th>Telephone</th><th>Email</th>"
    html=html+"</tr>\n"

    for indice in range(len(contact_list)):
        mon_contact=contact_list[indice]

        html=html+"<tr>\n"
        html=html+"<td>"+mon_contact["nom"]+"</td>\n"
        html=html+"<td>"+mon_contact["prenom"]+"</td>\n"
        html=html+"<td>"+mon_contact["tel"]+"</td>\n"
        html=html+"<td>"+mon_contact["mail"]+"</td>\n"
        html=html+"</tr>\n"

    html=html+"</table>\n"
    html=html+"</body>\n"
    html=html+"</html>\n"
    return html





@app.route('/')
def hello_world():
    return 'Hello, World!'