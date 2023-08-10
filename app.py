'''SE IMPORTA LA CLASE FLASK DESDE EL MODULO FLASK'''
from  flask import Flask,render_template


#CREAR EL OBJETO FLASK DE LA APP  __name__ asume el valor donde se  esta trabajando
app=Flask(__name__)


#crear la primera ruta en python flask
@app.route('/paises')
def paises():
    username="kevin fernando"
    #estructura de paises
    continentes=[
       
        {
            "nombre":"America",
            "Poblacion":"mil millones",
            "Superficie":"1m",
            "paises":[ {
                    "nom":"colombia",
                    "cap":"bogota",
                    "mon":"peso",
                    "pob":51
                },
                {"nom":"peru",
                 "cap":"Lima",
                    "mon":"sol",
                    "pob":33
                    },
                {"nom":"paraguay",
                 "cap":"asuncion",
                    "mon":"guarani",
                    "pob":33}]
        },{
            "nombre":"Europa",
            "Poblacion":"746 millones",
            "Superficie":"1m",
            "paises":[ {
                    "nom":"reino unido",
                    "cap":"londres",
                    "mon":"usd",
                    "pob":55
                },
                {"nom":"alemania",
                 "cap":"berlin",
                    "mon":"euro",
                    "pob":33
                    },
                {"nom":"francia",
                 "cap":"asuncion",
                    "mon":"guarani",
                    "pob":33}]
        }]
   
    #renderizar una vista de la carpeta templates
    return render_template("paises.html",dtusername=username,continentes=continentes)












