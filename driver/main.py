"""This module serves to do complex Python computing"""

import sys


def main():
    """Main driver function"""

    print("Hello World :D")


def setup(write_file):
    """Setup for main driver function"""

    if write_file:
        sys.stdout = open(write_file, "w")
    main()
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    setup(None)
