#!/usr/bin/python3

from scripts import starting

class principal():
    if __name__ == "__main__":
        def root():
            import sys
            if(sys.platform != "linux"):
                print("\33[41m"+"\33[34m"+"Imcompatível com esse sistema.".center(80))
            else:
                root()
