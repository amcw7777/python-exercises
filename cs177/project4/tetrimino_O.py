from tetrimino import *

class Tetrimino_O( Tetrimino ):
    # TASK 2:
    #
    # Constructor function of Tetrimino_O.
    # This function sets self.coordinates with the initial values.
    #
    # If self.tetris_window.num_blocks_x is even:
    #     The tetrimino should be perfectly in the center two columns.
    # Else:
    #     The tetrimino should be positioned near the center but closer to right
    #
    # You need to use these member variables/functions:
    #
    # self.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    #          (You will generate this list.)
    # self.tetris_window.block_size: Size of the blocks, type: Integer
    # self.tetris_window.num_blocks_x: Number of blocks in x direction, type: Integer
    # self.tetris_window.num_blocks_y: Number of blocks in y direction, type: Integer
    #
    # Please see images/initial_tetrimino_O_01.png,
    #            images/initial_tetrimino_O_02.png,
    #            images/initial_tetrimino_O_03.png,
    #            images/initial_tetrimino_O_04.png
    #
    # and their corresponding parameters in images/data.txt
    #
    # (Tetrimino_I and Tetrimino_J is given to you. Please look at them before you
    #  start this task.)
    # 
    def __init__( self, tetris_window  ):
        # Your code starts here.

        super().__init__( tetris_window )
        bs = self.tetris_window.block_size
        num_x = self.tetris_window.num_blocks_x
        num_y = self.tetris_window.num_blocks_y
        x = ( num_x // 2) * bs + bs // 2
        y = bs // 2
        self.coordinate = [ (x,y),(x+bs,y),(x+bs,y+bs),(x,y+bs) ]

        # Your code ends here.

    # This function is given.
    #
    # We do not need to do anything in this function because
    # tetrimino_O has only one state hence we do not need to rotate it.
    #
    def rotate( self ):
        pass

    def get_color( self ):
        return (0,0,255)
