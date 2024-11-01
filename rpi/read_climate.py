import serial
import time

arduino_port = '/dev/ttyusbmodem1101'  # Replace with your actual Arduino port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Allow some time for the connection to establish

try:
    while True:
        if ser.in_waiting > 0:  # Check if there is incoming data
            line = ser.readline().decode('utf-8').strip()  # Read and decode the line
            # Print raw data for reference
            print(f"Received from Arduino: {line}")

            # Check if the line starts with 'TEMP:' to ensure valid data format
            if line.startswith("TEMP:"):
                try:
                    # Split the line into temperature and humidity
                    data = line.split(",")
                    temperature = float(data[0].split(":")[1])
                    humidity = float(data[1].split(":")[1])

                    # Print parsed data
                    print(
                        f"Temperature: {temperature} °C, "
                        f"Humidity: {humidity} %"
                    )

                except (IndexError, ValueError):
                    print("Error parsing data")
        else:
            time.sleep(0.1)  # Short delay to avoid busy waiting
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    ser.close()
