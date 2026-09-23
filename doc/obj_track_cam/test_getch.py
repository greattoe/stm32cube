from getchar import Getchar

def main(args=None):
    print("Type any Key!(Type'Q' for quit this Program)\n")
    kb = Getchar()
    key = ''

    while key != 'Q':

        if kb.chk_stdin():
            key = kb.getch()
            print(key, end="", flush=True)


if __name__ == '__main__':
    main()