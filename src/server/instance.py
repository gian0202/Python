from flask import Flask
from flask_restplus import Api

class Server():
    def _init_(self, ):
        self.app = Flask(_name_)
        self.api = Api(self.app,
            version='1.0',
            title='Sample Book API',
            description='A simple book API',
            doc='/docs'
            )
    def run(self, ):
        self.app.run(
            debug=True
        )
server = Server()
