from flask import Flask, make_response, jsonify, request
from db import car

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/car", methods=["GET"])
def get_car():
  return make_response(
    jsonify(car)
  )

@app.route("/car", methods=["POST"])
def create_car():
  newCar = request.json
  car.append(newCar)
  return { "msg": "Added car sucess", "data": car}

@app.route("/car/<int:car_id>", methods=["PUT"])
def update_car(car_id):
  update_car_data = request.json
  if car_id < 0 or car_id >= len(car):
    return {"error": "Carro não encontrado"}, 404
  
  car[car_id].update(update_car_data)
  return { "msg": f"Carro {car_id} atualizado com sucesso",  "data": car[car_id]}

app.run()

