import pygame
import sys
from pygame.locals import *
import pieces
from colors import color, inverter

def main(): #
    pygame.init()
    TAMAÑO_TABLERO = 8
    TAMAÑO_CASILLA = 60
    ANCHO = ALTO = TAMAÑO_TABLERO * TAMAÑO_CASILLA
    
    posicion_inicial = [ #
        list("rnbqkbnr"),
        list("pppppppp"),
        list("........"),
        list("........"),
        list("........"),
        list("........"),
        list("PPPPPPPP"),
        list("RNBQKBNR"),
    ]

    ARTE_PIEZA = { #
        'b': pieces.BISHOP, 'B': pieces.BISHOP,
        'k': pieces.KING,   'K': pieces.KING,
        'n': pieces.KNIGHT, 'N': pieces.KNIGHT,
        'p': pieces.PAWN,   'P': pieces.PAWN,
        'q': pieces.QUEEN,  'Q': pieces.QUEEN,
        'r': pieces.ROCK,   'R': pieces.ROCK,
    }

    def dibujo(arte, invertir=False):
        filas = len(arte)
        columnas = len(arte[0])
        superficie = pygame.Surface((columnas, filas), pygame.SRCALPHA)
        for y, fila in enumerate(arte):
            for x, c in enumerate(fila):
                if c == ' ':
                    continue
                color_pieza = color.get(c, (0, 0, 0))
                if invertir:
                    color_pieza = color.get(inverter.get(c, c), color_pieza)
                superficie.set_at((x, y), color_pieza)
        return pygame.transform.smoothscale(superficie, (TAMAÑO_CASILLA, TAMAÑO_CASILLA))

    superficies_piezas = {}
    for simbolo, arte in ARTE_PIEZA.items():
        invertir = simbolo.islower()
        superficies_piezas[simbolo] = dibujo(arte, invertir=invertir)

    COLOR_BLANCO = (245, 245, 245)
    COLOR_OSCURO = (100, 100, 100)

    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Tablero de Ajedrez")
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get(): #
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

        for fila in range(TAMAÑO_TABLERO):
            for columna in range(TAMAÑO_TABLERO):

                sombra = (fila + columna) % 2
                color_casilla = COLOR_BLANCO if sombra == 0 else COLOR_OSCURO
                rectangulo = pygame.Rect(columna * TAMAÑO_CASILLA, fila * TAMAÑO_CASILLA, TAMAÑO_CASILLA, TAMAÑO_CASILLA)
                pygame.draw.rect(pantalla, color_casilla, rectangulo)

                simbolo = posicion_inicial[fila][columna]
                if simbolo != '.':
                    superficie = superficies_piezas.get(simbolo)
                    if superficie:
                        pantalla.blit(superficie, rectangulo)

        pygame.display.flip() #

if __name__ == '__main__':
    main()
