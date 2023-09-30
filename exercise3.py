# You are going to write a program that will mark a spot with an X.
# First, your program must take the user input and convert it to a usable format.
#
# Next, you need to use that input to update your nested list with an "x". Remember that your nested list map
# actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].
#
# Example Input 1
# column 2, row 3 would be entered as:
#
# 23
# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
# Example Input 2
# column 3, row 1 would be entered as:
#
# 31
# Example Output 2
# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
######################################################
######################################################
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
# To address the scenario where users enter spaces between rows and columns..
cell = "".join((input("enter the address of cell you want to mark first row then column ")).split())
# 1) input() : 2 3
# 2) "2 3".split()=['2', '3']
# 3) "".join(['2', '3'])="23"

row = (int(cell[0])) - 1
column = (int(cell[1])) - 1
if row > 2 or column > 2:
    print("row or column can not exceed 3")
else:
    maps[row][column] = 'X '
    print(f"{row1}\n{row2}\n{row3}\n")
