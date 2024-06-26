from abc import ABC, abstractmethod

class Piece(ABC):
  def __init__(self, white=False):
    self.__killed = False
    self.__white = white

  def is_white(self):
    return self.__white

  def set_white(self, white):
    self.__white = white

  def is_killed(self):
    return self.__killed

  def set_killed(self, killed):
    self.__killed = killed

  def can_move(self, board, start_box, end_box):
    None