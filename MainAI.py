import DatabaseConnection

class Control:

    def mainTask(self, sensorData):

        data = DatabaseConnection.Database.Get(self)

        if sensorData.sensor1 == 1:
            Control.CalculateDecision(self, data)
            sensorData.motor1 = 1
        if sensorData.sensor2 == 1:
            sensorData.motor2 = 1
        if sensorData.sensor3 == 1:
            sensorData.light1 = 1
        return sensorData

    def CalculateDecision(self, dataset):
        for data in dataset:
            if data.sensor1 == 1:
                return True
            else:
                return False
