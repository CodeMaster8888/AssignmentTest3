import pyodbc

class Database:
    global conn

    # Establish the connection
    server = 'test-sql-server-zw023.database.windows.net'
    database = 'SmartHome'
    username = 'AdminUser'
    password = 'Password8!'
    driver = '{ODBC Driver 17 for SQL Server}'
    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' +
                          server + ';PORT=1433;DATABASE=' + database +
                          ';UID=' + username + ';PWD=' + password)

    def Create(self, sensorData):
        curr_obj = conn.cursor()

        sensor1 = sensorData.sensor1
        sensor2 = sensorData.sensor2
        sensor3 = sensorData.sensor3
        motor1 = sensorData.motor1
        motor2 = sensorData.motor2
        light1 = sensorData.light1
        datetime = sensorData.datetime

        query = "INSERT INTO SensorDataset VALUES (1,%s,%s,%s,%s,%s,%s,'%s')" % (
        sensor1, sensor2, sensor3, motor1, motor2, light1, datetime)

        conn.execute(query)

        conn.commit()

    def Get(self):
        query = "SELECT [sensor1],[sensor2],[sensor3],[motor1],[motor2],[light1],[DateTime] FROM [dbo].[SensorDataset]"

        data = conn.execute(query)

        rows = data.fetchall()

        return rows
