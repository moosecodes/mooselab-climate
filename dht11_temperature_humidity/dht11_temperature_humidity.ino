#include <DHT.h>

#define DHTTYPE DHT11
#define DHTPIN 2

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600); // Initialize serial communication
  dht.begin();        // Initialize DHT sensor
}

void loop()
{
  delay(2000);

  float celcius = dht.readTemperature();
  float farenheit = dht.readTemperature(true);
  float humidity = dht.readHumidity();

  if (isnan(celcius) || isnan(humidity))
  {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Send data in "TEMP:xx.x,HUM:yy.y" format
  Serial.print("CELCIUS:");
  Serial.print(celcius);
  Serial.print(", FARENHEIT:");
  Serial.print(farenheit);
  Serial.print(", HUMIDITY:");
  Serial.println(humidity);
  delay(60000);
}
