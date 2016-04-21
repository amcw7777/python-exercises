from tetrimino import *

# This class is given to you.
class Tetrimino_I( Tetrimino ):
    # Constructor function of Tetrimino_I.
    # This function sets self.coordinates with the initial values.
    #
    # If self.tetris_window.num_blocks_x is odd:
    #     The tetrimino should be perfectly in the center column
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
    # Please see images/initial_tetrimino_I_01.png,
    #            images/initial_tetrimino_I_02.png,
    #            images/initial_tetrimino_I_03.png,
    #            images/initial_tetrimino_I_04.png
    #
    # and their corresponding parameters in images/data.txt
    # 
    def __init__( self, tetris_window  ):
        super().__init__( tetris_window )
        bs,num_x,num_y = self.tetris_window.block_size,self.tetris_window.num_blocks_x, self.tetris_window.num_blocks_y
        x,y = ( num_x // 2 ) * bs + bs // 2, bs // 2
        self.coordinates = [ (x,y),(x,y+bs), (x,y+2*bs),(x,y+3*bs) ]

    # This function rotates the tetrimino.
    #
    # Tetrimino_I has two states. (0 and 1)
    # 
    # You should first rotate the tetrimino according to self.state and 
    # update self.coordinates if:
    #
    # (1) All the updated coordinates are inside the window, and,
    # (2) None of the new coordinates have any collision with the landed objects.
    #
    # You need to use these member variables/functions:
    #
    # self.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    #          (You should update this list if necessary.)
    # self.tetris_window.block_size: Size of the blocks, type: Integer
    # self.state: The state of the tetrimino, type: Integer
    #          (You should update self.state if necessary.)
    # self.tetris_window.all_inside()
    # self.tetris_window.has_collision_with_landed_objects()
    # 
    # Please see  images/tetrimino_I_01_state_00.png
    #             images/tetrimino_I_01_state_01.png
    #             images/tetrimino_I_02_state_00.png
    #             images/tetrimino_I_02_state_01.png
    # 
    # and their corresponding parameters in images/data.txt
    #
    def rotate( self ):
        bs = self.tetris_window.block_size
        if self.state == 0:
            x,y = self.coordinates[1]
            temp = [ (x - 2 * bs, y), (x - 1 * bs, y ), (x,y), (x + bs, y) ]
        elif self.state == 1:
            x,y = self.coordinates[2]
            temp = [ (x, y - 1 * bs), (x, y), (x,y + bs), (x, y + 2 * bs) ]

        if self.tetris_window.all_inside( temp ) and \
           not self.tetris_window.has_collision_with_landed_objects( temp ):
            self.coordinates = temp
            self.state = ( self.state + 1 ) % 2

    # This function is given.
    def get_color( self ):
        return (255,0,0)
