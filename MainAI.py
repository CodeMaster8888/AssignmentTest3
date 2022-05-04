import DatabaseConnection

class Control:

    def mainTask(self, sensorData):

        data = DatabaseConnection.Database.Get(self)

        if sensorData.sensor1 == 1:
            sensorData.motor1 = 1
        if sensorData.sensor2 == 1:
            if Control.Calculate_1_2(self, data):
                sensorData.motor1 = 0
            if sensorData.motor2 == 1:
                sensorData.motor2 = 0
            else:
                sensorData.motor2 = 1
        if sensorData.sensor3 == 1:
            if sensorData.light1 == 1:
                sensorData.light1 = 0
            else:
                sensorData.light1 = 1
        return sensorData

    def Calculate_1_2(self, dataset):
        for data in dataset:
            if data.sensor1 == 1:
                return True
            else:
                return False

    def CalculateDecision_2_1(self, dataset):
        for data in dataset:
            if data.sensor2 == 1:
                return True
            else:
                return False