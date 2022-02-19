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
        if len(self.get_con()) == 1 and isinstance(self.get_con(), list):
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
        self.making_progress = True  # Set initial value
        self.num_possible_values = self.num_spots ** 2  # Initialize to largest possible value

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
                    print("J,K ROWS have assigned values __: {},{}".format(j, k))  #DEBUG
                    print()  #DEBUG space
                    if self.puzz[k].get_row() != row_number:  # Skip since wrong row
                        print("J in row {} but K in row {} so skip".format(row_number, self.puzz[k].get_row()))  #DEBUG
                        continue  
                    else:
                        if self.puzz[k].get_known() == True:  # skip since cannot remove from known spot (includes itself)
                            continue
                        else:
                            print("DEBUG J is: {}".format(self.puzz[j].get_con()))
                            print("DEBUG K is: {}".format(self.puzz[k].get_con()))
 
                            if self.puzz[j].get_con() in self.puzz[k].get_con():  # If duplicated
                                print("DEBUG J in K so remove")
                                self.puzz[k].rem(self.puzz[j].get_con())
                                print("DEBUG K contents now {}".format(self.puzz[k].get_con()))
                                print()  #DEBUG add blank line
                            else:  # skip
                                pass

    def solve_columns(self):
        self.state = "Solving Columns"  # Update state

        # For every spot in every column, if spot is 'known' remove that value from other spots in column
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:  # Value is not known so skip
                continue
            else:  # Value is known so remove from all other spots in same column except itself
                column_number = self.puzz[j].get_column()
                for k in range(self.num_spots):
                    print("J,K COLUMNS have assigned values __: {},{}".format(j, k))  #DEBUG
                    print()  #DEBUG space
                    if self.puzz[k].get_column() != column_number:  # Skip since wrong column
                        print("J in column {} but K in column {} so skip".format(column_number, self.puzz[k].get_column()))  #DEBUG
                        continue  
                    else:
                        if self.puzz[k].get_known() == True:  # skip since cannot remove from known spot (includes itself)
                            continue
                        else:
                            print("DEBUG J is: {}".format(self.puzz[j].get_con()))
                            print("DEBUG K is: {}".format(self.puzz[k].get_con()))
 
                            if self.puzz[j].get_con() in self.puzz[k].get_con():  # If duplicated
                                print("DEBUG J in K so remove")
                                self.puzz[k].rem(self.puzz[j].get_con())
                                print("DEBUG K contents now {}".format(self.puzz[k].get_con()))
                                print()  #DEBUG add blank line
                            else:  # skip
                                pass

    def solve_grids(self):
        self.state = "Solving Grids"  # Update state

        # For every spot in every grids, if spot is 'known' remove that value from other spots in grids
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:  # Value is not known so skip
                continue
            else:  # Value is known so remove from all other spots in same column except itself
                grid_number = self.puzz[j].get_grid()
                for k in range(self.num_spots):
                    print("J,K GRIDS have assigned values __: {},{}".format(j, k))  #DEBUG
                    print()  #DEBUG space
                    if self.puzz[k].get_grid() != grid_number:  # Skip since wrong grid
                        print("J in grid {} but K in grid {} so skip".format(grid_number, self.puzz[k].get_grid()))  #DEBUG
                        continue  
                    else:
                        if self.puzz[k].get_known() == True:  # skip since cannot remove from known spot (includes itself)
                            continue
                        else:
                            print("DEBUG J is: {}".format(self.puzz[j].get_con()))
                            print("DEBUG K is: {}".format(self.puzz[k].get_con()))
 
                            if self.puzz[j].get_con() in self.puzz[k].get_con():  # If duplicated
                                print("DEBUG J in K so remove")
                                self.puzz[k].rem(self.puzz[j].get_con())
                                print("DEBUG K contents now {}".format(self.puzz[k].get_con()))
                                print()  #DEBUG add blank line
                            else:  # skip
                                pass


    def get_num_possible_values(self):
        return self.num_possible_values

    def calc_num_possible_values(self):  # The sum of all possible values in all spots
                                         # Use to determine if puzzle solving is stalled or not
        previous_value = self.get_num_possible_values()
        sum = 0
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == True:
                sum = sum + 1  # Since spot is 'known' its contents are a single integer
                               # Get TypeError if perform 'len' on integer so this is the workaround
            else:
                sum = sum + len(self.puzz[j].get_con())
        self.num_possible_values = sum
       
        print("DEBUG Previous = {}, SUM = {}".format(previous_value, self.num_possible_values))  #DEBUG

        if previous_value > sum:
            self.making_progress = True
        else:
            self.making_progress = False

        return self.num_possible_values 


def main():
    easy_puzzle = [7,4,5,0,9,0,0,0,0,\
                   0,3,2,1,5,0,0,4,6,\
                   0,0,0,2,8,0,5,0,3,\
                   2,0,0,0,0,0,0,6,0,\
                   9,8,0,6,0,0,3,5,1,\
                   0,0,0,5,4,0,2,0,7,\
                   3,0,8,0,0,0,0,0,2,\
                   0,2,0,7,6,0,0,1,0,\
                   0,6,0,9,0,8,0,3,4]

    medium_puzzle = [8,0,0,7,0,6,0,0,0,\
                     0,0,6,0,0,0,0,5,0,\
                     0,9,2,4,0,0,0,7,6,\
                     9,0,7,6,2,1,5,0,3,\
                     0,2,0,0,0,0,0,1,0,\
                     5,0,1,9,4,7,6,0,8,\
                     2,5,0,0,0,4,1,8,0,\
                     0,6,0,0,0,0,2,0,0,\
                     0,0,0,2,0,5,0,0,4]

    hard_puzzle = [0,0,0,0,0,0,0,1,7,\
                   0,0,7,0,6,2,0,0,5,\
                   4,0,0,0,1,0,0,0,0,\
                   0,7,0,0,0,3,0,0,8,\
                   0,0,3,5,0,4,1,0,0,\
                   8,0,0,1,0,0,0,6,0,\
                   0,0,0,0,4,0,0,0,9,\
                   1,0,0,7,9,0,2,0,0,\
                   3,4,0,0,0,0,0,0,0]

    hardest_puzzle = [0,0,0,2,0,1,5,0,3,\
                      2,0,0,0,0,6,0,7,0,\
                      0,0,9,0,0,0,0,0,0,\
                      9,0,0,0,8,0,7,0,2,\
                      0,1,0,0,0,0,0,3,0,\
                      8,0,6,0,1,0,0,0,9,\
                      0,0,0,0,0,0,9,0,0,\
                      0,9,0,8,0,0,0,0,6,\
                      3,0,8,7,0,2,0,0,0]
   
    p = Puzzle(easy_puzzle)
    print("Puzzle solving progress is: {}".format(p.making_progress))  # Debug

    while p.making_progress == True:
        p.solve_rows()
        after_rows_solving_total = p.calc_num_possible_values()
        p.solve_columns()
        after_columns_solving_total = p.calc_num_possible_values()
        p.solve_grids()
        after_grids_solving_total = p.calc_num_possible_values()
        print("After row solving total = {}".format(after_rows_solving_total))
        print("After column solving total = {}".format(after_columns_solving_total))
        print("After grid solving total = {}".format(after_grids_solving_total))
        print("PROGRESS STATE = {}".format(p.making_progress))



if __name__ == "__main__":
    main()


