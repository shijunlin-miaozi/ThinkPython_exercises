# Think Python 2nd Edition book_Ch3.Functions_p27

# Exercise 3.3. Note: This exercise should be done using only the statements and other features we have learned so far.

# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# 2. Write a function that draws a similar grid with four rows and four columns.


def line_plus_minus (row):
    # draw the horizontal line with "+""-" based on num of rows given
    incremental = " - - - - +"
    full_line = "+" + (incremental * row)
    print(full_line)

def line_pipe_x4 (row):
    # draw the horizontal line with "|" based on num of rows given
    # propagate the line 4 times vertically
    incremental = "         |"
    full_line = "|" + (incremental * row)
    for i in range(4):
        print(full_line)
        i += 1

def draw_grid (row, column):
    # propagate the grid vertially based on num of columns given
    line_plus_minus(row)
    for i in range(column):
        line_pipe_x4(row)
        line_plus_minus(row)
        i += 1

draw_grid(4, 4)