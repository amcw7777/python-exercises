import pygame

from tetrimino import *

class TetrisWindow( object ):
    # Constructor of TetrisWindow class.
    # This functions is given.
    def __init__( self, block_size, num_blocks_x, num_blocks_y ):
        #initializations
        pygame.init()
        self.block_size = block_size
        self.num_blocks_x = num_blocks_x
        self.num_blocks_y = num_blocks_y
        self.width = block_size * num_blocks_x
        self.height = block_size * num_blocks_y
        self.surface = pygame.display.set_mode( (self.width+1, self.height+1) )
        pygame.display.set_caption( 'Purdue University - CS 177 - Tetris game' )
        # clock is helping us to set FPS
        self.clock = pygame.time.Clock()
        self.landed_objects = []

    # TASK 16:
    #
    # Checks if all coordinates are in the window or not.
    # Returns True if all coordinates are in the window.
    # Returns False if at least one coordinate is outside of the window.
    #
    # INPUT:
    # coordinates: List of coordinates of the form (x,y) where x and y is Integer
    #
    # You need to use these member variables/functions:
    # self.width: Width of the window, type: Integer
    # self.height: Height of the window, type: Integer
    #
    # RETURNS: Whether all cordinates are in the window or not, type: Boolean
    #
    def all_inside( self, coordinates ):
        # Your code starts here.

        print('remove this line.')

        # Your code ends here.

    # TASK 17:
    #
    # Checks if there is any collision between self.landed_objects and coordinates.
    #
    # Returns True if there is a collision
    # Returns False if there is no collision
    #
    # INPUT:
    # coordinates: List of coordinates of the form (x,y) where x and y is Integer
    #
    # You need to use these member variables/functions:
    # self.landed_objects: List of landed objects of the form ((x,y),(r,g,b))
    #     where x,y,r,g,b are Integers. (x,y) contains the coordinate of the object
    #     and (r,g,b) has the color information of the object.
    #
    # RETURNS: Whether there is a collision or not, type: Boolean
    #
    def has_collision_with_landed_objects( self, coordinates ):
        # Your code starts here.

        print('remove this line.')

        # Your code ends here.

    # TASK 18:
    #
    # Adds a tetrimino to the self.landed_objects.
    # We need to break the tetrimino into pieces before we add it to self.landed_objects.
    #
    # tetrimino.coordinates has list of (x,y) values which are the center 
    # coordinates of the squares of the tetrimino. self.landed_objects has list 
    # of ((x,y),(r,g,b)) values for each square that has landed. Note that there 
    # are multiple squares in each tetrimino. (There are 4 squares in all 7 
    # different Tetriminos)
    #
    # More specifically, in this function we add each square's center position and
    # its color to the self.landed_objects.
    #
    # INPUT:
    # tetrimino: The tetrimino which needs to be broken into pieces and 
    # added to self.landed_objects, type: Tetrimino
    #
    # You need to use these member variables/functions:
    #
    # self.landed_objects: List of landed objects of the form ((x,y),(r,g,b))
    #     where x,y,r,g,b are Integers. (x,y) contains the coordinate of the object
    #     and (r,g,b) has the color information of the object.
    # tetrimino.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    # tetrimino.get_color(): Returns the color of the tetrimino of the form (r,g,b) where
    #                             r,g,b are Integers, type: Tuple
    #
    # RETURNS: None
    #
    def add_tetrimino_to_landed_objects( self, tetrimino ):
        # Your code starts here.

        print('remove this line.')

        # Your code ends here.

    # TASK 19:
    #
    # Updates the self.landed_objects after a new tetrimino is added.
    # In the update phase, if a row is full, the row should be deleted and the rows
    # on top the deleted row should be moved one row below.
    # If there are more than one row is full, then all full rows should be
    # deleted.
    #
    # You need to use these member variables/functions:
    # 
    # self.num_blocks_x: Number of blocks in x direction
    # self.num_blocks_y: Number of blocks in y direction
    # self.width: Width of the window, type: Integer
    # self.height: Height of the window, type: Integer
    # self.block_size: Size of the blocks, type: Integer
    # self.landed_objects: List of landed objects of the form ((x,y),(r,g,b))
    #     where x,y,r,g,b are Integers. (x,y) contains the coordinate of the object
    #     and (r,g,b) has the color information of the object.
    # 
    # Please see images/update_01_01.png
    #            images/update_01_02.png
    #            images/update_02_01.png
    #            images/update_02_02.png
    #            images/update_03_01.png
    #            images/update_03_02.png
    #            images/update_04_01.png
    #            images/update_04_02.png
    #            images/update_05_01.png
    #            images/update_05_02.png
    #
    # and their corresponding parameters in images/data.txt
    #
    # RETURNS: None
    #
    def update_landed_objects( self ):
        # Your code starts here.

        print('remove this line.')

        # Your code ends here.

    # TASK 20:
    #
    # Checks the new tetrimino object has any collision with self.landed_objects,
    # hence the game is over.
    # Returns True if there is at least one collision.
    # Returns False if there is no collision.
    #
    # INPUT:
    # tetrimino: The tetrimino to check if there is any collision with 
    # self.landed_objects, type: Tetrimino
    #
    # You need to use these member variables/functions:
    #
    # self.landed_objects: List of landed objects of the form ((x,y),(r,g,b))
    #     where x,y,r,g,b are Integers. (x,y) contains the coordinate of the object
    #     and (r,g,b) has the color information of the object.
    # tetrimino.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    #
    # RETURNS: Whether there is a collision, type: Boolean
    #
    def is_game_over( self, tetrimino ):
        # Your code starts here.

        print('remove this line.')

        # Your code ends here.

    # TASK 21:
    #
    # Draws the grid on the window. (Using white lines)
    # It is similar to the Task 3 in Lab 13.
    # You need to use these member variables/functions:
    #
    # self.width: Width of the window, type: Integer
    # self.height: Height of the window, type: Integer
    # self.block_size: Size of the blocks, type: Integer
    # self.surface: Surface object to the draw the lines, type: pygame.Surface
    # 
    # Returns: None
    #
    # Documentation for draw.line() function: 
    # http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
    #
    # Example: pygame.draw.line( self.surface, (255, 255, 255), (0, 0), (100, 100) )
    # will draw a line to the window from (0,0) to (100,100) with white color.
    #
    def draw_grid( self ):
        # Your code starts here.

        print('remove this line.')

        # Your code ends here.

    # TASK 22:
    #
    # Draws the landed objecs on the screen using a set of pygame.draw.rect()
    # function calls.
    # 
    # You need to use these member variables/functions:
    #
    # self.landed_objects: List of landed objects of the form ((x,y),(r,g,b))
    #     where x,y,r,g,b are Integers. (x,y) contains the coordinate of the object
    #     and (r,g,b) has the color information of the object.
    # self.surface: Surface object to the draw the lines, type: pygame.Surface
    # self.block_size: Size of the blocks, type: Integer
    #
    # RETURNS: None
    #
    # Important: The coordinates in self.landed_objects are the center positions of the
    #            items. However, draw.rect() functions expects the top-left corner. 
    #
    # Example: pygame.draw.rect( self.surface, (255,255,255), (100,100,50,50) ) 
    # will draw a rectangle whose upper left corner is (100,100) and
    # whose width = 50 and height = 50.
    #
    # Documentation for draw.rect() function: 
    # http://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    #
    def draw_landed_objects( self ):
        # Your code starts here.

        print('remove this line.')

        # Your code ends here.

    # This function is given.
    def reset_window( self ):
        self.landed_objects = []
