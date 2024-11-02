Initial setup

- upload code to arduino
- Wire up the arduino
- Wire up the rpi
- plug in USB serial cable from arduino to rpi
- sudo raspi-config on rpi terminal
- enable rpi serial connection (say no to remote console log in when doing this setup)
- (optional) enable rpi VNC
- (optional) disable boot to desktop
- install DHT sensor library via Arduino IDE through Manage Extensions

### On RPi console:
``` bash
sudo apt update

sudo apt upgrade

# Install database server
sudo apt install mariadb-server

# Install mysql-connector-python
pip install mysql-connector-python

sudo mysql_secure_installation

sudo systemctl start mariadb

# Start database server on boot
sudo systemctl enable mariadb

sudo systemctl status mariadb
```
### Navigate to working folder and create Python Virtual Environment

``` bash
# Create a virtual environment (if not already created)
python3 -m venv arduinoenv

# Activate the virtual environment
source arduinoenv/bin/activate

# Install dependecies
pip install -r requirements.txt
```

To freeze any new depenencies in `requrements.txt`:

``` bash
pip freeze > requirements.txt
```

### Create database and table in database:

``` sql
-- Access the MariaDB shell
sudo mysql -u root -p

-- Create a database
CREATE DATABASE weather_data;

-- Use the database
USE weather_data;

-- Create a table for storing temperature and humidity
CREATE TABLE readings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    farenheit FLOAT NOT NULL,
    celsius FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';

GRANT SELECT, INSERT, UPDATE, DELETE ON weather_data.* TO 'your_username'@'localhost';

GRANT ALL PRIVILEGES ON weather_data.* TO 'your_username'@'localhost';

FLUSH PRIVILEGES;

EXIT;
```

### Database credentials config

Setup credentials for mariadb in python script:

``` python
db_config = {
    'host': 'localhost',  # the IP address or hostname for your database server
    'user': 'your_username',  # the MariaDB username
    'password': 'your_password',  # the MariaDB password
    'database': 'weather_data'  # the correct database name
}
```
