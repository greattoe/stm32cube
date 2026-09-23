from getchar import Getchar
from serial import Serial

sp = Serial('COM3', 115200, timeout=1)

def init():
    sp.write(b'i'); print("init P/T")
    
def up():
    sp.write(b'w'); print("tilt up")
    
def down():
    sp.write(b's'); print("tilt down")
    
def left():
    sp.write(b'a'); print("pan left")
    
def right():
    sp.write(b'd'); print("pan right")
    
def main(args=None):
    try:
        kb = Getchar()
        key = ''
        while key != 'Q':

            if kb.chk_stdin():
                key = kb.getch()
                if key == 'i':
                    init()
                elif key == 'w':
                    up()
                elif key == 's':
                    down()
                elif key == 'a':
                    left()
                elif key == 'd':
                    right()
                else:
                    pass
                
                    print(key)
    except KeyboardInterrupt:
        print("Program terminated!")

if __name__ == '__main__':
    main()
    

