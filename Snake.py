# This program can only work with codesulptor
import simplegui
import random

WIDTH= 400
HEIGHT = 400
DirectionList = ['up', 'down', 'left', 'right']
allPosition = []
for i in range(40):
    for j in range(40):
        allPosition.append((i, j))
        
"""Each block has a side length of 10 and takes one unit. So each side has 
40 units."""  

# to change the position coordinate into the display parameters
def toDrawPosition(position):
    return [(position[0]*10, position[1]*10), \
                         (position[0]*10+10, position[1]*10), \
                         (position[0]*10+10, position[1]*10+10), \
                         (position[0]*10, position[1]*10+10)]

# to generate the blocklist of snake in the beginning
def generateBlocks(direction):
    blockList = []
    if direction == 'left':
        for i in range(20, 23):
            blockList.append(Block((i, 20)))
    if direction == 'right':
        for i in range(23, 20, -1):
            blockList.append(Block((i, 20)))
    if direction == 'up':
        for i in range(20, 23):
            blockList.append(Block((20, i)))
    if direction == 'down':
        for i in range(23, 20, -1):
            blockList.append(Block((20, i)))
    return blockList

class Block(object):
    """position is a tuple with two parameters of x and y. drawPosition is for the
    drawing of the polygons. We use updatePosition to update the position of 
    different blocks"""
    
    #initiate the block with the position
    def __init__(self, position):
        self.position = position
        self.drawPosition = toDrawPosition(self.position)
    
    # return the position of the block
    def getPosition(self):
        return self.position
    
    #return the position for draw
    def getDrawPosition(self):
        return self.drawPosition
    
    #update the position of the block
    def updatePosition(self, newPosition):
        self.position = newPosition
        self.drawPosition = toDrawPosition(self.position)
        
class Candy(object):
    """generate candy in the canvas. The candies appears randomly in the canvas 
    except for the positions where there are the blocks of snake."""
    
    #initiate the candy
    def __init__(self, snake):
        checkStatus = True
        while checkStatus:
            checkStatus = False
            self.position = (random.randrange(0, 40), random.randrange(0, 40))
            for item in snake.getBlockList():
                if self.position == item.getPosition():
                    checkStatus = True
        self.drawPosition = toDrawPosition(self.position)
        
    #return the position of the candy   
    def getPosition(self):
        return self.position
    
    # return the draw parameter of the candy
    def getDrawPosition(self):
        return self.drawPosition
    
    
        
class Snake(object):
    """Snake is an object with all the blocks. blockList is a list including all
    the blocks. The snake will die when it hits the walls or it eats itself."""
    
    #initiate the snake with a list of blocks
    def __init__(self, blockList):
        self.blockList = blockList
        
    #return the blockList   
    def getBlockList(self):
        return self.blockList
    
    """The snake moves in the canvas. When it encounters a candy, the length of the 
    snake will grow with one unit, and return True. If it hits the walls or it eats
    itself, raise a exception."""
    def move(self, direction, candy):
        firstBlock = self.blockList[0]
        if direction == 'left':
            nextPosition = (firstBlock.getPosition()[0]-1, firstBlock.getPosition()[1])
        elif direction == 'right':
            nextPosition = (firstBlock.getPosition()[0]+1, firstBlock.getPosition()[1])
        elif direction == 'up':
            nextPosition = (firstBlock.getPosition()[0], firstBlock.getPosition()[1]-1)
        elif direction == 'down':
            nextPosition = (firstBlock.getPosition()[0], firstBlock.getPosition()[1]+1)
        currentBlockPosition = []
        for item in self.blockList:
            currentBlockPosition.append(item.getPosition())
        if (nextPosition in allPosition) and (not (nextPosition in currentBlockPosition)):
            if nextPosition == candy.getPosition():
                self.blockList.insert(0, Block(nextPosition))
                return True
            else:
                self.blockList.insert(0, Block(nextPosition))
                self.blockList.pop(-1)
                return False
        else:
            raise Exception
    
# To draw all the blocks, candies and words    
def draw(canvas):
    global snake, direction, candy, score
    for item in snake.getBlockList():
        canvas.draw_polygon(item.getDrawPosition(), 1, 'White', 'White')
    if end_status:
        canvas.draw_text('Game Over', (10, 200), 80, 'Red')
        canvas.draw_text('score earned: ' + str(score), (45, 250), 50, 'Red')
    canvas.draw_polygon(candy.getDrawPosition(), 1, 'White', 'White')

# move the snake
"""If the snake eats a candy, it accelerates and we create a new candd in a random place.
If it hits the walls, we turn the end_status into True, which creates the word "game over".
And we stop the timer at the same time."""
def timer_handler():
    global snake, direction, single_click, end_status, candy, timer, timerNumber, score
    try:
        if snake.move(direction, candy):
            candy = Candy(snake)
            score += 1
            if timerNumber < (len(timer) - 1):
                timer[timerNumber].stop()
                timerNumber += 1
                timer[timerNumber].start()
    except:
        end_status = True
        timer[timerNumber].stop()
    single_click = True
    
# use keyboard control to change the direction of move by obtain the input
"""we set that after each move, we get only input one change of direction.
After the first input after each move, the single_click will turn into False,
which makes sure the only the first input will be considered before the next move."""
def key_handler(key):
    global direction, single_click
    if key == simplegui.KEY_MAP['left'] and direction != 'right' and direction != 'left' and single_click:
        direction = 'left'
        single_click = False
    elif key == simplegui.KEY_MAP['right'] and direction != 'left' and direction != 'right' and single_click:
        direction = 'right'
        single_click = False
    elif key == simplegui.KEY_MAP['up'] and direction != 'down' and direction != 'up' and single_click:
        direction = 'up'
        single_click = False
    elif key == simplegui.KEY_MAP['down'] and direction != 'up' and direction != 'down' and single_click:
        direction = 'down'
        single_click = False
        
# to restart the game
def button_handler1():
    newgame()

#to make a pause
def button_handler2():
    global timer, timerNumber, end_status
    if not end_status:
        timer[timerNumber].stop()

#to continue after the pause
def button_handler3():
    global timer, timerNumber, end_status
    if not end_status:
        timer[timerNumber].start()
    
    
        

#start the game by initiating the snake with 3 blocks, a candy and random direction
def newgame():
    global snake, direction, single_click, end_status, candy, timer, timerNumber, score
    direction = random.choice(DirectionList)
    snake = Snake(generateBlocks(direction))
    single_click = True
    end_status = False
    candy = Candy(snake)
    timerNumber = 0
    timer[timerNumber].start()
    score = 0

    
frame = simplegui.create_frame('snake', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
"""initiate a list of timer with different timegap, so that we can accelerate the snake
by change the current timer into a timer with shorter timegap."""
timer = []
timegap = 500
while timegap > 30:
    timer.append(simplegui.create_timer(timegap, timer_handler))
    timegap *= 0.85
frame.set_keydown_handler(key_handler)
button1 = frame.add_button('Start', button_handler1, 200)
button2 = frame.add_button('Pause', button_handler2, 200)
button3 = frame.add_button('Continue', button_handler3, 200)

newgame()
frame.start()