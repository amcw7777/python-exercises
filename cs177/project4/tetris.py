import sys
import pygame
import time

from tetris_window import *
from tetrimino_factory import *

# TASK 0:
#
# Enter your group information:
#
GROUP_ID = 0
AUTHOR1 = 'Sait Celebi'
AUTHOR1_PURDUE_USERNAME = 'celebis'
AUTHOR2 = 'John Doe'
AUTHOR2_PURDUE_USERNAME = 'john123'
AUTHOR3 = 'Donald Knuth'
AUTHOR3_PURDUE_USERNAME = 'donald90'

########################### Global Constants ##############################

# size of the blocks 
BLOCK_SIZE = 40 # must be even

# number of blocks in x direction 
NUM_BLOCKS_X = 11

# number of blocks in y direction 
NUM_BLOCKS_Y = 20

# frames per second. this is effectively speed of snake in this program.
# read this if you are not familiar:
# https://en.wikipedia.org/wiki/Frame_rate
FPS = 16

###########################################################################

# The main() function is given. Do not change this.
# However, you are encouraged to change the above parameters and
# test your program with different set of parameters.
def main():    
    tetris_window = TetrisWindow( BLOCK_SIZE, NUM_BLOCKS_X, NUM_BLOCKS_Y )
    tetrimino_factory = TetriminoFactory( tetris_window )
    current_tetrimino = tetrimino_factory.get_random_object()
    counter = 0

    while True:
        moved_left, moved_right = False, False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_tetrimino.rotate()
                elif event.key == pygame.K_LEFT:
                    current_tetrimino.move_left()
                    moved_left = True
                    time.sleep(0.15)
                elif event.key == pygame.K_RIGHT:
                    current_tetrimino.move_right()
                    moved_right = True
                    time.sleep(0.15)
                elif event.key == pygame.K_SPACE:
                    current_tetrimino.land()

        keys = pygame.key.get_pressed()
        left, right, down = keys[ pygame.K_LEFT ], keys[ pygame.K_RIGHT ], keys[ pygame.K_DOWN ]

        if left and not moved_left: current_tetrimino.move_left()
        if right and not moved_right: current_tetrimino.move_right()
        if down: current_tetrimino.move_down()
                
        tetris_window.surface.fill( (0,0,0) ) # black background
    
        counter += 1
        if counter == 5:
            current_tetrimino.move_down()
            counter = 0
        
        current_tetrimino.draw_tetrimino()
        if current_tetrimino.has_landed():
            tetris_window.add_tetrimino_to_landed_objects(current_tetrimino) 
            tetris_window.update_landed_objects()
            current_tetrimino = tetrimino_factory.get_random_object()
        
        tetris_window.draw_landed_objects()
        tetris_window.draw_grid()

        if tetris_window.is_game_over(current_tetrimino):
            tetris_window.reset_window()

        # update the window with the last drawings
        pygame.display.update()
        
        # set fps (speed)
        tetris_window.clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
