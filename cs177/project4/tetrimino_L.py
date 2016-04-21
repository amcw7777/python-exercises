from tetrimino import *

class Tetrimino_L( Tetrimino ):
    # TASK 1:
    # 
    # Constructor function of Tetrimino_L.
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
    # Please see images/initial_tetrimino_L_01.png,
    #            images/initial_tetrimino_L_02.png,
    #            images/initial_tetrimino_L_03.png,
    #            images/initial_tetrimino_L_04.png
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
        self.coordinates = [ (x-bs,y),(x,y),(x,y+bs),(x,y+2*bs) ]


        # Your code ends here.

    # TASK 6:
    #
    # This function rotates the tetrimino.
    #
    # Tetrimino_L has four states. (0,1,2 and 3)
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
    # Please see  images/tetrimino_L_01_state_00.png
    #             images/tetrimino_L_01_state_01.png
    #             images/tetrimino_L_01_state_02.png
    #             images/tetrimino_L_01_state_03.png
    #             images/tetrimino_L_02_state_00.png
    #             images/tetrimino_L_02_state_01.png
    #             images/tetrimino_L_02_state_02.png
    #             images/tetrimino_L_02_state_03.png
    # 
    # and their corresponding parameters in images/data.txt
    #
    # (Tetrimino_I and Tetrimino_J is given to you. Please look at them before you
    #  start this task.)
    #
    def rotate( self ):
        # Your code starts here.
        bs = self.tetris_window.block_size
        if self.state == 0:
            x,y = self.coordinates[1]
            temp = [ (x,y),(x,y+bs),(x-bs,y+bs),(x-2*bs,y+bs)]
        elif self.state == 1:
            x,y = self.coordinates[1]
            temp = [ (x,y+2*bs),(x-bs,y+2*bs),(x-bs,y+bs),(x-bs,y) ]
        elif self.state == 2:
            x,y = self.coordinates[1]
            temp = [ (x,y-bs),(x,y-2*bs),(x+bs,y-2*bs),(x+2*bs,y-2*bs)]
        elif self.state == 3:
            x,y = self.coordinates[2]
            temp = [ (x-bs,y),(x,y),(x,y+bs),(x,y+2*bs) ]

        if self.tetris_window.all_inside( temp ) and \
           not self.tetris_window.has_collision_with_landed_objects( temp ):
            self.coordinates = temp
            self.state = (self.state + 1) % 4

        # Your code ends here.

    # This function is given.
    def get_color( self ):
        return (255,0,255)
