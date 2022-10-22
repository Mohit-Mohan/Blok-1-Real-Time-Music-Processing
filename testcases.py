float Rref = 1000;
float R = 0;               // Tested resistors default value
float R1 = 0;               // Tested resistors default value

float Vin = 5;             // Input voltage
float Vout = 0;            // Vout default value

int muxChannel[16][4] = {
  {0, 0, 0, 0}, //channel 0
  {1, 0, 0, 0}, //channel 1
  {0, 1, 0, 0}, //channel 2
  {1, 1, 0, 0}, //channel 3
  {0, 0, 1, 0}, //channel 4
  {1, 0, 1, 0}, //channel 5
  {0, 1, 1, 0}, //channel 6
  {1, 1, 1, 0}, //channel 7
  {0, 0, 0, 1}, //channel 8
  {1, 0, 0, 1}, //channel 9
  {0, 1, 0, 1}, //channel 10
  {1, 1, 0, 1}, //channel 11
  {0, 0, 1, 1}, //channel 12
  {1, 0, 1, 1}, //channel 13
  {0, 1, 1, 1}, //channel 14
  {1, 1, 1, 1} //channel 15
};

const byte startpin = 2;
const byte stoppin = 3;

//PIN out for Mux 1
int ms10 = 22;
int ms11 = 23;
int ms12 = 24;
int ms13 = 25;
int ms1SIG_pin = 0;


float readMux1(int gridnum) {
  int channel = gridnum % 16;
  int controlPin[] = {ms10, ms11, ms12, ms13};

  //loop through the 4 sig
  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(ms1SIG_pin);

  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value
  Serial.print("R:");
  Serial.println(R);                    // Give calculated resistance in Serial Monitor

  return R;
}

void setup() {
  Serial.begin(9600);

  attachInterrupt(digitalPinToInterrupt(interruptPin), blink, CHANGE);

  //  MUX 1 Setup
  pinMode(ms10, OUTPUT);
  pinMode(ms11, OUTPUT);
  pinMode(ms12, OUTPUT);
  pinMode(ms13, OUTPUT);

  digitalWrite(ms10, LOW);
  digitalWrite(ms11, LOW);
  digitalWrite(ms12, LOW);
  digitalWrite(ms13, LOW);

  pinMode(startpin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(startpin), play_pressed, RISING);
}

void start() {
  state = !state;
}

int VolumePot() {

}

int TempoPot() {

}

int readCoord(int x, int y) {
  int number = (12 * y) + x;

  if ( 0 <= number <= 15) {
    Serial.println("read Plexer 1");
    //    function to read mux ^
  } else if (16 <= number <= 31) {
    Serial.println("read Plexer 2");
    //    function to read mux ^
  } else if (32 <= number <= 47) {
    Serial.println("read Plexer 3");
    //    function to read mux ^
  } else if (48 <= number <= 63) {
    Serial.println("read Plexer 4");
    //    function to read mux ^
  } else if (64 <= number <= 79) {
    Serial.println("read Plexer 5");
    //    function to read mux ^
  } else if (80 <= number <= 83) {
    Serial.println("read Plexer 6");
    //    function to read mux ^
  }
}

void readMatrix() {
  for (int x = 0; x < 12; x++) {
    for (int y = 0; y < 7; y++) {
      //      Serial.println(String(x)+  " "+ String(y));
      //MATRIX READ CODE
      Serial.print(01);

      //      Sends the Matrix Coord
      Serial.print(" ");
      Serial.print(x);
      Serial.print(" ");
      Serial.print(y);
      Serial.print(" ");

      //      Reads in the value
      int value = readCoord(x, y);

      Serial.println(value);

      delay(1);
    }
  }
}

void play_pressed(){
  
}

void loop() {
  readMatrix();
  delay(1000000);
}