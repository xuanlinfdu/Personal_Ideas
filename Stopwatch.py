# This program can only work with codesulptor

# template for "Stopwatch: The Game"
import simplegui


# define global variables
interval = 100
width = 300
height = 200
t = 0
try_win = 0
try_total = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tensecond
    tensecond = t % 10
    second_total = (t - tensecond) / 10
    second = second_total % 60 
    minute = (second_total - second) / 60
    return str(minute) + ":" + str(second) + "." + str(tensecond)

# define event handlers for buttons; "Start", "Stop", "Reset"   
def startwatch():
    timer.start()
    
def stopwatch():
    global try_win, try_total
    if timer.is_running():
        timer.stop()
        if tensecond == 0:
            try_win = try_win + 1;
            try_total = try_total + 1;
        else:
            try_total = try_total + 1;
            
def resetwatch():
    global t, try_win, try_total
    timer.stop()
    t = 0
    try_win = 0
    try_total = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t = t + 1
    
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [80, 110], 40, "White")
    win_times =  str(try_win) + "/" + str(try_total)
    canvas.draw_text(win_times, [250,30], 30, "Green")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", startwatch, 200)
frame.add_button("Stop", stopwatch, 200)
frame.add_button("Reset", resetwatch, 200)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
