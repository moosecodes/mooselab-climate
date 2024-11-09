db_config = {
    'host': 'localhost',
    'user': 'rpidbuser',
    'password': 'a',
    'database': 'weather_data'
}

insert_dht11_query = "INSERT INTO weather_data.readings (farenheit, celsius, humidity) VALUES (%s, %s, %s)"