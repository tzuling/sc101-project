"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()

    dx = graphics.get_x_speed()
    dy = graphics.get_y_speed()

    lives = NUM_LIVES

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)

        if graphics.start and lives > 0 and graphics.count > 0:
            graphics.ball.move(dx, dy)

            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
            else:
                # ball touches paddle or bricks
                if graphics.get_obj():
                    if graphics.ball.y < graphics.window.height/2:  # bricks
                        dy = -dy
                    else:  # paddle
                        if dy > 0:  # ensure won’t stick on the paddle
                            dy = -dy
                # ball touches the window
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx
                if graphics.ball.y <= 0:
                    dy = -dy

            # update ball velocity
            if graphics.score > 0 and graphics.score % 200 == 0:
                dy += 0.1
                graphics.update_dy(dy)

        elif lives <= 0:
            # game over
            label = GLabel('Game Over', x=0, y=graphics.window.height/2)
            label.font = '-48-bold'
            label.color = 'red'
            graphics.window.add(label)
            graphics.window.remove(graphics.ball)
            break

        elif graphics.count <= 0:
            # you win
            label = GLabel('You Win!!!', x=0, y=graphics.window.height/2)
            label.font = '-48-bold'
            label.color = 'forestgreen'
            graphics.window.add(label)
            graphics.window.remove(graphics.ball)
            break

    # label animation
    label_dx = 1
    while label.x <= graphics.window.width / 2 - 120:
        label.move(label_dx, 0)
        pause(10)


if __name__ == '__main__':
    main()
