"""
File: bouncing_ball.py
Name: Sabrina
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.3
START_X = 30
START_Y = 40

# Global variables
count = 0
start = False
window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    global start, count
    vy = 0

    # create bouncing ball
    start_ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    start_ball.filled = True
    start_ball.fill_color = 'black'
    window.add(start_ball)

    # mouse click to start
    onmouseclicked(mouse_click)

    # run up to three times
    while True:
        if count < 3 and start:
            while start_ball.x <= window.width + SIZE:
                start_ball.move(VX, vy)
                # if ball touch the ground
                if start_ball.y >= window.height - SIZE:
                    start_ball.y = window.height - SIZE # 避免REDUCE低到彈不起來，也可黏在地板上
                    vy *= -REDUCE

                vy = vy + GRAVITY
                # for the anime
                pause(DELAY)

            start = False
            count += 1

        elif count >= 3:
            break

        start_ball.x = START_X
        start_ball.y = START_Y
        # for while True
        pause(DELAY)


def mouse_click(mouse):
    global start
    start = True


if __name__ == "__main__":
    main()
