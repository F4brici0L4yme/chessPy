from interpreter import draw
from chessPictures import *
from time import sleep

d1 = draw(square.negative().under(knight).join(square.under(bishop)).up(square.horizontalRepeat(4)))

