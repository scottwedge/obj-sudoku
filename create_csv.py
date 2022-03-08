#!/usr/bin/env python3

import csv


p1 = [7,4,5,0,9,0,0,0,0,\
0,3,2,1,5,0,0,4,6,\
0,0,0,2,8,0,5,0,3,\
2,0,0,0,0,0,0,6,0,\
9,8,0,6,0,0,3,5,1,\
0,0,0,5,4,0,2,0,7,\
3,0,8,0,0,0,0,0,2,\
0,2,0,7,6,0,0,1,0,\
0,6,0,9,0,8,0,3,4]
    
p2 = [8,0,0,7,0,6,0,0,0,\
0,0,6,0,0,0,0,5,0,\
0,9,2,4,0,0,0,7,6,\
9,0,7,6,2,1,5,0,3,\
0,2,0,0,0,0,0,1,0,\
5,0,1,9,4,7,6,0,8,\
2,5,0,0,0,4,1,8,0,\
0,6,0,0,0,0,2,0,0,\
0,0,0,2,0,5,0,0,4]
    
p3 = [0,0,0,0,0,0,0,1,7,\
0,0,7,0,6,2,0,0,5,\
4,0,0,0,1,0,0,0,0,\
0,7,0,0,0,3,0,0,8,\
0,0,3,5,0,4,1,0,0,\
8,0,0,1,0,0,0,6,0,\
0,0,0,0,4,0,0,0,9,\
1,0,0,7,9,0,2,0,0,\
3,4,0,0,0,0,0,0,0]
    
p4 = [0,0,0,2,0,1,5,0,3,\
2,0,0,0,0,6,0,7,0,\
0,0,9,0,0,0,0,0,0,\
9,0,0,0,8,0,7,0,2,\
0,1,0,0,0,0,0,3,0,\
8,0,6,0,1,0,0,0,9,\
0,0,0,0,0,0,9,0,0,\
0,9,0,8,0,0,0,0,6,\
3,0,8,7,0,2,0,0,0]


"""
valid_entry = False
while not valid_entry:
    print("There are four puzzles to choose from.")
    entry = input("Enter 1, 2, 3 or 4 to select puzzle")

    if entry == "1" or entry =="2" or entry == "3" or entry == "4":
        valid_entry = True  # Exit while loop

if entry == "1":
    p = p1
if entry == "2":
    p = p2
if entry == "3":
    p = p3
if entry == "4":
    p = p4

for j in p:
    print(p)

file = "/tmp/t"
with open(file, "w", newline ="") as f:
    csv_writer = csv.writer(f)
    for j in p:
        csv_writer.writerow(j)

#csv_writer = csv.writer(f)
"""

"""

with  open("/tmp/t", "w") as f2:  # Open file in write mode
    writer = csv.writer(f2)  # Create the csv writer
    writer.writerow(row)  # Write a row to the csv file

#f.close()  # Close the file
"""

#row = "alkfhlkahdflh alhafjvb,mzbxcvm,kjlhfioqyto8q345yoqywrfiohjfd"
with open("/tmp/s", "r") as r1:  # Open file to read from
    row = r1.readlines()
    print(row)
