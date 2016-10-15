# This program can only work with codesulptor
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction:
        ball_vel = [2.0 * random.random() + 2.0, -2.0 * random.random() - 1.0]
    else:
        ball_vel = [-2.0 * random.random() - 2.0, -2.0 * random.random() - 1.0]
        
        
# Randomization of velocity
def direction():
    rand_vel = random.randrange(0, 2)
    if rand_vel == 0:
        return LEFT
    else:
        return RIGHT
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(direction())
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1,"White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos[1] - HALF_PAD_HEIGHT) >= 4) and ((paddle1_pos[1] + HALF_PAD_HEIGHT) <= (HEIGHT - 4)):
        paddle1_pos[1] += paddle1_vel
    elif ((paddle1_pos[1] - HALF_PAD_HEIGHT) < 4) and (paddle1_vel > 0):
        paddle1_pos[1] += paddle1_vel
    elif ((paddle1_pos[1] + HALF_PAD_HEIGHT) > (HEIGHT - 4)) and (paddle1_vel < 0):
        paddle1_pos[1] += paddle1_vel
    if ((paddle2_pos[1] - HALF_PAD_HEIGHT) >= 4) and ((paddle2_pos[1] + HALF_PAD_HEIGHT) <= (HEIGHT - 4)):
        paddle2_pos[1] += paddle2_vel
    elif ((paddle2_pos[1] - HALF_PAD_HEIGHT) < 4) and (paddle2_vel > 0):
        paddle2_pos[1] += paddle2_vel
    elif ((paddle2_pos[1] + HALF_PAD_HEIGHT) > (HEIGHT - 4)) and (paddle2_vel < 0):
        paddle2_pos[1] += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], \
                         [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT], \
                         [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT], \
                         [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT]], \
                        1, "White", "White")
    
    canvas.draw_polygon([[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], \
                         [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT], \
                         [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT], \
                         [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT]], \
                        1, "White", "White")
    
    # determine whether paddle and ball collide    
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS):
        ball_vel[1] = -1 * ball_vel[1]
    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        if (ball_pos[1] > (paddle1_pos[1] - HALF_PAD_HEIGHT)) and (ball_pos[1] < (paddle1_pos[1] + HALF_PAD_HEIGHT)):
            ball_vel[0] = -1 * ball_vel[0]
            ball_vel[0] = 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            spawn_ball(direction())
            score2 += 1
    if ball_pos[0] >= (WIDTH - 1 - PAD_WIDTH - BALL_RADIUS):
        if (ball_pos[1] > (paddle2_pos[1] - HALF_PAD_HEIGHT)) and (ball_pos[1] < (paddle2_pos[1] + HALF_PAD_HEIGHT)):
            ball_vel[0] = -1 * ball_vel[0]
            ball_vel[0] = 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            spawn_ball(direction())
            score1 += 1
            
            
    # draw scores
    canvas.draw_text(str(score1), [135, 60], 60, "White")
    canvas.draw_text(str(score2), [435, 60], 60, "White")
        
def keydown(key):
    v_cste = 4
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -v_cste
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = v_cste
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -v_cste
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = v_cste
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("restart", new_game, 200)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
