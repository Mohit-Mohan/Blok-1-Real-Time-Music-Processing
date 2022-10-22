void setup() {
  Serial.begin(9600);

}



void readMatrix() {
  for (int x = 0; x < 4; x++) {
    for (int y = 0; y < 7; y++) {
      //      Serial.println(String(x)+  " "+ String(y));
      //MATRIX READ CODE
      Serial.print(01);

//      SEnds the Matrix Coord
      Serial.print(" ");
      Serial.print(x);
      Serial.print(" ");
      Serial.print(y);
      Serial.print(" ");

//      Reads in the value
      int value = random(4);

      Serial.println(value);

      delay(1);
    }
  }
}

void loop() {
  readMatrix();

  delay(1000000);
}