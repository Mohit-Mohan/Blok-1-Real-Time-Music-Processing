//Wiring Numbers
const byte play_pin = 2;
const byte stop_pin = 3;
int volume_pin = A15;
int tempo_pin = A14;

int ms10 = 7;
int ms11 = 6;
int ms12 = 5;
int ms13 = 4;
int ms1SIG_pin = A0;

int ms20 = 26;
int ms21 = 27;
int ms22 = 28;
int ms23 = 29;
int ms2SIG_pin = A1;

int ms30 = 30;
int ms31 = 31;
int ms32 = 32;
int ms33 = 33;
int ms3SIG_pin = A2;

int ms40 = 34;
int ms41 = 35;
int ms42 = 36;
int ms43 = 37;
int ms4SIG_pin = A3;

int ms50 = 38;
int ms51 = 39;
int ms52 = 40;
int ms53 = 41;
int ms5SIG_pin = A4;

int ms60 = 42;
int ms61 = 43;
int ms62 = 44;
int ms63 = 45;
int ms6SIG_pin = A5;

volatile bool play_pressed = false;
volatile bool stop_pressed = false;
int volume_val = 0;
int tempo_val = 0;
float Rref = 10000;
float R = 0;      // Tested resistors default value
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

void setup() {
  Serial.begin(9600);

  pinMode(ms10, OUTPUT);
  pinMode(ms11, OUTPUT);
  pinMode(ms12, OUTPUT);
  pinMode(ms13, OUTPUT);

  pinMode(ms20, OUTPUT);
  pinMode(ms21, OUTPUT);
  pinMode(ms22, OUTPUT);
  pinMode(ms23, OUTPUT);

  pinMode(ms30, OUTPUT);
  pinMode(ms31, OUTPUT);
  pinMode(ms32, OUTPUT);
  pinMode(ms33, OUTPUT);

  pinMode(ms40, OUTPUT);
  pinMode(ms41, OUTPUT);
  pinMode(ms42, OUTPUT);
  pinMode(ms43, OUTPUT);

  pinMode(ms50, OUTPUT);
  pinMode(ms51, OUTPUT);
  pinMode(ms52, OUTPUT);
  pinMode(ms53, OUTPUT);

  digitalWrite(ms10, LOW);
  digitalWrite(ms11, LOW);
  digitalWrite(ms12, LOW);
  digitalWrite(ms13, LOW);

  digitalWrite(ms20, LOW);
  digitalWrite(ms21, LOW);
  digitalWrite(ms22, LOW);
  digitalWrite(ms23, LOW);

  digitalWrite(ms30, LOW);
  digitalWrite(ms31, LOW);
  digitalWrite(ms32, LOW);
  digitalWrite(ms33, LOW);

  digitalWrite(ms40, LOW);
  digitalWrite(ms41, LOW);
  digitalWrite(ms42, LOW);
  digitalWrite(ms43, LOW);

  digitalWrite(ms50, LOW);
  digitalWrite(ms51, LOW);
  digitalWrite(ms52, LOW);
  digitalWrite(ms53, LOW);

  pinMode(play_pin, INPUT_PULLUP);
  pinMode(stop_pin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(play_pin), play_button, RISING);
  attachInterrupt(digitalPinToInterrupt(stop_pin), stop_button, RISING);
}

void loop() {
  if (play_pressed == 1) {
    //    do stuff

    //    Set tempo map it to value range and then send via serial
    tempo_command(tempo_to_time(map(analogRead(tempo_pin), 0, 1023, 60, 300)));
    //    Set volume map it to value range and then send via serial
    volume_command(map(analogRead(volume_pin), 0, 1023, 0, 100));

    read_matrix();


    //send serial command to MAX to start playing
    start_command(1);
    play_pressed = false;
  }
  if (stop_pressed  == 1) {
    stop_command();
    stop_pressed = false;
  }
}

float readMux1(int gridnum) {
  int channel = gridnum % 16;
//  Serial.println(channel);
  int controlPin[] = {ms10, ms11, ms12, ms13};

  //loop through the 4 sig
  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(ms1SIG_pin);

  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value

  return R;
}

float readMux2(int gridnum) {
  int channel = gridnum % 16;
//  Serial.println(channel);
  int controlPin[] = {ms20, ms21, ms22, ms23};

  //loop through the 4 sig
  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(ms2SIG_pin);

  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value

  return R;
}

float readMux3(int gridnum) {
  int channel = gridnum % 16;
//  Serial.println(channel);
  int controlPin[] = {ms30, ms31, ms32, ms33};

  //loop through the 4 sig
  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(ms3SIG_pin);

  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value

  return R;
}

float readMux4(int gridnum) {
  int channel = gridnum % 16;
//  Serial.println(channel);
  int controlPin[] = {ms40, ms41, ms42, ms43};

  //loop through the 4 sig
  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(ms4SIG_pin);

  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value

  return R;
}

float readMux5(int gridnum) {
  int channel = gridnum % 16;
//  Serial.println(channel);
  int controlPin[] = {ms50, ms51, ms52, ms53};

  //loop through the 4 sig
  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(ms5SIG_pin);

  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value

  return R;
}

float readMux6(int gridnum) {
  int channel = gridnum % 16;
//  Serial.println(channel);
  int controlPin[] = {ms60, ms61, ms62, ms63};

  //loop through the 4 sig
  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  //read the value at the SIG pin
  int val = analogRead(ms6SIG_pin);

  Vout = (Vin * val) / 1023;    // Convert Vout to volts
  R = Rref * (1 / ((Vin / Vout) - 1));  // Formula to calculate tested resistor's value

  return R;
}

int readCoord(int x, int y) {
  int number = (12 * y) + x;
//  Serial.println(String(x) + " " + String(y) + " " + String(number));
  if ( 0 <= number and number <= 15) {
    return readMux1(number);
  } else if (16 <= number and number <= 31) {
    return readMux2(number);
  } else if (32 <= number and number <= 47) {
    return readMux3(number);
  } else if (48 <= number and number <= 63) {
    return readMux4(number);
  } else if (64 <= number and number <= 79) {
    return readMux5(number);
  } else if (80 <= number and number <= 83) {
    return readMux6(number);
  }
}

void read_matrix() {
  for (int y = 0; y < 7; y++) {
    for (int x = 0; x < 12; x++) {
      int value = readCoord(x, y);

      Serial.print("01");

      //      Sends the Matrix Coord
      Serial.print(" ");
      Serial.print(x);
      Serial.print(" ");
      Serial.print(y);
      Serial.print(" ");

      //      Reads in the value


      Serial.println(value);

      delay(1);
    }
  }
}

int random_block(int value) {
  return random(0,4);
}

int block_translator(int value) {
  //  18K -> 1
  if ( 17000 <= value and value <= 19000) {
    return 1;
    //  25K -> 2
  } else if (24000 <= value and value <= 26000) {
    return 2;
    //  47K -> 3
  } else if (46000 <= value and value <= 48000) {
    return 3;
    //  35? K -> 4
  } else if (34000 <= value and value <= 36000) {
    return 4;
  } else {
    return 0;
  }
}

int tempo_to_time(int tempo) {
  return 60000 / tempo;
}

void tempo_command(int tempo) {
  Serial.print("02");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.println(tempo);

  delay(1);
}

void volume_command(int volume) {
  Serial.print("03");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.println(volume);

  delay(1);
}

void start_command(int command) {
  Serial.print("05");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.println(command);

  delay(1);
}

void stop_command() {
  Serial.print("0");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.print("0");
  Serial.print(" ");
  Serial.println("0");
}

void stop_button() {
  stop_pressed = true;
}

void play_button() {
  play_pressed = true;
}