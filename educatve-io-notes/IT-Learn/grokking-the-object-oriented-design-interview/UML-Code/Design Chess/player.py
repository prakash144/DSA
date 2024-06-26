class Player(Account):
  def __init__(self, person, white_side=False):
    self.__person = person
    self.__white_side = white_side

  def is_white_side(self):
    return self.__white_side