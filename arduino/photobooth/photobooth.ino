// NeoPixelTest
// This example will cycle between showing four pixels as Red, Green, Blue, White
// and then showing those pixels as Black.
//
// Included but commented out are examples of configuring a NeoPixelBus for
// different color order including an extra white channel, different data speeds, and
// for Esp8266 different methods to send the data.
// NOTE: You will need to make sure to pick the one for your platform 
//
//
// There is serial output of the current state so you can confirm and follow along
//

#include <NeoPixelBus.h>

const uint16_t PixelCount = 124; // this example assumes 4 pixels, making it smaller will cause a failure
const uint8_t PixelPin = 6;  // make sure to set this to the correct pin, ignored for Esp8266
const uint16_t PixelHeight = 31;
#define colorSaturation 128



// four element pixels, RGBW
NeoPixelBus<NeoRgbwFeature, Neo800KbpsMethod> strip(PixelCount, PixelPin);

unsigned long last_call;
bool reset_b;
bool run_idle;

char red[PixelCount];
char blue[PixelCount];
char green[PixelCount];

void setup()
{
    Serial.begin(115200);
    while (!Serial); // wait for serial attach

    Serial.println();
    Serial.println("Initializing...");
    Serial.flush();

    // this resets all the neopixels to an off state
    strip.Begin();
    strip.Show();

    Serial.println();
    Serial.println("Running...");

    for(int i=0; i<PixelCount; i++) {
      red[i] = 0;
      blue[i] = 0;
      green[i] = 0;
    }

    run_idle = true;
}

void flash() {
  for(int i = 0; i<PixelCount; i++) {
    strip.SetPixelColor(i, RgbwColor(20, 0, 0, 255));
  }
  strip.Show();
  
   for(int i = 0; i<PixelCount; i++) {
    strip.SetPixelColor(i, RgbwColor(0, 0, 0));
  }
  delay(500);
  strip.Show();
}

void countdown(int sec) {

  int brightness = 30;

  RgbwColor c(0, 0, 0, brightness);

  for(int i = 0; i<PixelCount; i++) {

    int pos = i % PixelHeight;

    if(pos < (15-sec) || pos >= (PixelHeight - (15-sec)) || sec <= 0) {
      strip.SetPixelColor(i, RgbwColor(0, 0, 0, brightness));
    } else {
      strip.SetPixelColor(i, RgbwColor(0, 0, 0));
    }
    
  }
  
   strip.Show();
}

void idle() {

  static float bright;
  static bool dir;
    
  for(int i = 0; i<PixelCount; i++) {  
    strip.SetPixelColor(i, HsbColor(0.75, 1.0, bright));    
  }

  strip.Show();

  if(bright <= 0.05) dir=true;
  if(bright >= 0.15) dir=false;

  if(dir) {
    bright+=0.002;
  } else {
    bright-=0.002;
  }
}

void readInput() {
  int c = 0;
  for(int i=0; i<PixelCount; i++) {
    
    c = Serial.read();
    if(c < 0) return;
    red[i] = c;

    c = Serial.read();
    if(c < 0) return;
    green[i] = c;

    c = Serial.read();
    if(c < 0) return;
    blue[i] = c;
    
  }
}

void showInput() {

  for(int i=0; i<PixelCount; i++) {
    strip.SetPixelColor(i, RgbColor(red[i], green[i], blue[i]));  
  }
  strip.Show();
}

void effect() {
  effect(0);
}
void effect(bool init) {

  static float pos = 0;
  static float brightness = 0;

  for(int i = 0; i<PixelCount; i++) {
    float x = float(i / 31) / 4;
    float y = float(i % 31) / 31.0;

    int val = int(i + (pos * float(PixelCount))) % PixelCount;
    
    strip.SetPixelColor(i, HsbColor(float(val) / float(PixelCount), 1.0, brightness));    
  }

  strip.Show();

  pos = pos + 0.002;
  
  if(pos >= 1) {
    pos = 0;
  }

  brightness = brightness + 0.001;
  if(brightness > 0.2) {
    brightness = 0.2;
  }

  if(init == true) {
    brightness = 0;
  }
}

void loop()
{

  int c = 0;
 
    if(Serial.available()) {
      c = Serial.read();
      run_idle = false;

      if(c > 0 ) {

        if(c == 'f') flash();
        if(c == 'i') run_idle=true;
        if(c == 'c') {
          c = Serial.read();
          switch(c) {
            case 'a': countdown(11);
                break;
            case '9': countdown(10);
                break;
            case '8': countdown(9);
                break;
            case '7': countdown(8);
                break;
            case '6': countdown(7);
                break;
            case '5': countdown(6);
                break;
            case '4': countdown(5);
                break;
            case '3': countdown(4);
                break;
            case '2': countdown(3);
                break;
            case '1': countdown(2);
                break;
            case '0': countdown(1);
                break;
          }
        
        }

        if(c == 'W') {
          readInput();
        }

        if(c == 'S') {
          showInput();
        }
      }

      last_call = millis();
      reset_b = true;
    }

    if(run_idle) idle();

    if((millis() - last_call) > 120000) {
      effect(reset_b);
      run_idle = false;
      reset_b = false;
    }
    
   delay(20);

}
