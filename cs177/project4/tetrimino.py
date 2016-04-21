import pygame

# This is the base Tetrimino class. (It may be referred as an abstract 
# class in some programming languages.
# Actual Tetrimino classes (i.e., Tetrimino_I, Tetrimino_J, etc.)
# will take inheritance from this class.
class Tetrimino( object ):
    # This function is given.
    def __init__( self, tetris_window ):
        self.tetris_window = tetris_window 
        self.state = 0
    
    # TASK 10:
    #
    # This function moves a tetrimino down. (It adds self.tetris_window.block_size to the y values)
    #
    # Updates self.coordinates. (if necessary)
    #
    # Move every coordinate in self.coordinates down. (self.tetris_window.block_size)
    # Check if all cordinates of the tetrimino are still,
    # (a) In the window, and,
    # (b) Does not have any collision with any landed object
    # If (a) and (b) is True, then update the self.coordinates, 
    # Otherwise do not update the self.coordinates.
    #
    # You need to use these member variables/functions:
    #
    # self.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    # self.tetris_window.block_size: Size of the blocks, type: Integer
    # self.tetris_window.all_inside()
    # self.tetris_window.has_collision_with_landed_objects()
    #
    # RETURNS: None
    #
    def move_down( self ):
        # Your code starts here.
        bs = self.tetris_window.block_size
        temp = []
        for (x,y) in self.coordinates:
            temp.append(x,y+sb)

        if self.tetris_window.all_inside( temp ) and \
           not self.tetris_window.has_collision_with_landed_objects( temp ):
            self.coordinates = temp
            

        # Your code ends here.

    # TASK 11:
    #
    # This function moves a tetrimino left. (It subtracts self.tetris_window.block_size from the x values)
    #
    # Updates self.coordinates. (if necessary)
    #
    # Move every coordinate in self.coordinates to left. (self.tetris_window.block_size)
    # Check if all cordinates of the tetrimino are still,
    # (a) In the window, and,
    # (b) Does not have any collision with any landed object
    # If (a) and (b) is True, then update the self.coordinates, 
    # Otherwise do not update the self.coordinates.
    #
    # You need to use these member variables/functions:
    #
    # self.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    # self.tetris_window.block_size: Size of the blocks, type: Integer
    # self.tetris_window.all_inside()
    # self.tetris_window.has_collision_with_landed_objects()
    #
    # RETURNS: None
    #
    def move_left( self ):
        # Your code starts here.
        bs = self.tetris_window.block_size
        temp = []
        for (x,y) in self.coordinates:
            temp.append(x-sb,y)

        if self.tetris_window.all_inside( temp ) and \
           not self.tetris_window.has_collision_with_landed_objects( temp ):
            self.coordinates = temp

        # Your code ends here.

    # TASK 12:
    #
    # This function moves a tetrimino right. (It adds self.tetris_window.block_size to the x values)
    #
    # Updates self.coordinates. (if necessary)
    #
    # Move every coordinate in self.coordinates to right. (self.tetris_window.block_size)
    # Check if all cordinates of the tetrimino are still,
    # (a) In the window, and,
    # (b) Does not have any collision with any landed object
    # If (a) and (b) is True, then update the self.coordinates, Otherwise do not update 
    # the self.coordinates.
    #
    # You need to use these member variables/functions:
    #
    # self.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    # self.tetris_window.block_size: Size of the blocks, type: Integer
    # self.tetris_window.all_inside()
    # self.tetris_window.has_collision_with_landed_objects()
    #
    # RETURNS: None
    #
    def move_right( self ):
        # Your code starts here.
        bs = self.tetris_window.block_size
        temp = []
        for (x,y) in self.coordinates:
            temp.append(x+sb,y)

        if self.tetris_window.all_inside( temp ) and \
           not self.tetris_window.has_collision_with_landed_objects( temp ):
            self.coordinates = temp

        # Your code ends here.

    # TASK 13:
    #
    # Checks whether the tetrimino has landed.
    # Returns True if,
    # (a) Any coordinate in self.coordinates is in the last row, or
    # (b) Any coordinate in self.coordinates is one row above any of a 
    # self.tetris_window.landed_objects
    #
    # Otherwise returns False.
    #
    # You need to use these member variables/functions:
    # self.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    # self.tetris_window.block_size: Size of the blocks, type: Integer
    # self.tetris_window.height: Height of the window, type: Integer
    # self.tetris_window.landed_objects: List of landed objects of the form ((x,y),(r,g,b))
    #     where x,y,r,g,b are Integers. (x,y) contains the coordinate of the object
    #     and (r,g,b) has the color information of the object.
    #
    # RETURNS: Whether the tetrimino has landed, type: Boolean
    #
    def has_landed( self ):
        # Your code starts here.
        bs = self.tetris_window.block_size
        for (x,y) in self.coordinates:
            if y+bs == self.tetris_window.height:
                return True
            for ((x_landed,y_landed),(r,g,b)) in self.tetris_window.landed_objects:
                if y+bs == y_landed:
                    return True

        return False
        # Your code ends here.

    # TASK 14:
    #
    # Moves the tetrimino down until it has landed.
    #
    # More specifically, you should call self.move_down() until
    # move.has_landed() becomes True.
    #
    # You need to use these member variables/functions:
    #
    # self.has_landed()
    # self.move_down()
    #
    # RETURNS: None
    #
    def land( self ):
        # Your code starts here.
        while not self.has_landed():
            self.move_down()

        # Your code ends here.

    # TASK 15:
    #
    # Draws the tetrimino on the screen using a set of pygame.draw.rect() function calls.
    # 
    # You need to use these member variables/functions:
    #
    # self.coordinates: List of coordinates of the form (x,y) where x and y is Integer
    # self.tetris_window.block_size: Size of the blocks, type: Integer
    # self.tetris_window.surface: Surface object to the draw the lines, type: pygame.Surface
    # self.get_color(): Returns the color of the tetrimino of the form (r,g,b),
    #                    where r,g,b are Integer
    #
    # RETURNS: None
    #
    # Important: The coordinates in self.coordinates are the center positions of the
    #            items. However, draw.rect() functions expect the top-left corner. 
    #
    # Example: pygame.draw.rect( self.tetris_window.surface, (255,255,255), (100,100,50,50) ) 
    # will draw a rectangle whose upper left corner is (100,100) and
    # whose width = 50 and height = 50.
    #
    # Documentation for draw.rect() function: 
    # http://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
    #
    def draw_tetrimino( self ):
        # Your code starts here.

        # Your code ends here.
