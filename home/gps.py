import serial
import time
import json

def getSensorData():
    print("------GPS Data collection------")
    ser = None
    try:
        ser = serial.Serial('COM4', 9600, timeout=1)
        time.sleep(2)

        data = ser.readline().decode().strip()
        if data != '':
            json_data = json.loads(data)
            print(json_data)
            return json_data
        
    except serial.SerialException as e:
        print("Serial port error: ", e)

    finally:
        if ser:
            ser.close()



