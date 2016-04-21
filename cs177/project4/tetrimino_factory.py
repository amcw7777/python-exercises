import random

from tetrimino_I import *
from tetrimino_J import *
from tetrimino_L import *
from tetrimino_O import *
from tetrimino_S import *
from tetrimino_T import *
from tetrimino_Z import *

# This class is given.
class TetriminoFactory( object ):
    def __init__( self, tetris_window ):
        self.tetris_window = tetris_window

    def get_random_object( self ):
        return random.choice( [Tetrimino_I( self.tetris_window ),
                               Tetrimino_J( self.tetris_window ),
                               Tetrimino_L( self.tetris_window ),
                               Tetrimino_O( self.tetris_window ),
                               Tetrimino_S( self.tetris_window ),
                               Tetrimino_T( self.tetris_window ),
                               Tetrimino_Z( self.tetris_window ),
                              ]
                            )
