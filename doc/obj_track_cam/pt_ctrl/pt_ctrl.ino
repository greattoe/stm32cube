
#include <Servo.h>
Servo pan, tlt;
unsigned int pos_pan = 90;
unsigned int pos_tlt = 90;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  pan.attach(12); pan.write(pos_pan);
  tlt.attach(13);tlt.write(pos_tlt);
}

void loop() {
  if(Serial.available()>0) {
    char ch = Serial.read();
    if(ch == 'w') { /**************************** tilt up */
      if(pos_tlt - 1 >= 0)
        pos_tlt = pos_tlt - 1;
      else
        pos_tlt = 0;
    }
    
    else if(ch == 's') { /************************** tilt down */
      if(pos_tlt + 1 <= 180)
        pos_tlt = pos_tlt + 1;
      else
        pos_tlt = 180;
    }
    
    if(ch == 'a') { /*************************** pan left */
      if(pos_pan + 1 <= 180)
        pos_pan = pos_pan + 1;
      else
        pos_pan = 180;
    }
    
    else if(ch == 'd') { /************************** pan right */
      if(pos_pan - 1 >= 0)
        pos_pan = pos_pan - 1;
      else
        pos_pan = 0;
    }

    else if(ch == 'i') { /*************************** P/T init */
      pos_tlt = pos_pan = 90;
    }
    else;
    pan.write(pos_pan); tlt.write(pos_tlt);
    Serial.print("pos_pan = "); Serial.print(pos_pan); Serial.print(", ");
    Serial.print("pos_tlt = "); Serial.print(pos_tlt); Serial.println(".");
  }
}
