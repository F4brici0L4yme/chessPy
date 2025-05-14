from chessPictures import *
from interpreter import draw

cuadro1 = square
for index in range(1,8):
    if index % 2 == 0:
        cuadro1 = cuadro1.join(square)
    else:
        cuadro1 = cuadro1.join(square.negative())

cuadro2 = square.negative()
for index in range(1,8):
    if index % 2 == 0:
        cuadro2 = cuadro2.join(square.negative())
    else:
        cuadro2 = cuadro2.join(square)
        
draw(cuadro2.up(cuadro1).up(cuadro2).up(cuadro1))


