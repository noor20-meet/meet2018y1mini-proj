
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random

turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.setup(1000, 1000)
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 1
count=0

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()
border=turtle.clone()
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
title=turtle.clone()
SNAKE_GAME=turtle.clone()

SNAKE_GAME.penup()
SNAKE_GAME.goto(0,300)
SNAKE_GAME.write("SNAKE GAME!", True, align="center", font=("Times New Roman",30,"normal"))

border.pensize(5)
border.goto(-410,267)
border.pendown()
border.goto(410,267)
border.goto(410,-267)
border.goto(-410,-267)
border.goto(-410,267)


for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1] 

    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) 
    snake.goto(x_pos,y_pos) 
   
    pos_list.append(my_pos) 


    stamp_ID= snake.stamp()
    stamp_list.append(stamp_ID)

TIME_STEP = 400
SPACEBAR = "space" 

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction
    direction=UP 
    print("You pressed the up key!")

def down():
    global direction
    direction = DOWN
    print("You pressed the down key!")

def left():
    global direction
    direction = LEFT
    print("You pressed the left key!")

def right():
    global direction
    direction = RIGHT
    print("You pressed the right key!")
    

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.listen()


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+5
    max_x=int(SIZE_X/2/SQUARE_SIZE)-5
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+5
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-5
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())

def move_snake():
    global TIME_STEP,count
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
        
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    
    if new_x_pos>= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos<= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
    elif new_y_pos>= UP_EDGE:
        print("You it the upper edge! Game over!")
        quit()
    elif new_y_pos<= DOWN_EDGE:
        print("You hit the lower edge! Game over!")
        quit()

    if new_pos in pos_list:
        print("You can't eat yourself!")
        quit()
    else:
        my_pos=snake.pos() 
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
    
    global food_stamps, food_pos
    
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_ind])                             
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("om nom nom")
        make_food()
        TIME_STEP-=9
        print(TIME_STEP)
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

   
                
    title.goto(0,-300)
    title.clear()
    title.write("score: "+str(len(stamp_list)), True, align="center",font=("Times New Roman",20,"normal"))
    turtle.ontimer(move_snake,TIME_STEP)

    count+=1
    color_list=["pink","cyan","blue","yellow","orange","red"]
    snake.color(color_list[count%6])
move_snake()

food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
 
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    stamp1=food.stamp()
    food_stamps.append(stamp1)



    
turtle.mainloop()
