class Board:
  def __init__(self):
    self.__boxes = [[]]

  def Board(self):
    self.reset_board()

  def get_box(self, x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
      raise Exception("Index out of bound")
    return self.__boxes[x][y]

  def reset_board(self):
    # initialize white pieces
    boxes[0][0] = Box(Rook(True), 0, 0);
    boxes[0][1] = Box(Knight(True), 0, 1);
    boxes[0][2] = Box(Bishop(True), 0, 2);
    #...
    boxes[1][0] = Box(Pawn(True), 1, 0);
    boxes[1][1] = Box(Pawn(True), 1, 1);
    #...

    # initialize black pieces
    boxes[7][0] = Box(Rook(False), 7, 0);
    boxes[7][1] = Box(Knight(False), 7, 1);
    boxes[7][2] = Box(Bishop(False), 7, 2);
    #...
    boxes[6][0] = Box(Pawn(False), 6, 0);
    boxes[6][1] = Box(Pawn(False), 6, 1);
    # ...

    # initialize remaining boxes without any piece
    for i in range(2, 6):
      for j in range(0, 8):
        boxes[i][j] = Box(i, j, None)