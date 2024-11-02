# MooseLab Climate Monitor

### Initial setup

- Upload code to Arduino
- Wire up the arduino
- Wire up the Raspberry Pi (rpi)
- Plug in USB serial cable from arduino to rpi
- run `sudo raspi-config` on rpi terminal
- enable rpi serial connection (say no to remote console log in when doing this setup)
- (optional) enable rpi VNC via `raspi-config`
- (optional) disable boot to desktop
- install `DHT sensor library` via Arduino IDE through `Manage Extensions`
- Expand rpi filesystem through `raspi-config`
- Install `nodejs` apt package
- Install `npm`
- (optional) Install `nvm` via `npm`

``` bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

=> Appending nvm source string to /home/moose/.bashrc
=> Appending bash_completion source string to /home/moose/.bashrc
=> Close and reopen your terminal to start using nvm or run the following to use it now:

### Add to bash profile or oh my zsh profile:

``` bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

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
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- User access is from localhost only
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';

-- User access from any host
CREATE USER 'your_username'@'%' IDENTIFIED BY 'your_password';

-- For connections from only localhost
GRANT SELECT, INSERT, UPDATE, DELETE ON weather_data.* TO 'your_username'@'localhost';

-- For connections from any host
GRANT SELECT, INSERT, UPDATE, DELETE ON weather_data.* TO 'your_username'@'%';

-- Grant Privileges to new user for localhost
GRANT ALL PRIVILEGES ON weather_data.* TO 'your_username'@'localhost';

-- Alternative for all hosts
GRANT ALL PRIVILEGES ON weather_data.* TO 'your_username'@'%';

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

### Uncomplicated Firewall (UFW)
``` bash
sudo ufw allow ssh               # Allow SSH for remote access
sudo ufw allow http              # Allow HTTP for web traffic
sudo ufw allow https             # Allow HTTPS for secure web traffic
sudo ufw allow 3306/tcp          # Allow MySQL/MariaDB if needed
sudo ufw allow 5900              # Allow VNC if needed
sudo ufw default deny incoming   # Deny all other incoming connections
sudo ufw default allow outgoing  # Allow all outgoing connections
sudo ufw enable                  # Enable the firewall (this persists across reboots)
```