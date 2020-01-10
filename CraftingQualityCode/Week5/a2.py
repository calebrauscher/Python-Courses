# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        A Rat with a 1 character symbol, row the rat is located, col the rat
        is located, and number of sprouts eaten.
        
        >>> mickey = Rat('P', 1, 4)
        >>> mickey.symbol
        'P'
        >>> mickey.row
        1
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Sets the row and column parameter of the instance of Rat.
        
        >>> mickey = Rat('P', 1, 4)
        >>> mickey.set_location(5, 5)
        >>> mickey.row
        5
        >>> mickey.col
        5
        """
        self.row = row
        self.col = col

    def eat_sprouts(self):
        """ (Rat) -> NoneType

        Adds 1 to the instance variable, num_sprouts_eaten.
        
        >>> mickey = Rat('P', 1, 4)
        >>> mickey.eat_sprouts()
        >>> mickey.num_sprouts_eaten
        1
        >>> mickey.eat_sprouts()
        >>> mickey.num_sprouts_eaten
        2
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of this Rat
        
        >>> mickey = Rat('P', 1, 4)
        >>> mickey.__str__()
        'P at (1, 4) ate 0 sprouts.'
        >>> mickey.eat_sprouts()
        >>> mickey.set_location(5,5)
        >>> mickey.__str__()
        'P at (5, 5) ate 1 sprouts.'
        """
        return ('{0} at ({1}, {2}) ate {3} sprouts.'
                .format(self.symbol,
                        self.row,
                        self.col,
                        self.num_sprouts_eaten))

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, kist of list of str, Rat, Rat) -> NoneType

        Initializes maze with a maze, 2 rats.

        >>> rat1 = Rat('J', 1, 1)
        >>> rat2 = Rat('P', 1, 4)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> arena = Maze(maze,rat1,rat2)
        >>> arena.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', 'J', '.', '.', 'P', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> arena.rat_1.symbol
        'J'
        >>> arena.rat_2.row
        1
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol
        self.num_sprouts_left = sum(x.count(1) for x in self.maze)

    def is_wall(self, row, col):
        """ (Maze, int, int) -> Bool

        Returns True if and only if there is a wall at the given row and column
        of the maze.
        
        >>> rat1 = Rat('J', 1, 1)
        >>> rat2 = Rat('P', 1, 4)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> arena = Maze(maze,rat1,rat2)
        >>> arena.is_wall(0, 0)
        True
        >>> arena.is_wall(1, 1)
        False
        """
        return self.maze[row][col] == '#'

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

            Returns the character in the maze at the given row and column.
            If there is a rat at that location, then its character should be
            returned not the WALL.
            
        >>> rat1 = Rat('J', 1, 1)
        >>> rat2 = Rat('P', 1, 4)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> arena = Maze(maze,rat1,rat2)
        >>> arena.get_character(0,0)
        '#'
        >>> arena.get_character(2,1)
        '.'
        >>> arena.get_character(1,1)
        'J'
        >>> arena.get_character(1,4)
        'P'
        """
        if row == self.rat_1.row and col == self.rat_1.col:
            return self.rat_1.symbol
        if row == self.rat_2.row and col == self.rat_2.col:
            return self.rat_2.symbol
        return self.maze[row][col]

    def move(self, rat, vertical, horizontal):
        """ (Maze, Rat, int, int) -> bool

        Move the rat in the given direction, unless there is a wall in the way.

        Also, check for a Brussels sprout at that location and, if present:

            - have the rat eat the Brussels sprout,
            - make that location a \verb|HALL|HALL, and
            - decrease the value that num_sprouts_left refers to by one
            - Return True if and only if there wasn't a wall in the way
        
        >>> rat1 = Rat('J', 1, 1)
        >>> rat2 = Rat('P', 1, 4)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> arena = Maze(maze,rat1,rat2)
        >>> arena.move(rat1, DOWN, NO_CHANGE)
        True
        >>> rat1.row
        2
        """
        if not self.is_wall(rat.row + vertical, rat.col + horizontal):
            if self.get_character(rat.row + vertical,
                                  rat.col + horizontal) == SPROUT:
                rat.eat_sprouts()
                self.num_sprouts_left -= 1
            self.maze[rat.row][rat.col] = HALL
            rat.row += vertical
            rat.col += horizontal
            self.maze[rat.row][rat.col] = rat.symbol
            return True
        return False

    def __str__(self):
        ''' (Maze) -> str
            Return a string representation of this Maze.
            
        >>> rat1 = Rat('J', 1, 1)
        >>> rat2 = Rat('P', 1, 4)
        >>> maze = [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> arena = Maze(maze,rat1,rat2)
        >>> arena.__str__()
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        '''
        result = '\n'.join([''.join(x) for x in self.maze])
        result += ('\n{0} at ({1}, {2}) ate {3} sprouts.'
                   .format(self.rat_1.symbol,
                           self.rat_1.row,
                           self.rat_1.col,
                           self.rat_1.num_sprouts_eaten))
        result += ('\n{0} at ({1}, {2}) ate {3} sprouts.'
                   .format(self.rat_2.symbol,
                           self.rat_2.row,
                           self.rat_2.col,
                           self.rat_2.num_sprouts_eaten))

        return result
        
                
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
