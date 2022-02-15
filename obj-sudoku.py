#!/usr/bin/env python3

# Sudoku puzzle written in object oriented Python
# Assume 9x9 puzzle 


class UnknownSpot():  # Make this parent = UnknownSpot; child = KnownSpot 
    def __init__(self, num):
        pass
        self.num = num  # Value of 0 through 80
        self.contents = [1,2,3,4,5,6,7,8,9]  # Initialize to all possible values 
        self.known = False  # Toggle to 'True' when contents reaches one value

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


class Puzzle():
    def __init__(self):
        self.num_spots = 81  # For default 9x9 puzzle
        self.full_side = int(self.num_spots ** 0.5)


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


