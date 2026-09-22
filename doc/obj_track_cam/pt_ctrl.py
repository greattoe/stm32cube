from getchar import Getchar
import serial

sp  = serial.Serial('COM3', 9600, timeout=1)

pan = tlt = 90
sp.write(("pan" + str(pan) + "\n").encode())
sp.write(("tlt" + str(tlt) + "\n").encode())

def main(args=None):
    global pan; global tlt
    kb  = Getchar()
    old_key = ''
    key = ' '
    
    while key!='Q': 
        key = kb.getch()
        if key != old_key:
            if key == 'w':
                if tlt - 5 >= 0:
                    tlt = tlt - 5
                else:
                    tlt = 0
            elif key == 's':
                if tlt + 5 <= 180:
                    tlt = tlt + 5
                else:
                    tlt = 180
            elif key == 'a':
                if pan + 5 <= 180:
                    pan = pan + 5
                else:
                    pan = 180
            elif key == 'd':
                if pan - 5 >= 0:
                    pan = pan - 5
                else:
                    pan = 0
            elif key == '1':
                pan = tlt = 90; print("PT Position Initialized!")
            sp.write(("pan" + str(pan) + "\n").encode())
            sp.write(("tlt" + str(tlt) + "\n").encode())
            print("pan = ", end="");print(pan, end='')
            print(" , tilt = ", end='');print(tlt)
            old_key = key
            
        else:   pass
    print("Program Terminated!")
        
if __name__ == '__main__':
    main()