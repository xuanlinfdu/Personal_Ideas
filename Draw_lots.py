# This program can only work with codesulptor

import simplegui
import random

number = 0

def timer_handler():
    global number
    number = random.randrange(1, 101)
    
def draw_handler(canvas):
    canvas.draw_text(str(number), [10, 140], 100, 'White')
    
def button1():
    timer.start()
    
def button2():
    timer.stop()
    
frame = simplegui.create_frame('draw lots', 200, 200)
timer = simplegui.create_timer(10, timer_handler)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Start', button1, 100)
button2 = frame.add_button('Stop', button2, 100)


frame.start()
