db_config = {
    'host': 'localhost',
    'user': 'rpidbuser',
    'password': 'a',
    'database': 'weather_data'
}

insert_dht11_query = "INSERT INTO readings (farenheit, celsius, humidity) VALUES (%s, %s, %s)"