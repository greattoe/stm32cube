#include <Servo.h>
Servo pan, tlt;
String rcv_str = "";

int pos_pan = 90;
int pos_tlt = 90;

void setup() {
  pan.attach(12);
  tlt.attach(13);
  pan.write(pos_pan);delay(15);
  tlt.write(pos_tlt);delay(15);
  rcv_str.reserve(10);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0)
  {
    char ch = Serial.read();
    if(ch != '\n') rcv_str= rcv_str + ch;
    else {
      if(rcv_str.substring(0,3) == "pan"){
        pos_pan = rcv_str.substring(3).toInt();
      }
      if(rcv_str.substring(0,3) == "tlt"){
        pos_tlt = rcv_str.substring(3).toInt();
      }
      Serial.print("pan = ");Serial.print(pos_pan);Serial.print(", ");
      Serial.print("tilt = ");Serial.println(pos_tlt);
      pan.write(pos_pan); delay(15);  tlt.write(pos_tlt); delay(15);
      rcv_str="";
      
    }    
  }
}
