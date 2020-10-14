"""
File: draw_line.py
Name: Sabrina
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(title="draw_line.py")
SIZE = 10

count = 0
first_click_x = 0
first_click_y = 0
large_cir = GOval(SIZE, SIZE)
small_cir = GOval(SIZE-2, SIZE-2)


def main():
    onmouseclicked(draw_line)


def draw_line(mouse):
    global count, first_click_x, first_click_y

    # draw line and remove hollow circle
    if count % 2 == 0:
        first_click_x = mouse.x
        first_click_y = mouse.y

        # create hollow circle
        # large_cir = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        large_cir.x = first_click_x - SIZE/2
        large_cir.y = first_click_y - SIZE/2
        large_cir.filled = True
        large_cir.fill_color = "black"
        window.add(large_cir)

        # small_cir = GOval(SIZE - 2, SIZE - 2, x=mouse.x - (SIZE - 2) / 2, y=mouse.y - (SIZE - 2) / 2)
        small_cir.x = first_click_x - (SIZE-2)/2
        small_cir.y = first_click_y - (SIZE-2)/2
        small_cir.filled = True
        small_cir.fill_color = "white"
        window.add(small_cir)
    else:
        line = GLine(first_click_x, first_click_y, mouse.x, mouse.y)
        window.add(line)
        window.remove(large_cir)
        window.remove(small_cir)

    count += 1


if __name__ == "__main__":
    main()
