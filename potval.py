void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0,1,2:
  int sensorValueTempo = analogRead(A0);
  int sensorValueVol = analogread(A1);
  int sensorValueUntitled = analogread(A2);
  // print out the value you read:
  Serial.println(sensorValueTempo);
  Serial.println(sensorValueVol);
  Serial.println(sensorValueUntitled);
}