# using flask_restful
import json

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
import DatabaseConnection
import MainAI
from SensorData import SensorData

app = Flask(__name__)
# creating an API object
api = Api(app)


class Sensor(Resource):
    def post(self):
        data = request.get_json()

        sensordata = SensorData.to_object(self, data)

        data = MainAI.Control.mainTask(self, sensorData=sensordata)

        DatabaseConnection.Database.Create(self, data)

        return json.dumps(data.__dict__)


api.add_resource(Sensor, '/sensor')

# driver function
if __name__ == '__main__':
    app.run()
