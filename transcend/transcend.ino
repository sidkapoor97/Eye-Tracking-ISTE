ldr_right_pin=A0
ldr_left_pin=A1
ldr_center_pin=A2
ldr_rev_pin=A3

//Motor A is in left direction
const int motor_a_pos  = 5;  // Pin 14 of L293
const int motor_a_neg  = 6;  // Pin 10 of L293
//Motor B is in right direction
const int motor_b_pos  = 10; // Pin  7 of L293
const int motor_b_neg  = 9;  // Pin  2 of L293

void setup() {
  // put your setup code here, to run once:
pinMode(ldr_right,input);
pinMode(ldr_left,input);
pinMode(ldr_center,input);
pinMode(ldr_rev,input);
pinMode(motor_a_pos, OUTPUT);
pinMode(motor_a_neg, OUTPUT);
pinMode(motor_b_pos, OUTPUT);
pinMode(motor_b_neg, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

ldr_right=analogRead(ldr_right_pin)
ldr_left=analogRead(ldr_right_pin
ldr_center=analogRead(ldr_center_pin)
ldr_rev=analogRead(ldr_rev_pin)

if(ldr_right>threshold)
{
  digitalWrite(motor_a_pos,LOW)
  digitalWrite(motor_a_neg,LOW)
  digitalWrite(motor_b_pos,HIGH)
  digitalWrite(motor_b_neg,LOW)
}

if(ldr_left>threshold)
{
  digitalWrite(motor_a_pos,HIGH)
  digitalWrite(motor_a_neg,LOW)
  digitalWrite(motor_b_pos,LOW)
  digitalWrite(motor_b_neg,LOW)
}

if(ldr_center>threshold)
{
  digitalWrite(motor_a_pos,HIGH)
  digitalWrite(motor_a_neg,LOW)
  digitalWrite(motor_b_pos,HIGH)
  digitalWrite(motor_b_neg,LOW)
}

if(ldr_right>threshold)
{
  digitalWrite(motor_a_pos,LOW)
  digitalWrite(motor_a_neg,HIGH)
  digitalWrite(motor_b_pos,LOW)
  digitalWrite(motor_b_neg,HIGH)
}

}
