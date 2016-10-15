# This program can only work with codesulptor
# implementation of card game - Memory


import simplegui
import random
    
count = 0

# helper function to initialize globals
def new_game():
    global number_int, exposed, state
    number_int = range(8) + range(8)
    random.shuffle(number_int)
    exposed = []
    for i in range(16):
        exposed.append(False)
    state = 0
    count = 0
    turns = 'Turns = ' + str(count)
    label.set_text(turns)
    
# define event handlers
def mouseclick(pos):
    global sequence, exposed, state, parity1, parity2, count, turns
    pos_click = list(pos)
    for i in range(16):
        if (pos_click[0] >= (1 + i * 50)) and (pos_click[0] <= (50 + i * 50)):
            sequence = i
    if exposed[sequence] == False:
        exposed[sequence] = True
        if state == 2:
            count = count + 1
            turns = 'Turns = ' + str(count)
            label.set_text(turns)
            if number_int[parity1] != number_int[parity2]:
                exposed[parity1] = False
                exposed[parity2] = False
        if state == 0:
            state = 1
        elif state == 1:
            state = 2
        else:
            state = 1
        if state == 1:
            parity1 = sequence
        elif state == 2:
            parity2 = sequence
    print state
    
                                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global number_int, exposed
    for i in range(16):
        canvas.draw_text(str(number_int[i]), [i * 50 + 5, 78], 80, 'White')
        
    for j in range(16):
        if not exposed[j]:
            canvas.draw_polygon([[1 + j * 50, 0], \
                             [50 + j * 50, 0], \
                             [50 + j * 50, 100], \
                             [1 + j * 50, 100]],\
                         2, 'Black', 'Green')
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = 0')

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
