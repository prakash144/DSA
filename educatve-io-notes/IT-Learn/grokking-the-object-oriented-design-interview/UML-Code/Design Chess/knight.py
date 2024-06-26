class Knight(Piece):
  def __init__(self, white):
    super().__init__(white)

  def can_move(self, board, start, end):

    # we can't move the piece to a box that has a piece of the same color
    if end.get_piece().is_white() == self.is_white():
      return False

    x = abs(start.get_x() - end.get_x())
    y = abs(start.get_y() - end.get_y())
    return x * y == 2