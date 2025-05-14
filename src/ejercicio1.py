from chessPictures import *
from interpreter import draw
knight1 = knight
knight2 = knight.negative()

fila1 = knight1.join(knight2)
fila2 = knight2.join(knight1)
cuadro_a = fila1.up(fila2)
draw(cuadro_a)