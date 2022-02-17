#!/usr/bin/env python3

# Sudoku puzzle written in object oriented Python
# Assume 9x9 puzzle 

# Global constants

# Classes
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
    def __init__(self, initial_values):
        self.initial_values = initial_values
        self.num_spots = len(self.initial_values)  # Handle both 9x9 or 16x16 puzzle
        self.full_side = int(self.initial_values ** 0.5)  # Handle both 9x9 or 16x16 puzzle
        self.part_side = int(self.initial_values ** 0.25)  # Handle both 9x9 or 16x16 puzzle
        self.state = "Init"
#        print("Initial values are {}".format(self.initial_values))  #DEBUG
        self.puzz = dict()
        for j in range(len(self.initial_values)):
            if self.initial_values[j] == 0:
                self.puzz[j] = UnknownSpot(j)
            else:
                self.puzz[j] = KnownSpot(j, self.initial_values[j])
            print("Contents of spot {} are {}.".format(j, self.puzz[j].get_con())) 
            print(j, self.puzz[j].get_con())
      
    def get_val(self, spot):
        self.spot = spot
        return self.puzz[self.spot].get_con() 
        

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


    p = Puzzle(initial_puzzle)

    print()
    print("First grid contains: {}".format(p.get_val(0)))



if __name__ == "__main__":
    main()


