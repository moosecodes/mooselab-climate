import serial
import mysql.connector
import time
from mysql.connector import Error

# Set the correct serial port for the Arduino Leonardo
serial_port = '/dev/ttyACM0'
baud_rate = 9600

# Connect to the Arduino
ser = serial.Serial(serial_port, baud_rate, timeout=60000)

# Database connection settings
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'weather_data'
}

# Function to insert data into the database
def insert_reading(celcius, farenheit, humidity):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            cursor = connection.cursor()
            # Insert data into the readings table
            insert_query = "INSERT INTO readings (celcius, farenheit, humidity) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (celcius, farenheit, humidity))
            connection.commit()
            print(f"Inserted: {celcius} °C, {farenheit} °F, {humidity} %")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main loop
try:
    while True:
        if ser.in_waiting > 0:
            # Read the data from the serial port
            line = ser.readline().decode('utf-8').strip()
            
            climate_data = line.split(',')

            celcius = float(climate_data[0].split(':')[1])
            farenheit = float(climate_data[1].split(':')[1])
            humidity = float(climate_data[2].split(':')[1])

            # Save to database
            insert_reading(celcius, farenheit, humidity)

            time.sleep(60)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
