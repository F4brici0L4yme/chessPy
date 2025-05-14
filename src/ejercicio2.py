from chessPictures import *
from interpreter import draw

knight1 = knight
knight2 = knight.negative()

fila1 = knight1.join(knight2)
fila2 = knight1.join(knight2).horizontalMirror()
cuadro_b = fila2.up(fila1)
draw(cuadro_b)