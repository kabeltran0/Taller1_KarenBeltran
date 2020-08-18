# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from colorimage import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    path = input('Ingrese la ruta de la imagen:')
    name = input('Ingrese el nombre de la imagen:')
    #ruta y nombre de la imagen
    img=colorimage(path,name)
    #implementación de métodos
    img.displayProperties()
    img.makeGray()
    img.colorizeRGB('red')
    img.makeHue()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
