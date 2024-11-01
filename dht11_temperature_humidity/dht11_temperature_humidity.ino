#include <DHT.h>

// Define the DHT sensor type
#define DHTTYPE DHT11

// Define the digital pin connected to the DHT sensor
#define DHTPIN 2

// Initialize DHT sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); // Begin serial communication
  dht.begin();        // Initialize DHT sensor
}

void loop() {
  delay(2000); // Wait 2 seconds between readings

  // Read temperature as Celsius
  float temperature = dht.readTemperature();
  // Read humidity
  float humidity = dht.readHumidity();

  // Check if any reads failed
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Print results to the serial monitor
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  // Optional: Print temperature in Fahrenheit
  float fahrenheit = dht.readTemperature(true);
  Serial.print("Temperature: ");
  Serial.print(fahrenheit);
  Serial.println(" °F");
}
