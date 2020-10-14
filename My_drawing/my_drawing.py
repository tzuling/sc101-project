"""
File: my_drawing.py
Name: Sabrina
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(800, 500, title='my_drawing.py')

FIRST_X = 600
FIRST_Y = 50
REDUCE = 80

ROBOT_FACE_X = 650
ROBOT_FACE_Y = 300

ROBOT_BODY_X = ROBOT_FACE_X + 20
ROBOT_BODY_Y = ROBOT_FACE_Y + 75


def main():
    # background
    background_color = ['ivory', 'lightblue', 'skyblue']

    for i in range(0, 3):
        background = GRect(window.width, window.height/3, x=0, y=window.height/3 * i)
        background.filled = True
        background.fill_color = ''+background_color[i]
        background.color = ''+background_color[i]
        window.add(background)

    # pyramid
    pyramid_color = ['saddlebrown', 'darkgoldenrod', 'goldenrod', 'orange', 'gold', 'palegoldenrod', 'lemonchiffon']

    for i in range(0, 7):
        # pyramid Grect
        pyramid = GRect(FIRST_X - REDUCE * i, FIRST_Y, x=5 + REDUCE / 2 * i, y=window.height - FIRST_Y * (1+i))
        pyramid.filled = True
        pyramid.fill_color = ''+pyramid_color[i]
        window.add(pyramid)

        # pyramid GLabel
        # pyramid_label = GLabel('STAGE '+str(i+1), x=260, y=window.height - FIRST_Y * i -10)
        # pyramid_label.font = '-24'
        # pyramid_label.color = 'darkgrey'
        # window.add(pyramid_label)

    # flag
    flagstaff = GRect(5, 100, x=280, y=50)
    flagstaff.filled =True
    flagstaff.fill_color = 'brown'
    window.add(flagstaff)

    flag = GRect(100, 40, x=285, y=50)
    flag.filled = True
    flag.fill_color = 'silver'
    window.add(flag)

    flag_label = GLabel('GOAL!!!', x=290, y=85)
    flag_label.font = '-26'
    flag_label.color = 'red'
    window.add(flag_label)

    # sun
    sun()

    # robot
    robot_face()
    robot_body()


def robot_face():
    # head
    head = GOval(60, 60, x=ROBOT_FACE_X+25, y=ROBOT_FACE_Y-15)
    head.filled = True
    head.fill_color = 'slateblue'
    window.add(head)

    # ear
    ear = GOval(120, 60, x=ROBOT_FACE_X-5, y=ROBOT_FACE_Y+5)
    ear.filled = True
    ear.fill_color = 'magenta'
    window.add(ear)

    # face
    face = GRect(110, 75, x=ROBOT_FACE_X, y=ROBOT_FACE_Y)
    face.filled = True
    face.fill_color = 'lightgray'
    window.add(face)

    # eye
    l_eye_outer = GOval(30, 30, x=ROBOT_FACE_X + 10, y=ROBOT_FACE_Y + 5)
    l_eye_outer.filled = True
    l_eye_outer.fill_color = 'white'
    window.add(l_eye_outer)

    l_eye_inner = GOval(25, 25, x=ROBOT_FACE_X+10, y=ROBOT_FACE_Y + 5)
    l_eye_inner.filled = True
    l_eye_inner.fill_color = 'gold'
    window.add(l_eye_inner)

    r_eye_outer = GOval(30, 30, x=ROBOT_FACE_X + 70, y=ROBOT_FACE_Y + 5)
    r_eye_outer.filled = True
    r_eye_outer.fill_color = 'white'
    window.add(r_eye_outer)

    r_eye_inner = GOval(25, 25, x=ROBOT_FACE_X + 70, y=ROBOT_FACE_Y + 5)
    r_eye_inner.filled = True
    r_eye_inner.fill_color = 'gold'
    window.add(r_eye_inner)

    # nose
    nose = GOval(20, 20, x=ROBOT_FACE_X + 45, y=ROBOT_FACE_Y + 22)
    nose.filled = True
    nose.fill_color = 'steelblue'
    window.add(nose)

    # mouth
    mouth = GRect(80, 15, x=ROBOT_FACE_X+15, y=ROBOT_FACE_Y+50)
    mouth.filled = True
    mouth.fill_color = 'ivory'
    window.add(mouth)


def robot_body():
    # body
    body = GRect(70, 70, x=ROBOT_BODY_X, y=ROBOT_BODY_Y)
    body.filled = True
    body.fill_color = 'red'
    window.add(body)

    body_label = GLabel('stanCode', x=body.x+5, y=body.y+20)
    body_label.font = '-14'
    body_label.color = 'white'
    window.add(body_label)

    # arm
    l_arm = GRect(20, 20, x=ROBOT_FACE_X, y=ROBOT_BODY_Y)
    l_arm.filled = True
    l_arm.fill_color = 'red'
    window.add(l_arm)

    r_arm = GRect(20, 20, x=ROBOT_FACE_X + 90, y=ROBOT_BODY_Y)
    r_arm.filled = True
    r_arm.fill_color = 'red'
    window.add(r_arm)

    # hand
    l_hand = GRect(15, 50, x=l_arm.x+5, y=ROBOT_BODY_Y+20)
    l_hand.filled = True
    l_hand.fill_color = 'lightgrey'
    window.add(l_hand)

    l_hand_1_outer = GOval(20, 20, x=l_hand.x-3, y=l_hand.y+40)
    l_hand_1_outer.filled = True
    l_hand_1_outer.fill_color = 'grey'
    window.add(l_hand_1_outer)

    l_hand_1_inner = GOval(10, 10, x=l_hand_1_outer.x+5, y=l_hand_1_outer.y+10)
    l_hand_1_inner.filled = True
    l_hand_1_inner.fill_color = 'skyblue'
    window.add(l_hand_1_inner)

    r_hand = GRect(15, 50, x=r_arm.x, y=ROBOT_BODY_Y + 20)
    r_hand.filled = True
    r_hand.fill_color = 'lightgrey'
    window.add(r_hand)

    r_hand_1_outer = GOval(20, 20, x=r_hand.x, y=r_hand.y + 40)
    r_hand_1_outer.filled = True
    r_hand_1_outer.fill_color = 'grey'
    window.add(r_hand_1_outer)

    r_hand_1_inner = GOval(10, 10, x=r_hand_1_outer.x + 5, y=r_hand_1_outer.y + 10)
    r_hand_1_inner.filled = True
    r_hand_1_inner.fill_color = 'skyblue'
    window.add(r_hand_1_inner)

    # leg
    l_leg = GRect(15, 50, x=ROBOT_BODY_X+15, y=ROBOT_BODY_Y+70)
    l_leg.filled = True
    l_leg.fill_color = 'lightgrey'
    window.add(l_leg)

    r_leg = GRect(15, 50, x=ROBOT_BODY_X + 40, y=ROBOT_BODY_Y + 70)
    r_leg.filled = True
    r_leg.fill_color = 'lightgrey'
    window.add(r_leg)

    # shoe
    l_shoe = GRect(25, 15, x=l_leg.x-5, y=l_leg.y+40)
    l_shoe.filled = True
    l_shoe.fill_color = 'black'
    window.add(l_shoe)

    r_shoe = GRect(25, 15, x=r_leg.x-5, y=r_leg.y+40)
    r_shoe.filled = True
    r_shoe.fill_color = 'black'
    window.add(r_shoe)


def sun():
    sun_0 = GOval(100, 100)
    sun_0.filled = True
    sun_0.fill_color = 'orangered'
    sun_0.color = 'orangered'
    window.add(sun_0)

    sun_1 = GOval(40, 20, x=110, y=40)
    sun_1.filled = True
    sun_1.fill_color = 'orangered'
    sun_1.color = 'orangered'
    window.add(sun_1)

    sun_2 = GOval(20, 40, x=40, y=110)
    sun_2.filled = True
    sun_2.fill_color = 'orangered'
    sun_2.color = 'orangered'
    window.add(sun_2)

    sun_3 = GOval(20, 20, x=95, y=0)
    sun_3.filled = True
    sun_3.fill_color = 'orangered'
    sun_3.color = 'orangered'
    window.add(sun_3)

    sun_4 = GOval(20, 20, x=95, y=90)
    sun_4.filled = True
    sun_4.fill_color = 'orangered'
    sun_4.color = 'orangered'
    window.add(sun_4)

    sun_5 = GOval(20, 20, x=0, y=95)
    sun_5.filled = True
    sun_5.fill_color = 'orangered'
    sun_5.color = 'orangered'
    window.add(sun_5)


if __name__ == '__main__':
    main()
