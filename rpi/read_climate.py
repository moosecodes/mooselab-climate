## Python Script Running on Raspberry Pi

import serial
import mysql.connector

from db_config import db_config, insert_query
from mysql.connector import Error
from gpiozero import LED


# Set the correct serial port for the Arduino Leonardo
serial_port = '/dev/ttyACM0'
baud_rate = 9600
led = LED(21)

# Connect to the Arduino
ser = serial.Serial(serial_port, baud_rate)

# Function to insert data into the database
def insert_reading(farenheit, celsius, humidity):
    led.on()
    try:
        # Establish the database connection
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(insert_query, (farenheit, celsius, humidity))
            connection.commit()
            
            print(f"Inserted --> {farenheit} °F, {celsius} °C, {humidity} %")
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            led.off()

# Main loop
print("\nStarting...\n")
try:
    while True:
        if ser.in_waiting > 0:
            # Read the data from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            climate_data = line.split(',')

            farenheit = float(climate_data[0].split(':')[1])
            celsius = float(climate_data[1].split(':')[1])
            humidity = float(climate_data[2].split(':')[1])

            # Save to database
            insert_reading(farenheit, celsius, humidity)
except KeyboardInterrupt:
    print("\nExiting...\n")
finally:
    ser.close()
