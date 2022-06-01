from flask import Flask, make_response
from flask_restful import Resource, Api

from resources.teste import Teste
from resources.teste import c
from resources.teste import baixarP
app = Flask(__name__)
api = Api(app)

api.add_resource(Teste, '/teste2')
api.add_resource(c, '/comparacao')
api.add_resource(baixarP, '/teste')
if __name__== '__main__':
    app.run(debug=True)
