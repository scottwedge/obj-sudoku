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
        self.normal_column_width = True  # "normal" == True (default);  "narrow" == False
        self.puzzle_selected = False

    def start_menu(self):
        print()  # Spacing blank line
        print("Please choose one of the following options:")
        entry = input("1. Select puzzle\n2. Solve puzzle\n3. Show puzzle\n4. Display puzzle with normal column width (default)\n5. Display puzzle with narrow column width\n6. Display puzzle with single lines around internal grids (default)\n7. Display puzzle with double lines around internal grids\n8. List unresolved spots and their possible values\n9. Select a spot and try one of its possible values\n10. Quit game\nEnter selection: ")
        if entry == "1":  # Select puzzle
            return entry
        elif entry == "2":  # Solve puzzle
            return entry
        elif entry == "3":  # Show puzzle
            return entry
        elif entry == "4":  # Use normal column width (default)
            return entry
        elif entry == "5":  # Use narrow column width  (not default)
            return entry
        elif entry == "6":  # Use single lines around internal grids (default)
            return entry
        elif entry == "7":  # Use double lines (++======++ or ||) around internal grids
            return entry
        elif entry == "8":  # List unresolved spots and their values
            return entry
        elif entry == "9":  # Select a spot and guess a value 
            return entry
        elif entry == "10":  # Exit game
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

    def choose_unresolved_spot(self, guesses):
        self.guesses = guesses
        valid_value = False
        while not valid_value:  # Loop until valid spot is entered
            print()  # Blank spacer line
            entry = input("Select a spot to guess a value: ")
            try:
                entry = int(entry)
                if entry not in self.guesses:
                    print("{} is not valid. Choose from the Spot list above".format(entry))
                else:
                    valid_value = True
            except ValueError:
                print("Enter an integer value")
        return entry

    def guess_unresolved_value(self, guesses, spot_entry):  # Select value for guess
        self.guesses = guesses
        self.spot_entry = spot_entry
        possible_values = self.guesses[self.spot_entry]
        guess_attempt = False
        while not guess_attempt:  # Loop until valid guess is entered
            print()
            print("Possible values to select for spot {} are: ".format(self.spot_entry), end = "")
            possible_values_string = "{}".format(possible_values[0])  # Print first of possible value 
            for j in range(1, len(possible_values)):
                possible_values_string += " or {}".format(possible_values[j])  # Print 'or' between remaining possible values 
            possible_values_string += "."  # Print end of line
            print(possible_values_string)
            print()
            guess_value = input("Select one of the content values to try in the puzzle: ")
            try:
                guess_value = int(guess_value)
                if guess_value not in possible_values:
                    print("Choose one of the valid values for spot {} which are {}.".format(self.spot_entry, possible_values))
                else:
                    guess_attempt = True
            except ValueError:
                print()
                print("'{}' is not a valid choice. Enter one of: {}".format(guess_value, possible_values_string))
        return guess_value

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
        self.normal_column_width = width  # set in UserInput.start_menu
        self.num_spots = len(self.initial_values)  # Handle both 9x9 or 16x16 puzzle
        self.full_side = int(self.num_spots ** 0.5)  # Handle both 9x9 or 16x16 puzzle
        self.part_side = int(self.num_spots ** 0.25)  # Handle both 9x9 or 16x16 puzzle
        self.state = "Initiated"
        self.action = "Initiating"
        self.making_progress = True  # Set initial value
        self.num_possible_values = self.num_spots ** 2  # Initialize to largest possible value
        self.narrow_divider_line = "+-+-+-+-+-+-+-+-+-+"  # Initialize value
        self.normal_divider_line = "+--+--+--+--+--+--+--+--+--+"  # Initialize value
        self.narrow_divider_double_line = "++===+===+===++"  # Initialize value
        self.normal_divider_double_line = "++=====+=====+=====++"  # Initialize value
        self.use_single_line = True  # Highlight internal grid boundaries with single (default) line
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
        self.create_normal_divider_line(cw)  # Create divider line for normal column width
        self.create_narrow_divider_line(cw)  # Create divider line for narrow column width
        self.create_normal_divider_double_line(cw)  # Create double divider for normal column width
        self.create_narrow_divider_double_line(cw)  # Create double divider for narrow column width
        return cw

    def create_normal_divider_line(self, cw):  
        # Line has '+' at every intersection and '-' in between - for normal width columns puzzle
        self.cw = cw
        if self.use_single_line == True:
            normal_line = "+"  # First character
        else:
            normal_line = "++"  # First character

        for j in self.cw:
            if self.use_single_line == True:             
                normal_line += + 3 * self.cw[j] * '-' + "+"  # Want three '-' for every number in grid
            else:  # use_single_line == False
                if (j+1) % self.part_side == 0:
                    normal_line += + 3 * self.cw[j] * '-' + "++"  # grid intersection is '+'
                else:
                    normal_line += + 3 * self.cw[j] * '-' + "+"  # grid intersection is '++'
          

 
        self.normal_divider_line = normal_line

    def create_normal_divider_double_line(self, cw):  
        # Line has '++' at internal grid intersection and '=' in between for normal width columns puzzle
        self.cw = cw
        double_line = "++"  # First characters
        for j in self.cw:
            if (j+1) % self.part_side == 0:
                double_line +=  3 * self.cw[j] * '=' + "++"  # Want '++' at internal grid intersection
            else:
                double_line +=  3 * self.cw[j] * '=' + "+"  # Want three '=' for every number in grid
                
        self.normal_divider_double_line = double_line

    def create_narrow_divider_line(self, cw):  
        # Line has '+' at every intersection and '-' in between - for narrow width columns puzzle
        self.cw = cw
        if self.use_single_line == True:
            narrow_line = "+"  # First character
        else:
            narrow_line = "++"  # First character

        for j in self.cw:
            if self.use_single_line == True:             
                narrow_line += + (2 * self.cw[j] + 1) * '-' + "+"  #Dh  Want two '-' plus one for every number in grid
            else:  # use_single_line == False
                if (j+1) % self.part_side == 0:
                    narrow_line += + (2 * self.cw[j] + 1) * '-' + "++"  #Dh  Want two '-' plus one for every number in grid
                else:
                    narrow_line += + (2 * self.cw[j] + 1) * '-' + "+"  #Dh  Want two '-' plus one for every number in grid
        self.narrow_divider_line = narrow_line

    def create_narrow_divider_double_line(self, cw):  
        # Line has '++' at every internal grid intersection and '=' in between for narrow width columns puzzle
        self.cw = cw
        double_line = "++"  # First characters
        for j in self.cw:
            if (j+1) % self.part_side == 0:
                double_line += + (2 * self.cw[j] + 1) * '=' + "++"  #Dh  Want two '= plus one for every number in grid
            else:
                double_line += + (2 * self.cw[j] + 1) * '=' + "+"  #Dh  Want two '= plus one for every number in grid
        self.narrow_divider_double_line = double_line


    def display_puzzle_normal_column(self):
        cw = self.calc_column_widths()  # Get max column widths and create divider lines
        self.p_divider_line(-1)  # Print top-most divider line

        for j in range(self.num_spots):
            if self.use_single_line == False and (j % self.part_side == 0):
                print("||{:^{}}".format(str(self.puzz[j].get_con()), 3*cw[j%self.full_side]), end = "")  # Must convert to string to print list
            else:
                print("|{:^{}}".format(str(self.puzz[j].get_con()), 3*cw[j%self.full_side]), end = "")  # Must convert to string to print list
                if (j+1) % self.full_side == 0 and self.use_single_line == False:
                    print("||")  # Print end of line at end of each line
                    self.p_divider_line(j)  # Determine if print normal/wide column single/double divider line
                elif (j+1) % self.full_side == 0 and self.use_single_line == True:
                    print("|")  # Print end of line at end of each line
                    self.p_divider_line(j)  # Determine if print normal/wide column single/double divider line
                else:
                    pass
             

    def display_puzzle_narrow_column(self):
        cw = self.calc_column_widths()  # Get max column widths
        self.p_divider_line(-1)

        for j in range(self.num_spots):
            if self.use_single_line == False and (j % self.part_side == 0):
                print("||{:^{}}".format(str(self.puzz[j].short_list_string()), 2*cw[j%self.full_side] + 1), end = "")  # Must convert to string to print list
            else:
                print("|{:^{}}".format(str(self.puzz[j].short_list_string()), 2*cw[j%self.full_side] + 1), end = "")  # Must convert to string to print list
                if (j+1) % self.full_side == 0 and self.use_single_line == False:
                    print("||")  # Print end of line at end of each line
                    self.p_divider_line(j)  # Determine if print normal/wide column single/double divider line
                elif (j+1) % self.full_side == 0 and self.use_single_line == True:
                    print("|")  # Print end of line at end of each line
                    self.p_divider_line(j)  # Determine if print normal/wide column single/double divider line
                else:
                    pass
             

    def display_puzzle(self):
        if self.normal_column_width == True:  # Determine if normal columns 
            self.display_puzzle_normal_column()
        else:  # Determine if narrow columns 
            self.display_puzzle_narrow_column()

    def p_divider_line(self, j):  # Determine if print normal/wide column single/double divider line
        if (self.use_single_line == False) and ((j + 1) % (self.part_side ** 3) == 0):
            self.p_double_line(j)  # print double line
        else:
            self.p_single_line(j)  # print single line

    def p_double_line(self,j):
        if self.normal_column_width == True:  # Determine if normal or narrow columns 
            print(self.normal_divider_double_line)  # Print normal horizontal line between rows
        else:
            print(self.narrow_divider_double_line)  # Print narrow horizontal line between rows

    def p_single_line(self,j):
        if self.normal_column_width == True:  # Determine if normal or narrow columns 
            print(self.normal_divider_line)  # Print normal double horizontal line between rows
        else:
            print(self.narrow_divider_line)  # Print narrow double horizontal line between rows

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

    def solve_all(self):
        self.solve_row_singles()
        after_rows_solving_total = self.calc_num_possible_values()
        self.solve_column_singles()
        after_columns_solving_total = self.calc_num_possible_values()
        self.solve_grid_singles()
        after_grids_solving_total = self.calc_num_possible_values()
        print("After row solving total = {}".format(after_rows_solving_total))  #DEBUG
        print("After column solving total = {}".format(after_columns_solving_total))  #DEBUG
        print("After grid solving total = {}".format(after_grids_solving_total))  #DEBUG
        print("PROGRESS STATE = {}".format(self.making_progress))  #DEBUG
        self.solve_pairs()

    def check_sanity(self):  # Determine if puzzle still sane after guess a value for spot(s)
        # Verify that maximum of only one count of every value in every row, column or internal grid
        # Otherwise the grid is insane and the last guess was incorrect
        sane_row = self.check_row_sanity()
        sane_column = self.check_column_sanity()
        sane_grid = self.check_grid_sanity()
        return sane_row and sane_column and sane_grid  # False if any are False

    def reset_counters(self):  # Reset all dictionary values to zero
        d = dict()
        for j in range(self.full_side):
            d[j] = 0
        return d

    def check_counters(self, count):
        sane = True
        self.count = count
        for j in range(len(count)):
            if count[j] > 1:
                sane = False
        return sane

    def check_row_sanity(self):
        # For every row, reset counts, then cycle through every spot and check each row for a value with >1 count.
        for row in self.full_side: # for every row
            sanity = True
            count = self.reset_counters()  # reset counters
            for j in self.num_spots:  # for every spot in puzzle
                if row == self.puzz[j].get_row() and self.puzz[k].get_known() == True:
                    count[self.puzz[j].get_con()] += 1  # Increment count if known value and in matching row
            sanity = sanity and self.check_counters(count) 
        return sanity

    def check_column_sanity(self):
        # For every column, reset counts, then cycle through every spot and check each column for a value with >1 count.
        for column in self.full_side: # for every column
            sanity = True
            count = self.reset_counters()  # reset counters
            for j in self.num_spots:  # for every spot in puzzle
                if column == self.puzz[j].get_column() and self.puzz[k].get_known() == True:
                    count[self.puzz[j].get_con()] += 1  # Increment count if known value and in matching row
            sanity = sanity and self.check_counters(count) 
        return sanity

    def check_grid_sanity(self):
        # For every grid, reset counts, then cycle through every spot and check each grid for a value with >1 count.
        for grid in self.full_side: # for every grid
            sanity = True
            count = self.reset_counters()  # reset counters
            for j in self.num_spots:  # for every spot in puzzle
                if grid == self.puzz[j].get_grid() and self.puzz[k].get_known() == True:
                    count[self.puzz[j].get_con()] += 1  # Increment count if known value and in matching row
            sanity = sanity and self.check_counters(count) 
        return sanity


def main():
   
    ui = UserInput()
    while ui.play_game == True:  # Play game until quit

        entry = ui.start_menu()  # Choose option in Starting menu
    
        if entry == "1":
            ui.puzzle_selected = True
            chosen_puzzle = ui.puzzle_menu()
            width = ui.normal_column_width
    
            p = Puzzle(chosen_puzzle, width)
    
        if entry == "2":  # Solve
            p.making_progress = True
            while p.making_progress == True:
                p.solve_all()

        if entry == "3":  # Show
            p.display_puzzle()
            print()
            p.show_state()
            p.calc_solved_counts()
            p.show_solved_unsolved_counts()

        if entry == "4":  # Use normal column width (default)
            p.normal_column_width = True

        if entry == "5":  # Use narrow column width  (not default)
            p.normal_column_width = False  # For 'narrow' column width

        if entry == "6":  # Use single lines around internal grids (default)
            p.use_single_line = True  # Highlight internal grid boundaries with double line

        if entry == "7":  # Use double lines (++======++ or ||) around internal grids
            p.use_single_line = False  # Highlight internal grid boundaries with double line

        if entry == "8":
            guesses = p.unsolved_spot_guesses()
            for j in guesses:
                print("Spot {} contains {}".format(j, guesses[j]))

        if entry == "9":
            guesses = p.unsolved_spot_guesses()
            guesses_list = list(guesses.items())
            padded_guesses_list = copy.copy(guesses_list)
            l = len(guesses_list)
            excess = l % 4
            if excess != 0:
                num_padding = 4 - excess  # Pad the list with blanks since print four values per line
                for j in range(num_padding):
                    padded_guesses_list.append(("",""))

            print("Number of unresolved spots is {}.".format(l))
            print()  # Spacer line
            print("Unresolved spots and contents are:")
            w1 = 5  # Format width for spot number
            w2 = 18  # Format width for contents number

            t1 = "Spot"
            t2 = "Contents"
            print("{:{}}{:{}}{:{}}{:{}}{:{}}{:{}}{:{}}{:{}}".format(str(t1), w1,str(t2), w2, str(t1), w1, str(t2), w2, str(t1), w1, str(t2), w2, str(t1), w1, str(t2), w2))
            for j in range(0, len(padded_guesses_list), 4):  # Print four spots per line
                (a, b) = padded_guesses_list[j]
                (c, d) = padded_guesses_list[j + 1]
                (e, f) = padded_guesses_list[j + 2]
                (g, h) = padded_guesses_list[j + 3]
                print("{:{}}{:{}}{:{}}{:{}}{:{}}{:{}}{:{}}{:{}}".format(str(a), w1,str(b), w2, str(c), w1, str(d), w2, str(e), w1, str(f), w2, str(g), w1, str(h), w2))

            spot_entry = ui.choose_unresolved_spot(guesses)  # Select spot for guess
            guess_value = ui.guess_unresolved_value(guesses, spot_entry)  # Select value for guess

            g = copy.copy(p)  # Make copy of stalled puzzle; try guess on copy
            print("OLD VALUE", g.puzz[spot_entry].get_con())  #DEBUG  # get old value
            g.puzz[spot_entry].set_con(guess_value)   # Set new value
            g.puzz[spot_entry].set_known(True)   # Set to True
            g.making_progress = True  # Must switch from False
            print("NEW VALUE", g.puzz[spot_entry].get_con())  #DEBUG  # get NEW value

            while g.making_progress == True:
                g.solve_all()
    
            g.display_puzzle()
            print()
            g.show_state()
            g.calc_solved_counts()
            g.show_solved_unsolved_counts()


if __name__ == "__main__":
    main()

