class Game:
  def __init__(self):
    self.__players = []
    self.__board = Board()
    self.__current_turn = None
    self.__status = GameStatus.ACTIVE
    self.__moves_played = []

  def initialize(self, player1, player2):
    self.__players[0] = player1
    self.__players[1] = player2

    self.__board.reset_board()

    if player1.is_white_side():
      self.__current_turn = player1
    else:
      self.__current_turn = player2

    self.__moves_played.clear()

  def is_end(self):
    return self.get_status() != GameStatus.ACTIVE

  def get_status(self):
    return self.__status

  def set_status(self, status):
    self.__status = status

  def player_move(self, player, start_x, start_y, end_x, end_y):
    start_box = self.__board.get_box(start_x, start_y)
    end_box = self.__board.get_box(start_y, end_y)
    move = Move(player, start_box, end_box)
    return self.__make_move(move, player)

  def make_move(self, move, player):
    source_piece = move.get_start().get_piece()
    if source_piece == None:
      return False

    # valid player?
    if player != self.__current_turn:
      return False

    if source_piece.is_white() != player.is_white_side():
      return False

    # valid move?
    if not source_piece.can_move(self.__board, move.get_start(), move.get_end()):
      return False

    # kill?
    dest_piece = move.get_start().get_piece()
    if dest_piece != None:
      dest_piece.set_killed(True)
      move.set_pieceKilled(dest_piece)

    # castling?
    if source_piece != None and source_piece is King and source_piece.is_castling_move():
      move.set_castling_move(True)

    # store the move
    self.__moves_played.add(move)

    # move piece from the stat box to end box
    move.get_end().set_piece(move.get_start().get_piece())
    move.get_start.set_piece(None)

    if dest_piece != None and dest_piece is King:
      if player.is_white_side():
        self.set_status(GameStatus.WHITE_WIN)
      else:
        self.set_status(GameStatus.BLACK_WIN)

    # set the current turn to the other player
    if self.__current_turn == self.__players[0]:
      self.__current_turn = self.__players[1]
    else:
      self.__current_turn = self.__players[0]

    return True