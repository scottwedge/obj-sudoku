#!/usr/bin/env python3

# Sudoku puzzle written in object oriented Python
# Assume 9x9 puzzle 


class Spot():
    def __init__(self, num):
        self.num = num
        self.contents = [1,2,3,4,5,6,7,8,9]
        self.known = False

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
        


    initial_puzzle = [7,4,5,0,9,0,0,0,0,\
                      0,3,2,1,5,0,0,4,6,\
                      0,0,0,2,8,0,5,0,3,\
                      2,0,0,0,0,0,0,6,0,\
                      9,8,0,6,0,0,3,5,1,\
                      0,0,0,5,4,0,2,0,7,\
                      3,0,8,0,0,0,0,0,2,\
                      0,2,0,7,6,0,0,1,0,\
                      0,6,0,9,0,8,0,3,4]


def main():
    first = Spot(1)
    
    val = first.get_con()
    print(val) 

    for j in first.get_con():
        print(j)


if __name__ == "__main__":
    main()


