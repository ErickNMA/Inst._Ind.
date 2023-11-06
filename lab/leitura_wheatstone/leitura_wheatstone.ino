void setup() 
{
  Serial.begin(4800);

  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
}

void loop() 
{
  int neg = analogRead(A1);
  int pos = analogRead(A2);
  float lum = (100-((pos-neg)/7.0));
  //Serial.print("Luminosidade: ");
  Serial.println(constrain(lum, 0, 100));
  //Serial.println("%");
}
