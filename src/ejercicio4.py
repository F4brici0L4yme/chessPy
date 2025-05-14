from chessPictures import *
from interpreter import draw

cuadro = square
for index in range(1,8):
    if index % 2 == 0:
        cuadro = cuadro.join(square)
    else:
        cuadro = cuadro.join(square.negative())
draw(cuadro)
