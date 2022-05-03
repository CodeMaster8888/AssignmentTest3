class SensorData:

    def __init__(self, sensor1, sensor2,sensor3, motor1, motor2, light1, datetime, __class__):
        self.sensor1 = sensor1
        self.sensor2 = sensor2
        self.sensor3 = sensor3
        self.motor1 = motor1
        self.motor2 = motor2
        self.light1 = light1
        self.datetime = datetime
        self.__class__ = __class__

    def to_object(self, object):
        if object['__class__'] == "SensorData":
            inst = SensorData(object['sensor1'],
                              object['sensor2'],
                              object['sensor3'],
                              object['motor1'],
                              object['motor2'],
                              object['light1'],
                              object['datetime'],
                              object['__class__'])
        return inst

    sensor1 = 0
    sensor2 = 0
    sensor3 = 0
    motor1 = 0
    motor2 = 0
    light1 = 0
    datetime = None
    __class__ = "SensorData"


