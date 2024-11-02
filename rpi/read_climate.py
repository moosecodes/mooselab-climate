import serial
import time

# Set up the serial connection (use '/dev/ttyACM0' for GPIO serial communication)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=60)
time.sleep(2)  # Wait for connection to establish

try:
    while True:
        if ser.in_waiting > 0:  # Check if there is incoming data
            raw_line = ser.readline()  # Read raw bytes
            try:
                line = raw_line.decode('utf-8').strip()  # Decode and strip whitespace

                # Check if the line starts with 'CELCIUS:' to ensure valid data format
                if line.startswith("CELCIUS:"):
                    try:
                        # Split the line into temperature and humidity
                        data = line.split(",")
                        celcius = float(data[0].split(":")[1])
                        farenheit = float(data[1].split(":")[1])
                        humidity = float(data[2].split(":")[1])
                        
                        # Print parsed data
                        print(f"celcius: {celcius}, farenheit: {farenheit}, humidity: {humidity}")
                        
                        # TODO: Save data to database

                    except (IndexError, ValueError):
                        print("Error parsing data")
            except UnicodeDecodeError:
                print("Received non-UTF-8 data, skipping...")
        else:
            time.sleep(0.2)  # Short delay to avoid busy waiting
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    ser.close()

