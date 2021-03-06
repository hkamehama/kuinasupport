import serial
import csv
import datetime
from picamera import PiCamera
from time import sleep

camera = PiCamera()
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    String_data = ser.readline().strip()
    float_data = float(String_data)
    with open('Logs/temp.csv', 'a') as f:
        dt_now = datetime.datetime.now()
        dt_now_str = dt_now.strftime('%Y_%m_%d-%H_%M_%S')
        writer = csv.writer(f)
        writer.writerow([dt_now_str,str(float_data)])
        print("save temp")

    camera.start_preview()
    sleep(5)#このスリープは少なくとも2秒必要。カメラの露光時間が必要なため
    dt_now_str = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
    camera.capture('images/image' + dt_now_str + '.jpg')
    print("imageSaved")
    camera.stop_preview()

    sleep(10)

ser.close()
