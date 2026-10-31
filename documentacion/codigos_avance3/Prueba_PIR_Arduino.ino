const int MOTION_PIN = 2; // Pin conectado al sensor PIR

void setup() {
  Serial.begin(9600);

  pinMode(MOTION_PIN, INPUT_PULLUP);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  int proximity = digitalRead(MOTION_PIN);
  Serial.write(proximity);

  if (proximity == LOW)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Motion detected!");
  }
  else
  {
    digitalWrite(LED_BUILTIN, LOW);
  }

  delay(1000);
}
