#include <Wire.h>
#include "SparkFun_Qwiic_Button.h"

// Pin definitions
#define BUZZER_PIN 5  // Change this to match your buzzer pin connection

// Create a button object
QwiicButton button;

void setup() {
  Serial.begin(115200);
      
  // I2C_setup_for_PyQT() 
  Wire1.begin(); // TinyPico only
  //check if button will acknowledge over I2C
  while (!button.begin(0x6F, Wire1)) {
    Serial.println("Device did not acknowledge! Freezing.");
    delay(1000);
  }
  Serial.println("Button acknowledged.");

  //Start with the LED off
  button.LEDoff();

  Serial.println("spotify_button_connected");
}


void loop() {
    // Check if button is pressed
    if (button.isPressed()) {
        // Play beep
        tone(1000);  // 1000 Hz tone
        
        // Wait for button release to prevent multiple beeps
        while (button.isPressed()) {
            delay(10);
        }
        noTone();      // Stop the tone

    }
    
    delay(10);  // Small delay to prevent overwhelming the I2C bus
}