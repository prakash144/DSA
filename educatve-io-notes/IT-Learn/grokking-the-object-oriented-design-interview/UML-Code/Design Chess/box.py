class Box:
  def __init__(self, piece, x, y):
    self.__piece = piece
    self.__x = x
    self.__y = y

  def get_piece(self):
    return self.__piece

  def set_piece(self, piece):
    self.__piece = piece

  def get_x(self):
    return self.__x

  def set_x(self, x):
    self.__x = x

  def get_y(self):
    return self.__y

  def set_y(self, y):
    self.__y = y