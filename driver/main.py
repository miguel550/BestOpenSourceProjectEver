"""This module serves to do complex Python computing"""

import sys


def main():
    """Main driver function"""

    print("=======================================================")
    print("=__________ ________    ______________________________=")
    print("=\______   \\_____  \  /   _____/\______   \_   _____/=")
    print("= |    |  _/ /   |   \ \_____  \  |     ___/|    __)_ =")
    print("= |    |   \/    |    \/        \ |    |    |        \=")
    print("= |______  /\_______  /_______  / |____|   /_______  /=")
    print("=        \/         \/        \/                   \/ =")
    print("=    The world is a happy place, you should be too    =")
    print("=======================================================")
    print("Hello World :D")
    print("The world is a happy place, you should be too")
    


def setup(write_file):
    """Setup for main driver function"""

    if write_file:
        sys.stdout = open(write_file, "w")
    main()
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    setup(None)
