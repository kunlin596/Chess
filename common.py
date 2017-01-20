import numpy as np

# Data sizes
FLOAT_SIZE = 4
DOUBLE_SIZE = 8
UNSIGNED_INT_SIZE = 4

# Model indices
CUBE_MODEL_INDEX = 0
CHESS_KING_MODEL_INDEX = 1
CHESS_QUEEN_MODEL_INDEX = 2
CHESS_BISHOP_MODEL_INDEX = 3
CHESS_KNIGHT_MODEL_INDEX = 4
CHESS_TOWER_MODEL_INDEX = 5
CHESS_PAWN_MODEL_INDEX = 6

# Tile enumerations
TILE_NOTSET = -1
TILE_EMPTY = 0
TILE_OCCUPIED = 1
TILE_SELECTED = 2
TILE_DESTINATION = 3
TILE_ATTACKED = 4

# Entity enumerations
BLACK_KING = 1
BLACK_QUEEN = 2
BLACK_BISHOP_1 = 3
BLACK_BISHOP_2 = 4
BLACK_KNIGHT_1 = 5
BLACK_KNIGHT_2 = 6
BLACK_TOWER_1 = 7
BLACK_TOWER_2 = 8
BLACK_PAWN_1 = 9
BLACK_PAWN_2 = 10
BLACK_PAWN_3 = 11
BLACK_PAWN_4 = 12
BLACK_PAWN_5 = 13
BLACK_PAWN_6 = 14
BLACK_PAWN_7 = 15
BLACK_PAWN_8 = 16

WHITE_KING = 21
WHITE_QUEEN = 22
WHITE_BISHOP_1 = 23
WHITE_BISHOP_2 = 24
WHITE_KNIGHT_1 = 25
WHITE_KNIGHT_2 = 26
WHITE_TOWER_1 = 27
WHITE_TOWER_2 = 28
WHITE_PAWN_1 = 29
WHITE_PAWN_2 = 30
WHITE_PAWN_3 = 31
WHITE_PAWN_4 = 32
WHITE_PAWN_5 = 33
WHITE_PAWN_6 = 34
WHITE_PAWN_7 = 35
WHITE_PAWN_8 = 36

# Player indices
PLAYER_BLACK = 0
PLAYER_WHITE = 1

# Rendering enumerations
CLEAR_COLOR = np.zeros((3,)) + 0.4

TILE_STATIC_SCALE = np.array([9.6, 0.5, 9.5])
TILE_HOVER_Y_POSITION = 1.0
TILE_HOVER_COLOR = np.array([1.0, 0.843, 0.0])

PIECE_STATIC_Y_OFFSET = 2.0
PIECE_SELECTION_Y_VALUE = 17.0
PIECE_SELECTION_SCALE = np.ones((3,)) * 20.0
PIECE_STATIC_SCALE = np.ones((3,)) * 12.0

PIECE_COLOR_PLAYER_BLACK = np.array([0.55, 0.27, 0.07])  # 139 	69 	19
PIECE_COLOR_PLAYER_WHITE = np.array([0.93, 0.88, 0.9])  # 238 	224 	229

PIECE_SELECTION_COLOR_PLAYER_BLACK = np.array([0.0, 0.41, 0.55])  # 0   104 139
PIECE_SELECTION_COLOR_PLAYER_WHITE = np.array([1.0, 0.19, 0.19])  # 255 	48 	48
