#!/usr/bin/env python3

# Sudoku puzzle written in object oriented Python
# Calculates puzzle size so it can handle either 9x9 or 16x16 puzzle

# Imports
import copy  # Need to perform 'copy.copy' operation to assign unique list to all unknown spots
import time  #DEBUG insert delays to help figure out repeated looping

# Classes
class UserInput():
    def __init__(self):
        self.play_game = True
        self.column_width = "normal"  # Either "normal" or "narrow"; default to "normal"
        self.puzzle_selected = False

    def start_menu(self):
        print()  # Spacing blank line
        print("Please choose one of the following options:")
        entry = input("1. Select puzzle to solve\n2. Display puzzle with normal column width (default)\n3. Display puzzle with narrow column width\n4. Guess a value in stalled puzzle\n5. List unresolved spots and their possible values\n6. Quit game\nEnter selection: ")
        if entry == "1":
            return entry
        elif entry == "2":
            self.column_width = "normal"
        elif entry == "3":
            self.column_width = "narrow"
        elif entry == "4":
            return entry
        elif entry == "5":
            return entry
        elif entry == "6":
            self.play_game = False
        else:
            pass


    def puzzle_menu(self):
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

        while True:
            print()  # Blank spacing line
            print("Select one of the following four puzzles:")
            print("1. easy\n2. medium\n3. hard\n4. very hard")
            entry = input("Enter 1 or 2 or 3 or 4: ")
            if entry == "1":
                return easy_puzzle
            elif entry == "2":
                return medium_puzzle
            elif entry == "3":
                return hard_puzzle
            elif entry == "4":
                return hardest_puzzle
            else:
                print("Please enter '1' or '2' or '3' or '4'")


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
        
    def get_coords(self):
        return (self.contents, self.row, self.column, self.grid) 

    def short_list_string(self):  # Display list without spaces to safe space
        con = self.get_con()
        if self.known == True:  # Single value
            short_list = str(con)  # Single value is not displayed as a list of one
        else:  # Handle two cases where number of values = 2 or number of values > 2
            if len(con) == 2:
                for j in range(len(con) - 1):
                    short_list = "[" + str(con[0]) + "," + str(con[1]) + "]"
            elif len(con) > 2:
                short_list = '[' + str(con[0])
                for j in range(1, len(con)):
                    short_list += "," + str(con[j])  # Complete string with last value then ']'
                short_list += "]"
        return short_list
            

class Puzzle():
    def __init__(self, initial_values, width):
        self.initial_values = initial_values
        self.column_width_type = width  # set in UserInput.start_menu
        self.num_spots = len(self.initial_values)  # Handle both 9x9 or 16x16 puzzle
        self.full_side = int(self.num_spots ** 0.5)  # Handle both 9x9 or 16x16 puzzle
        self.part_side = int(self.num_spots ** 0.25)  # Handle both 9x9 or 16x16 puzzle
        self.state = "Initiated"
        self.action = "Initiating"
        self.making_progress = True  # Set initial value
        self.num_possible_values = self.num_spots ** 2  # Initialize to largest possible value
        self.narrow_divider_line = "+-+-+-+-+-+-+-+-+-+"  # Initialize value
        self.long_divider_line = "+--+--+--+--+--+--+--+--+--+"  # Initialize value
        self.solved_spots = -1  # Initialize to invalid value
        self.unsolved_spots = -1  # Initialize to invalid value
        self.unsolved_combinations_count = -1  # Initialize to invalid value

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

#            print("Spot {} ".format(num), end = "")  #DEBUG
#            print("contains {:^{}}".format(str(self.puzz[num].get_con()), 30), end = "")  #DEBUG 
            # Must use column width to align columns
            # Must use 'str' on list else get error 
#            print("Row= {}, ".format(self.puzz[num].get_row()), end = "")  #DEBUG
#            print("Column= {}, ".format(self.puzz[num].get_column()), end = "")  #DEBUG
#            print("Grid= {}.".format(self.puzz[num].get_grid()))  #DEBUG
      
    def get_val(self, spot):
        self.spot = spot
        return self.puzz[self.spot].get_con() 
        
    def solve_row_singles(self):
        self.action = "Solving Row Singles"  # Update action

        # For every spot in every row, if spot is 'known' remove that value from other spots in row
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:  # Value is not known so skip
                continue
            else:  # Value is known so remove from all other spots in same row except itself
                row_number = self.puzz[j].get_row()
                for k in range(self.num_spots):
#                    print("J,K ROWS have assigned values __: {},{}".format(j, k))  #DEBUG
#                    print()  #DEBUG space
                    if self.puzz[k].get_row() != row_number:  # Skip since wrong row
#                        print("J in row {} but K in row {} so skip".format(row_number, self.puzz[k].get_row()))  #DEBUG
                        continue  
                    else:
                        if self.puzz[k].get_known() == True:  # skip since cannot remove from known spot (includes itself)
                            continue
                        else:
#                            print("DEBUG J is: {}".format(self.puzz[j].get_con()))
#                            print("DEBUG K is: {}".format(self.puzz[k].get_con()))
 
                            if self.puzz[j].get_con() in self.puzz[k].get_con():  # If duplicated
#                                print("DEBUG J in K so remove")
                                self.puzz[k].rem(self.puzz[j].get_con())
#                                print("DEBUG K contents now {}".format(self.puzz[k].get_con()))
#                                print()  #DEBUG add blank line
                            else:  # skip
                                pass

    def solve_column_singles(self):
        self.action = "Solving Column Singles"  # Update action

        # For every spot in every column, if spot is 'known' remove that value from other spots in column
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:  # Value is not known so skip
                continue
            else:  # Value is known so remove from all other spots in same column except itself
                column_number = self.puzz[j].get_column()
                for k in range(self.num_spots):
#                    print("J,K COLUMNS have assigned values __: {},{}".format(j, k))  #DEBUG
#                    print()  #DEBUG space
                    if self.puzz[k].get_column() != column_number:  # Skip since wrong column
#                        print("J in column {} but K in column {} so skip".format(column_number, self.puzz[k].get_column()))  #DEBUG
                        continue  
                    else:
                        if self.puzz[k].get_known() == True:  # skip since cannot remove from known spot (includes itself)
                            continue
                        else:
#                            print("DEBUG J is: {}".format(self.puzz[j].get_con()))
#                            print("DEBUG K is: {}".format(self.puzz[k].get_con()))
 
                            if self.puzz[j].get_con() in self.puzz[k].get_con():  # If duplicated
#                                print("DEBUG J in K so remove")
                                self.puzz[k].rem(self.puzz[j].get_con())
#                                print("DEBUG K contents now {}".format(self.puzz[k].get_con()))
#                                print()  #DEBUG add blank line
                            else:  # skip
                                pass

    def solve_grid_singles(self):
        self.action = "Solving Grid Singles"  # Update action

        # For every spot in every grids, if spot is 'known' remove that value from other spots in grids
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:  # Value is not known so skip
                continue
            else:  # Value is known so remove from all other spots in same column except itself
                grid_number = self.puzz[j].get_grid()
                for k in range(self.num_spots):
#                    print("J,K GRIDS have assigned values __: {},{}".format(j, k))  #DEBUG
#                    print()  #DEBUG space
                    if self.puzz[k].get_grid() != grid_number:  # Skip since wrong grid
#                        print("J in grid {} but K in grid {} so skip".format(grid_number, self.puzz[k].get_grid()))  #DEBUG
                        continue  
                    else:
                        if self.puzz[k].get_known() == True:  # skip since cannot remove from known spot (includes itself)
                            continue
                        else:
#                            print("DEBUG J is: {}".format(self.puzz[j].get_con()))
#                            print("DEBUG K is: {}".format(self.puzz[k].get_con()))
 
                            if self.puzz[j].get_con() in self.puzz[k].get_con():  # If duplicated
#                                print("DEBUG J in K so remove")
                                self.puzz[k].rem(self.puzz[j].get_con())
#                                print("DEBUG K contents now {}".format(self.puzz[k].get_con()))
#                                print()  #DEBUG add blank line
                            else:  # skip
                                pass

    def solve_pairs(self):  # If identical pair in group, remove two values from all other spots
        self.action = "Solving Pairs"  # Update action
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == True:  # If 'known' then only has a single value, so skip
                continue
            elif len(self.puzz[j].get_con()) != 2:  # Skip if not contain only two possible values
                continue
            else:
                (j_con, j_row, j_col, j_grid) = self.puzz[j].get_coords()  # Get contents, row, column and grid values
                for k in range(self.num_spots):  # Check every other spot for a matching pair of values
                    (k_con, k_row, k_col, k_grid) = self.puzz[k].get_coords()  # Get contents, row, column and grid values
                    if j_con == k_con and j != k:  # Pairs must match but cannot compare to itself
                        if j_row == k_row:  # ROW: Remove both values from all other spots in that row
                            for m in range(self.num_spots):  
                                if self.puzz[m].get_known() == True:  # Skip if known single value
                                    continue
                                (m_con, m_row, m_col, m_grid) = self.puzz[m].get_coords()  # Get contents, row, column and grid values
                                if m_row != j_row or m == j or m == k:  # Skip if wrong row or comparing to both selfs
                                    continue 
                                else:
                                    for val in j_con:  # For both values, remove from spot
                                        if val in m_con:
                                            self.puzz[m].rem(val)
                                
                        if j_col == k_col:  # COLUMN: Remove both values from all other spots in that column
                            for m in range(self.num_spots):  
                                if self.puzz[m].get_known() == True:  # Skip if known single value
                                    continue
                                (m_con, m_row, m_col, m_grid) = self.puzz[m].get_coords()  # Get contents, row, column and grid values
                                if m_col != j_col or m == j or m == k:  # Skip if wrong column or comparing to both selfs
                                    continue 
                                else:
                                    for val in j_con:  # For both values, remove from spot
                                        if val in m_con:
                                            self.puzz[m].rem(val)
                                
                        if j_grid == k_grid:  # GRID: Remove both values from all other spots in that grid
                            for m in range(self.num_spots):  
                                if self.puzz[m].get_known() == True:  # Skip if known single value
                                    continue
                                (m_con, m_row, m_col, m_grid) = self.puzz[m].get_coords()  # Get contents, row, column and grid values
                                if m_grid != j_grid or m == j or m == k:  # Skip if wrong grid or comparing to both selfs
                                    continue 
                                else:
                                    for val in j_con:  # For both values, remove from spot
                                        if val in m_con:
                                            self.puzz[m].rem(val)


    def get_num_possible_values(self):
        return self.num_possible_values

    def calc_solved_counts(self):
        solved_spots = 0
        unsolved_spots = 0
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == True:
                solved_spots += 1  # Increment solved count
            else:
                unsolved_spots += 1  # Increment unsolved count
        self.solved_spots = solved_spots
        self.unsolved_spots = unsolved_spots
#        return (solved_spots, unsolved_spots) 

    def calc_unsolved_combinations(self):
        unsolved_combinations_count = 1
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:
                unsolved_combinations_count *= len(self.puzz[j].get_con())  
        self.unsolved_combinations_count = unsolved_combinations_count  # Update value

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
       
#        print("DEBUG Previous = {}, SUM = {}".format(previous_value, self.num_possible_values))  #DEBUG

        if previous_value > sum:
            self.making_progress = True
            self.state = "Solving"
        else:
            self.making_progress = False
            if sum == self.num_spots:
                self.state = "Puzzle solved"  # Puzzle is solved
            else:
                self.state = "Solving Stalled"  # Puzzle is stalled

        return self.num_possible_values 

    def calc_column_widths(self):  # Calculate maximum width of every column
        cw = dict()  # Init dict
        for j in range(self.full_side):
            cw[j] = 1  # Initialize all column widths to 1
        
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == True:
                l = 1  # Length = 1 since value already known
            else:
                col = j % self.full_side  # Determine column
                l = len(self.puzz[j].get_con())
                if l > cw[col]:  # Calculate maximum width of every column
                    cw[col] = l
        self.create_long_divider_line(cw)  # Create divider line for normal column width
        self.create_narrow_divider_line(cw)  # Create divider line for narrow column width
        return cw

    def create_long_divider_line(self, cw):  
        # Line has '+' at every intersection and '-' in between - for normal width columns puzzle
        self.cw = cw
        long_line = "+"  # First character
        for j in self.cw:
             long_line += + 3 * self.cw[j] * '-' + "+"  # Want three '-' for every number in grid
        self.long_divider_line = long_line

    def create_narrow_divider_line(self, cw):  
        # Line has '+' at every intersection and '-' in between - for narrow width columns puzzle
        self.cw = cw
        narrow_line = "+"  # First character
        for j in self.cw:
             narrow_line += + (2 * self.cw[j] + 1) * '-' + "+"  #Dh  Want two '-' plus one for every number in grid
        self.narrow_divider_line = narrow_line


    def display_puzzle_normal_column(self):
        cw = self.calc_column_widths()  # Get max column widths and create divider lines

        print(self.long_divider_line)  # Print top most line
        for j in range(self.num_spots):
            print("|{:^{}}".format(str(self.puzz[j].get_con()), 3*cw[j%self.full_side]), end = "")  # Must convert to string to print list
            if j % self.full_side == self.full_side - 1:
                print("|")  # Print end of line at end of each line
                print(self.long_divider_line)  # Print long horizontal line between rows
                

    def display_puzzle_narrow_column(self):
        cw = self.calc_column_widths()  # Get max column widths

        print(self.narrow_divider_line)  # Print top most line
        for j in range(self.num_spots):
            print("|{:^{}}".format(str(self.puzz[j].short_list_string()), 2*cw[j%self.full_side] + 1), end = "")  # Must convert to string to print list
            if j % self.full_side == self.full_side - 1:
                print("|")  # Print end of line at end of each line
                print(self.narrow_divider_line)  # Print narrow horizontal line between rows

    def display_puzzle(self):
        if self.column_width_type == "normal":  # Determine if narrow or normal columns 
            self.display_puzzle_normal_column()
        elif self.column_width_type == "narrow":  # Determine if narrow or normal columns 
            self.display_puzzle_narrow_column()
        else:
            pass  # Invalid condition


    def show_state(self):
        print(self.state)

    def show_solved_unsolved_counts(self):
        print("Solved spot count = {}. Unsolved spot count = {}.".format(self.solved_spots, self.unsolved_spots))
        if self.unsolved_spots > 0:
           self.calc_unsolved_combinations()
           self.show_unsolved_combinations()

    def show_unsolved_combinations(self):
        print("There are {:,} possible combinations.".format(self.unsolved_combinations_count))  # Format with ',' as thousands separator

    def unsolved_spot_guesses(self):
        possible_guess = dict()
        for j in range(self.num_spots):
            if self.puzz[j].get_known() == False:
                possible_guess[j]= self.puzz[j].get_con()
        return possible_guess

def main():
   
    ui = UserInput()
    while ui.play_game == True:  # Play game until quit
        entry = ui.start_menu()  # Choose option in Starting menu
    
        if entry == "1":
            ui.puzzle_selected = True
            chosen_puzzle = ui.puzzle_menu()
            width = ui.column_width
    
            p = Puzzle(chosen_puzzle, width)
    #    print("Puzzle solving progress is: {}".format(p.making_progress))  # Debug
    
            while p.making_progress == True:
                p.solve_row_singles()
                after_rows_solving_total = p.calc_num_possible_values()
                p.solve_column_singles()
                after_columns_solving_total = p.calc_num_possible_values()
                p.solve_grid_singles()
                after_grids_solving_total = p.calc_num_possible_values()
    #        print("After row solving total = {}".format(after_rows_solving_total))  # DEBUG
    #        print("After column solving total = {}".format(after_columns_solving_total))  # DEBUG
    #        print("After grid solving total = {}".format(after_grids_solving_total))  # DEBUG
    #        print("PROGRESS STATE = {}".format(p.making_progress))  # DEBUG
                p.solve_pairs()
    
            p.display_puzzle()
            print()
    #        p.display_puzzle_narrow_column()
            p.show_state()
            p.calc_solved_counts()
            p.show_solved_unsolved_counts()

        if entry == "5":
            guesses = p.unsolved_spot_guesses()
            print(guesses)


if __name__ == "__main__":
    main()


