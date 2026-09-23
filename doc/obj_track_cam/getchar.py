import msvcrt


class Getchar:

    def __init__(self):
        pass

    def chk_stdin(self):
        """
        Check whether a key has been pressed.

        Return:
            True  : key input exists
            False : no key input
        """
        return msvcrt.kbhit()

    def getch(self):
        """
        Read one key without pressing Enter.

        Return:
            pressed key as a string
        """
        return msvcrt.getch().decode()