from flask import Flask
from db import car

app = Flask(__name__)

@app.route("/car", methods=["GET"])
def get_car():
  return car


app.run()