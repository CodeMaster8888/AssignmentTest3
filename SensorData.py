class SensorData:

    def __init__(self, sensor1, sensor2,sensor3,datetime):
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensor3 = sensor3
        self.datetime = datetime

    def to_object(self, object):
        if object['__class__'] == "SensorData":
            inst = SensorData(object['sensor1'], object['sensor2'], object['sensor3'], object['datetime'])
        return inst

    sensor1 = None
    sensor2 = None
    sensor3 = None
    datetime = None


