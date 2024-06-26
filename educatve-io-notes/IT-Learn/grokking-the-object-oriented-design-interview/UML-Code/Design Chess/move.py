class Move:
  def is_white_side(self, player, start_box, end_box, piece_killed, castling_move=False):
    self.__player = player
    self.__start = start_box
    self.__end = end_box
    self.__piece_moved = self.__start.get_piece()
    self.__piece_killed = piece_killed
    self.__castling_move = castling_move

  def is_castling_move(self):
    return self.__castling_move

  def set_castling_move(self, castling_move):
    self.__castling_move = castling_move