from getchar import Getchar

def main(args=None):
    kb  = Getchar()
    key = ''
    
    while key!='Q':
        old_key = ''
        key = kb.getch()
        if key != old_key:
            print(key)
            old_key = key

if __name__ == '__main__':
    main()
    

