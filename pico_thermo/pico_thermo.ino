#include <Wire.h>
#include "Adafruit_ADT7410.h" //you need this library

// Create the ADT7410 temperature sensor object
Adafruit_ADT7410 tempsensor = Adafruit_ADT7410();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
  
  Wire.setSDA(20);
  Wire.setSCL(21);
  Wire.begin();
  
    if (!tempsensor.begin()) {
   
    while (1){ 
      Serial.println("Couldn't find ADT7410!");
      delay(1000);
      };
  }
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  float c = tempsensor.readTempC();
  Serial.println(c);
  delay(1000);

}
