from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    vertical = [row[::-1] for row in self.img[::-1]]
    return Picture(vertical)

  def horizontalMirror(self):
    horizontal = []
    for value in self.img:
      horizontal.append(value[::-1])
    return Picture(horizontal)

  def negative(self):
      """ Devuelve un negativo de la imagen """
      negative_img = [
          "".join(self._invColor(char) for char in row)
          for row in self.img
      ]
      return Picture(negative_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    joined_img = [
        self_row + p_row
        for self_row, p_row in zip(self.img, p.img)
    ]
    return Picture(joined_img)

  def up(self, p):
      """ Devuelve una nueva figura poniendo la figura recibida como argumento
          encima de la figura actual """
      up_img = p.img + self.img
      return Picture(up_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura recibida como argumento
        sobre la figura actual """
    under_img = [
        ''.join([pc if pc != ' ' else sc for pc, sc in zip(p_line, s_line)])
        for p_line, s_line in zip(p.img, self.img)
    ]
    return Picture(under_img)

  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeated_img = [
        ''.join([line for _ in range(n)]) for line in self.img
    ]
    return Picture(repeated_img)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual debajo,
        la cantidad de veces que indique el valor de n """
    repeated_img = []
    for _ in range(n):
        repeated_img += self.img
    return Picture(repeated_img)

  #Extra: Sólo para realmente viciosos
  def rotate(self, sentido):
    """ Devuelve una figura rotada en 90 grados (horario) """
    if sentido == 'a':
        rotated_img = [''.join(row) for row in zip(*self.img[::-1])]
    elif sentido == 'h':
        rotated_img = [''.join(row[::-1]) for row in zip(*self.img)]
    else:
        raise ValueError("pámetro inválido")
    
    return Picture(rotated_img)

