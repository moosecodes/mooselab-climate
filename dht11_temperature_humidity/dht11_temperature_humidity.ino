#include <DHT.h>

#define DHTTYPE DHT11
#define DHTPIN 2

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600); // Initialize serial communication
  dht.begin();        // Initialize DHT sensor
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  
  float celsius = dht.readTemperature();
  float farenheit = dht.readTemperature(true);
  float humidity = dht.readHumidity();

  if (isnan(farenheit) || isnan(humidity) || isnan(celsius))
  {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Send data
  Serial.print("FARENHEIT:");
  Serial.print(farenheit);
  Serial.print(", CELSIUS:");
  Serial.print(celsius);
  Serial.print(", HUMIDITY:");
  Serial.println(humidity);
  
  digitalWrite(LED_BUILTIN, LOW);
  
  delay(15000);
}
