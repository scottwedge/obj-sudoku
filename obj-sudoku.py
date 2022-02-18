#!/usr/bin/env python3

# Sudoku puzzle written in object oriented Python
# Calculates puzzle size so it can handle either 9x9 or 16x16 puzzle

# Imports
import copy  # Need to perform 'copy.copy' operation to assign unique list to all unknown spots
import time  #DEBUG insert delays to help figure out repeated looping

# Classes
class Spot():  # 
    def __init__(self, num, known, contents, row, column, grid):
        self.num = num  # Value of 0 through 80
        self.known = known  # 'True' if single value contents are known, else False
        self.contents = contents  
        self.row = row
        self.column = column
        self.grid = grid

    def get_con(self):
        return self.contents

    def set_con(self, values):
        self.contents = values

    def rem(self, val):
        self.val = val
        con = self.get_con()
        con.remove(self.val)
        self.set_con(con)
#        print("DEBUG K contents now {}".format(self.puzz[k].get_con()))
        if len(self.get_con()) == 1:
            self.known = True  # If only one value in contents then value is known
            for j in self.get_con():
                self.set_con(j)  # Convert contents from list of one value to that one value 
                                 # so that it matches format of initial known single values


    def get_row(self):  # Row, column and grid coordinate values are set when initialized 
        return self.row  # and never change 

    def get_column(self):
        return self.column

    def get_grid(self):
        return self.grid

    def get_known(self):
        return self.known

    def set_known(self, known):
        self.known = known
        

class Puzzle(Spot):
    def __init__(self, initial_values):
        self.initial_values = initial_values
        self.num_spots = len(self.initial_values)  # Handle both 9x9 or 16x16 puzzle
        self.full_side = int(self.num_spots ** 0.5)  # Handle both 9x9 or 16x16 puzzle
        self.part_side = int(self.num_spots ** 0.25)  # Handle both 9x9 or 16x16 puzzle
        self.state = "Init"

        # Calculate all possible values for undefined spot whether 9x9 or 16x16 puzzle
        all_values_list = []  # Init list
        for j in range(1, self.full_side + 1):
            all_values_list.append(j)

        self.puzz = dict()  # Init dict

        for num in range(self.num_spots):  # For every value in initial puzzle
            # Calculate row coordinate value for spot
            row = num // self.full_side  # Calculate value using floor division '//' operation
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

            # Calculate column coordinate value for spot
            column = num % self.full_side  # Calculate value using modulo '%' operation
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
                                                
            # Calculate grid coordinat value for spot (in two lines for readability)
            grid = num // self.part_side**self.part_side * self.part_side 
            grid = grid + num // self.part_side % self.part_side  
                                    # This results in the following grid numbering: 
                                    #                                000111222
                                    #                                000111222
                                    #                                000111222
                                    #                                333444555
                                    #                                333444555
                                    #                                333444555
                                    #                                666777888
                                    #                                666777888
                                    #                                666777888
                                                                     
            if self.initial_values[num] == 0:
                self.puzz[num] = Spot(num, False, copy.copy(all_values_list), row, column, grid)
            else:
                self.puzz[num] = Spot(num, True, self.initial_values[num], row, column, grid)

            print("Spot {} ".format(num), end = "")  #DEBUG
            print("contains {:^{}}".format(str(self.puzz[num].get_con()), 30), end = "")  #DEBUG 
            # Must use column width to align columns
            # Must use 'str' on list else get error 
            print("Row= {}, ".format(self.puzz[num].get_row()), end = "")  #DEBUG
            print("Column= {}, ".format(self.puzz[num].get_column()), end = "")  #DEBUG
            print("Grid= {}.".format(self.puzz[num].get_grid()))  #DEBUG
      
    def get_val(self, spot):
        self.spot = spot
        return self.puzz[self.spot].get_con() 
        
    def solve_rows(self):
        self.state = "Solving Rows"  # Update state

        # For every spot in every row, if spot is 'known' remove that value from other spots in row
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:  # Value is not known so skip
                continue
            else:  # Value is known so remove from all other spots in same row except itself
                row_number = self.puzz[j].get_row()
                for k in range(self.num_spots):
                    print("J,K has assigned values __: {},{}".format(j, k))  #DEBUG
                    print()  #DEBUG space
                    if self.puzz[k].get_row() != row_number:  # Skip since wrong row
                        print("J in row {} but K in row {} so skip".format(row_number, self.puzz[k].get_row()))  #DEBUG
                        continue  
                    else:
                        if self.puzz[k].get_known() == True:  # skip since cannot remove from known spot (includes itself)
                            continue
                        else:
                            j_con = self.puzz[j].get_con()
                            k_con = self.puzz[k].get_con()
                            print("DEBUG J at {} is: {}".format(time.ctime(), self.puzz[j].get_con()))
                            print("DEBUG K at {} is: {}".format(time.ctime(), self.puzz[k].get_con()))
                            time.sleep(1)  #DEBUG
 
                            if self.puzz[j].get_con() in self.puzz[k].get_con():  # If duplicated
                                print("DEBUG J in K so remove")
                                self.puzz[k].rem(self.puzz[j].get_con())
                                print("DEBUG K contents now {} at {}".format(self.puzz[k].get_con(), time.ctime()))
                                print()  #DEBUG add blank line
                            else:  # skip
                                pass



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
    p.solve_rows()



if __name__ == "__main__":
    main()


