#!/usr/bin/env python3

# Practice with the different ANSI format options for strings
# such as bold, flashing, foreground colour, background colour etc

# Basic format is \033[Xm for X=2 to ?
# Reset format is \033[1m


for j in range(1,8):
    comment = ""
    if j == 1: comment = "bold"
    elif j == 2: comment = "faint"
    elif j == 3: comment = "italic"
    elif j == 4: comment = "underline"
    elif j == 5: comment = "flashing"
    elif j == 6: comment = "flashing"
    elif j == 7: comment = "reverse video"
    print("\033[{}m {:04d} {} \033[0m".format(j, j, comment))

for j in range(31, 41):
    print("\033[{}m {:04d} {} \033[0m".format(j, j, "foreground colour"))

for j in range(41, 48):
    print("\033[{}m {:04d} {} \033[0m".format(j, j, "background colour"))


