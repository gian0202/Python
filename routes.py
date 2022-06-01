from flask import Flask
from main import insertUser
app = Flask("Youtube")


@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return{"Ola": "mundo"}
app.run()
