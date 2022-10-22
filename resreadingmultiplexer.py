/* 
Modified on Nov 28, 2020
Modified by MehranMaleki from Arduino Examples
Home
*/


//Mux control pins
int s0 = 5;
int s1 = 4;
int s2 = 3;
int s3 = 2;

int sensorValue = 0;       // sensorPin default value
int sensorValue1 = 0;       // sensorPin default value
float Vin = 5;             // Input voltage
float Vout = 0;            // Vout default value
float Rref = 1000;          // Reference resistor's value in ohms (you can give this value in kiloohms or megaohms - the resistance of the tested resistor will be given in the same units)
float R = 0;               // Tested resistors default value
float R1 = 0;               // Tested resistors default value


//Mux in "SIG" pin
int SIG_pin = 0;


void setup(){
  pinMode(s0, OUTPUT); 
  pinMode(s1, OUTPUT); 
  pinMode(s2, OUTPUT); 
  pinMode(s3, OUTPUT); 

  digitalWrite(s0, LOW);
  digitalWrite(s1, LOW);
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);

  Serial.begin(9600);
}


void loop(){

  //Loop through and read all 16 values
  for(int i = 0; i < 16; i ++){
    Serial.print("Value at channel");
    Serial.print(i);
    Serial.print("is :");
    Serial.println(readMux(i));
    delay(1000);
  }

}


float readMux(int channel){
  int controlPin[] = {s0, s1, s2, s3};

  int muxChannel[16][4]={
    {0,0,0,0}, //channel 0
    {1,0,0,0}, //channel 1
    {0,1,0,0}, //channel 2
    {1,1,0,0}, //channel 3
    {0,0,1,0}, //channel 4
    {1,0,1,0}, //channel 5
    {0,1,1,0}, //channel 6
    {1,1,1,0}, //channel 7
    {0,0,0,1}, //channel 8
    {1,0,0,1}, //channel 9
    {0,1,0,1}, //channel 10
    {1,1,0,1}, //channel 11
    {0,0,1,1}, //channel 12
    {1,0,1,1}, //channel 13
    {0,1,1,1}, //channel 14
    {1,1,1,1}  //channel 15
  };

  //loop through the 4 sig
  for(int i = 0; i < 4; i ++){
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(SIG_pin);
  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value
  Serial.print("R: ");                  
  Serial.println(R);                    // Give calculated resistance in Serial Monitor

  return R;
}