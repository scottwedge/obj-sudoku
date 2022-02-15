#!/usr/bin/env python3

# Sudoku puzzle written in object oriented Python
# Assume 9x9 puzzle 

# Global constants
NUM_SPOTS = 81  # Number of spots in a 9x9 grid
FULL_SIDE = int(NUM_SPOTS ** 0.5)  # Length and number of row(s), column(s) and internal grids

class UnknownSpot():  # Make this parent = UnknownSpot; child = KnownSpot 
    def __init__(self, num):
        self.num = num  # Value of 0 through 80
        self.contents = [1,2,3,4,5,6,7,8,9]  # Initialize to all possible values 
        self.known = False  # Toggle to 'True' when contents reaches one value

        self.row = num // FULL_SIDE  # Calculate value using floor division '//' operation
                                     # so spots 0-8 in row 0 ... spots 72-80 in row 8
                                     # This results in the following row numbering:  000000000
                                     #                                               111111111
                                     #                                               222222222 
                                     #                                               333333333 
                                     #                                               444444444 
                                     #                                               555555555 
                                     #                                               666666666 
                                     #                                               777777777 
                                     #                                               888888888 

        self.column = num % FULL_SIDE  # Calculate value using modulo '%' operation
                                       # so spots 0,9..72 in column 0 ... spots 8,17..80 in column 8
                                       # This has the following column numbering: 012345678
                                       #                                          012345678
                                       #                                          012345678
                                       #                                          012345678
                                       #                                          012345678
                                       #                                          012345678
                                       #                                          012345678
                                       #                                          012345678
                                       #                                          012345678
            
        self.grid = num // 27 * 3 + num // 3 % 3  # This results in the following grid numbering: 
                                                  #                                000111222
                                                  #                                000111222
                                                  #                                000111222
                                                  #                                333444555
                                                  #                                333444555
                                                  #                                333444555
                                                  #                                666777888
                                                  #                                666777888
                                                  #                                666777888
                                                                     
            
    def get_con(self):
        return self.contents

    def set_con(self, values):
        self.contents = values

    def remove(self, val):
        self.remove(val)

    def get_known(self):
        return self.known

    def set_known(self, known):
        self.known = known
        

class KnownSpot(UnknownSpot):  # Spot whose single value is known
    def __init__(self, num, contents):
        self.num = num  
        self.contents = contents
        self.known = True


class Puzzle(KnownSpot, UnknownSpot):
    def __init__(self):
        self.num_spots = NUM_SPOTS  # For default 9x9 puzzle
        self.full_side = FULL_SIDE  # For default 9x9 puzzle
        self.state = "Init"


def main():
    initial_puzzle = [7,4,5,0,9,0,0,0,0,\
                      0,3,2,1,5,0,0,4,6,\
                      0,0,0,2,8,0,5,0,3,\
                      2,0,0,0,0,0,0,6,0,\
                      9,8,0,6,0,0,3,5,1,\
                      0,0,0,5,4,0,2,0,7,\
                      3,0,8,0,0,0,0,0,2,\
                      0,2,0,7,6,0,0,1,0,\
                      0,6,0,9,0,8,0,3,4]


    first = UnknownSpot(0)
    second = KnownSpot(1, 7)
    
    val = first.get_con()
    print("Contents of spot {} are {}.".format(first.num, val)) 
    print("Contents of spot {} are {}.".format(second.num, second.contents)) 
   

    for j in first.get_con():
        print(j)

    p = Puzzle()
    print("Number of spots in puzzle is {}".format(p.num_spots))
    print("Length of puzzle side is {}.".format(p.full_side))


if __name__ == "__main__":
    main()


