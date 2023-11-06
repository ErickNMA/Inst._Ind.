#include <math.h>

#define PWM 5
#define A 2
#define B 3

#define res 24   //Resolução do encoder (pulsos por revolução)
#define red 1    //Redução do motor
#define ts 10    //amostragem em ms

long pulses=0;
void cont()
{
  pulses++;
}

void setup() 
{
  Serial.begin(9600);

  pinMode(PWM, OUTPUT);
  pinMode(A, INPUT);
  pinMode(B, INPUT);

  attachInterrupt(digitalPinToInterrupt(A), cont, RISING);
}

int val=((30*255)/(100.00));

unsigned long t0 = 0;

double med[5];

void loop() 
{
  if(Serial.available())
  {
    //val = int(Serial.read());
  }

  analogWrite(PWM, val);
  
  if((micros()-t0) > (ts*1e3))
  {
    float freq = ((float)pulses/((float)red*res*(ts*1e-3)));
    float rot = (freq*60);
    float vel = ((2*M_PI)*freq);
    Serial.println(rot);
    pulses = 0;
    t0 = micros();
  }
  
}
