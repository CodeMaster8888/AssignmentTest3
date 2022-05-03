# using flask_restful
import json

from flask import Flask, jsonify, request

# creating the flask app
import DatabaseConnection
import MainAI
from SensorData import SensorData

app = Flask(__name__)

@app.route('/sensor', methods=['POST'])
def post():
    data = request.get_json()

    sensordata = SensorData.to_object(SensorData, data)

    data = MainAI.Control.mainTask(MainAI, sensorData=sensordata)

    DatabaseConnection.Database.Create(DatabaseConnection, data)

    return json.dumps(data.__dict__)

# driver function
if __name__ == '__main__':
    app.run(host='0.0.0.0')


