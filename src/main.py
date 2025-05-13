from interpreter import draw
from chessPictures import *
from time import sleep

draw(square.negative().under(knight).join(square.under(bishop)).up(square.horizontalRepeat(4)).verticalRepeat(4).rotate('a'))
