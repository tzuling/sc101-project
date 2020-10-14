"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        self.start = False
        self.count = brick_cols * brick_rows

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        # func: set_ball_position()
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'

        # Default initial velocity for the ball.
        # func: set_ball_velocity()
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        self.reset_ball()
        onmouseclicked(self.mouse_click)
        onmousemoved(self.mouse_move)

        # Draw bricks.
        colors = ['royalblue', 'cadetblue', 'steelblue', 'darkturquoise', 'deepskyblue', 'skyblue', 'lightskyblue']
        x = 0
        y = brick_offset
        c = 0
        for row in range(0, brick_rows):
            for col in range(0, brick_cols):
                self.bricks = GRect(brick_width, brick_height, x=x, y=y)
                self.bricks.filled = True
                self.bricks.fill_color = colors[c]
                self.window.add(self.bricks)
                x = x + brick_width + brick_spacing
            y = y + brick_height + brick_spacing
            x = 0
            if row % 2 == 1:
                c += 1

    # check the ball touches bricks or paddle
    def get_obj(self):
        obj_ball_x_y = self.window.get_object_at(self.ball.x, self.ball.y)
        obj_ball_x_y_2r = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        obj_ball_x_2r_y = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        obj_ball_x_2r_y_2r = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        if obj_ball_x_y is not None:
            self.check_obj(obj_ball_x_y)
            return True
        elif obj_ball_x_2r_y is not None:
            self.check_obj(obj_ball_x_2r_y)
            return True
        elif obj_ball_x_y_2r is not None:
            self.check_obj(obj_ball_x_y_2r)
            return True
        elif obj_ball_x_2r_y_2r is not None:
            self.check_obj(obj_ball_x_2r_y_2r)
            return True

        # if obj_ball_x_y or obj_ball_x_y_2r or obj_ball_x_2r_y or obj_ball_x_2r_y_2r is not None:
        #     if obj_ball_x_y is not self.paddle: # 當 obj_ball_x_y == None 時也會是 True
        #         self.window.remove(obj_ball_x_y)
        #         self.count -= 1
        #     elif obj_ball_x_y_2r is not self.paddle:
        #         self.window.remove(obj_ball_x_y_2r)
        #         self.count -= 1
        #     elif obj_ball_x_2r_y is not self.paddle:
        #         self.window.remove(obj_ball_x_2r_y)
        #         self.count -= 1
        #     elif obj_ball_x_2r_y_2r is not self.paddle:
        #         self.window.remove(obj_ball_x_2r_y_2r)
        #         self.count -= 1
        #     return True

    def check_obj(self, obj):
        if obj is not self.paddle:
            self.window.remove(obj)
            self.count -= 1

    def set_ball_position(self):
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    def set_ball_velocity(self):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball(self):
        self.start = False
        self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def mouse_click(self, mouse_click):
        self.start = True

    def mouse_move(self, mouse_move):
        self.paddle.x = mouse_move.x - self.paddle.width / 2

    def get_x_speed(self):
        return self.__dx

    def get_y_speed(self):
        return self.__dy
