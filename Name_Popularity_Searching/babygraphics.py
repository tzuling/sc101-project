"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'black']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_width = width/len(YEARS)-1
    x_coordinate = x_width * year_index

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    # Top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       GRAPH_MARGIN_SIZE)
    # Bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Year line
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(GRAPH_MARGIN_SIZE+x_coordinate, 0, GRAPH_MARGIN_SIZE+x_coordinate,
                           CANVAS_HEIGHT)
        x_text = GRAPH_MARGIN_SIZE + x_coordinate + TEXT_DX
        y_text = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE + TEXT_DX
        canvas.create_text(x_text, y_text, text=YEARS[i], anchor=tkinter.NW)

    #################################


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    """
    x1, y1: the current point
    x2, y2: the next point
    rank: the name of rank of the year, "*" for more than 1000 
    c: the parameter of COLORS
    """
    c = 0

    for lookup_name in lookup_names:
        dic = name_data[lookup_name]
        for i in range(len(YEARS)-1):   # the last point doesn`t need to create line
            x1 = GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i)
            if str(YEARS[i]) in dic:
                rank = dic[str(YEARS[i])]
                y1 = GRAPH_MARGIN_SIZE + int(rank) * CANVAS_HEIGHT/MAX_RANK
            else:
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank = "*"

            canvas.create_text(x1 + TEXT_DX, y1, text=f'{lookup_name} {rank}',
                               anchor=tkinter.SW, fill=COLORS[c])

            x2 = GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH, i+1)
            if str(YEARS[i+1]) in dic:
                rank = dic[str(YEARS[i + 1])]
                y2 = GRAPH_MARGIN_SIZE + int(rank) * CANVAS_HEIGHT / MAX_RANK
            else:
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank = "*"

            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[c])

        canvas.create_text(x2 + TEXT_DX, y2, text=f'{lookup_name} {rank}',
                           anchor=tkinter.SW, fill=COLORS[c])
        c += 1
        if c == len(COLORS):
            c = 0
    #################################


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
