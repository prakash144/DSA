class King(Piece):
  def __init__(self, white):
    self.__castling_done = False
    super().__init__(white)

  def is_castling_done(self):
    return self.__castling_done

  def set_castling_done(self, castling_done):
    self.__castling_done = castling_done

  def can_move(self, board, start_box, end_box):
    # we can't move the piece to a box that has a piece of the same color
    if end_box.get_piece().is_white() == self.is_white():
      return False

    x = abs(start_box.get_x() - end_box.get_x())
    y = abs(start_box.get_y() - end_box.get_y())
    if x + y == 1:
      # check if self move will not result in king being attacked, if so return True
      return True

    return self.is_valid_castling(board, start_box, end_box)

  def is_valid_castling(self, board, start, end):

    if self.is_castling_done():
      return False

    # check for the white king castling
    if self.is_white() and start.get_x() == 0 and start.get_y() == 4 and end.get_y() == 0:
      # confirm if white king moved to the correct ending box
      if abs(end.get_y() - start.get_y()) == 2:
        # check if there the Rook is in the correct position
        # check if there is no piece between Rook and the King
        # check if the King or the Rook has not moved before
        # check if self move will not result in king being attacked
        # ...
        self.set_castling_done(True)
        return True

    else:
      # check for the black king castling
      self.set_castling_done(True)
      return True

    return False

  def is_castling_move(self, start, end):
    # check if the starting and ending position are correct
    None