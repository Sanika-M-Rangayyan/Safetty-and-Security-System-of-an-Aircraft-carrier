// defines pins numbers
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int trigPin = 9;
const int echoPin = 10;
const int buzzer = 11;
const int seriesLedPin = 13;
const int trigPin1 = 6;
const int echoPin1 = 7;
// defines variables
long duration;
int distance;
int safetyDistance;
int count;
long duration1;
int distance1;
int safetyDistance1;
int plane=0;



//LDR DECLARATION
const int LdrLedPin = 8;   //the number of the LED pin
const int ldrPin = A0;  //the number of the LDR pin


//FLAME SENSOR
const int sensorMin = 0;     // sensor minimum
const int sensorMax = 1024;  // sensor maximum


//PIR SENSOR
int pirPin = 2;                 // PIR Out pin 
int pirStat = 0;

//WATER SENSOR
const int senmin = 0;
const int senmax = 1024;
int sensory = A2;
int i;




void setup() {

lcd.begin();

lcd.backlight();

lcd.clear();

//lcd.setCursor(4,0);
//lcd.print("SHREE");


Wire.begin();


pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(buzzer, OUTPUT);
pinMode(seriesLedPin, OUTPUT);
pinMode(trigPin1, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin1, INPUT); // Sets the echoPin as an Input

//LDR SENSOR
pinMode(LdrLedPin, OUTPUT);  //initialize the LED pin as an output
pinMode(ldrPin, INPUT);   //initialize the LDR pin as an input

//pir ssensor
pinMode(pirPin, INPUT);






Serial.begin(9600); // Starts the serial communication
}


void loop() {

//lcd.clear();

//lcd.setCursor(4,0);
//lcd.print("SHREE");

/*
lcd.setCursor(0,1);
lcd.print("RADIO");
*/


//LDR SENSOR
int ldrStatus = analogRead(ldrPin);   //read the status of the LDR value

  //check if the LDR status is <= 300
  //if it is, the LED is HIGH

if (ldrStatus>=850) {

digitalWrite(LdrLedPin, HIGH);               //turn LED on
//Serial.println("LDR is DARK, LED is ON");
    
}
else {

digitalWrite(LdrLedPin, LOW);          //turn LED off
//Serial.println("---------------");
}








//lcd.clear();
//ULTRASONIC SENSOR 1
// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;

safetyDistance = distance;
if (safetyDistance <= 5){
  digitalWrite(buzzer, HIGH);
delay(1000)  ;
    //digitalWrite(seriesLedPin, HIGH);
  lcd.setCursor(0,0);
  lcd.print("OBSTRUCTION");    

}
else{
  digitalWrite(buzzer, LOW);
  //digitalWrite(seriesLedPin, LOW);

  
}

// Prints the distance on the Serial Monitor
//Serial.print("Distance: ");
//Serial.println(distance);

//lcd.clear();
//SECOND USLRASONIC SENSOR

// Clears the trigPin
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration1 = pulseIn(echoPin1, HIGH);

// Calculating the distance
distance1= duration1*0.034/2;

safetyDistance1 = distance1;
if (safetyDistance1 <= 5)
{
  //digitalWrite(seriesLedPin, HIGH);
  //plane=1;
digitalWrite(seriesLedPin, HIGH);

delay(10000);
digitalWrite(seriesLedPin, LOW);
}



/*else{
  digitalWrite(seriesLedPin, LOW);
  
}*/


// Prints the distance on the Serial Monitor
//Serial.print("NEW PLANE ");
//Serial.println(distance);



//lcd.clear();
//FLAME SENSOR

// read the sensor on analog A1:
  int sensorReading = analogRead(A1);
  // map the sensor range (four options):
  // ex: 'long int map(long int, long int, long int, long int, long int)'
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);
  
  // range value:
  switch (range) {
  case 0:   // A fire closer than 1.5 feet away.
    //Serial.println("** Close Fire **");
    lcd.setCursor(0,1);
    lcd.print("FIRE FIRE");     
  
    digitalWrite(buzzer, HIGH);    
    delay(1000);        // ...for 1 sec
    digitalWrite(buzzer,LOW);     // Stop sound...
    delay(1000);
    break;
  case 1:    // A fire between 1-3 feet away.
    //Serial.println("** Distant Fire **");
    
    break;
  case 2:    // No fire detected.
    //Serial.println("No Fire");
    digitalWrite(buzzer,LOW);     
    break;
  }
  delay(1);  // delay between reads


//lcd.clear();
//PIR SENSOR
pirStat = digitalRead(pirPin); 
if (pirStat == HIGH) {            // if motion detected
tone(buzzer,100);
lcd.setCursor(0,1);
  lcd.print("INTRUDER"); 
//Serial.println("Some motion detected");
} 
else
{
    noTone(buzzer);
}

//lcd.clear();
//water sensor
int sensor = analogRead(sensory);
  int rangeWater = map(sensor, senmin, senmax, 0, 3);
//Serial.print("Water:");
//Serial.println(rangeWater);  
if(rangeWater==0)
{
//Serial.println("Water");
lcd.setCursor(0,0);
  lcd.print("WATER WATER"); 
digitalWrite(buzzer, HIGH);  
}
else
{
digitalWrite(buzzer,LOW );   
}
delay(500);


//TO SCAN ADDRESS
/*
byte error, address;
int Devices;
Serial.println("Scanning...");
Devices = 0;
for(address = 1; address < 127; address++ )
{

Wire.beginTransmission(address);
error = Wire.endTransmission();
if (error == 0)
{
Serial.print("I2C device found at address 0x");
if (address<16)
Serial.print("0");
Serial.print(address,HEX);
Serial.println("  !");
Devices++;
}
else if (error==4)
{
Serial.print("Unknown error at address 0x");
if (address<16)
Serial.print("0");
Serial.println(address,HEX);
}
}
if (Devices == 0)
Serial.println("No I2C devices found\n");
else
Serial.println("done\n");
delay(5000);    


*/

}
