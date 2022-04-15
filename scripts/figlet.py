from pyfiglet import Figlet

import sys

def art():
    if(sys.platform == "linux"):
        f = Figlet(font='big')
        for cont in range(1,5):
            try:
                texto = open("Frases/"+str(cont)+".txt","r")
                frase = texto.read()
                print(frase)
                texto.close()
            except:
                sys.exit()
            finally:
                print(f.renderText("Morpheus"))
    else:
        print("\nLinux is better!".center(80))
art()
