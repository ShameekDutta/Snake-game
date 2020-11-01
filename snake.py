import curses
from random import randint

curses.initscr()
curses.noecho()
curses.curs_set(0)
win = curses.newwin(20,60,0,0)
win.keypad(1)
win.border(0)
win.nodelay(1)

snake=[(4,10),(4,9),(4,8)]
food=(randint(7,18),randint(13,58))
bonus=()
ESC=27
key=curses.KEY_RIGHT
score=0
b=0
lifes=5
win.addch(food[0],food[1],"o")
while key!=ESC:
    win.addstr(0,2,"score "+str(score)+" ")
    win.addstr(0,48,"Bonus "+str(b)+" ")
    win.addstr(0,23,"Lifes "+str(lifes)+" ")
    win.timeout(100)
    prev_key = key
    event=win.getch()
    key=event if event!= -1 else prev_key 
    if key not in [curses.KEY_RIGHT,curses.KEY_LEFT,curses.KEY_UP,curses.KEY_DOWN,ESC]:
        key=prev_key
    #calculate next coordinate
    y=snake[0][0]
    x=snake[0][1]
    if key==curses.KEY_DOWN:
        y+=1
    if key==curses.KEY_UP:
        y-=1
    if key==curses.KEY_LEFT:
        x-=1
    if key==curses.KEY_RIGHT:
        x+=1
    snake.insert(0,(y,x))
    #checking for border
    if y==0: 
         y=18
        del snake[0]
        snake.insert(0,(y,x))
        lifes-=1
        if lifes==0: break
    if x==0: 
        x=58
        del snake[0]
        snake.insert(0,(y,x))
        lifes-=1
        if lifes==0: break
    if x==59: 
        x=2
        del snake[0]
        snake.insert(0,(y,x))
        lifes-=1
        if lifes==0: break
    if y==19: 
        y=2
        del snake[0]
        snake.insert(0,(y,x))
        lifes-=1
        if lifes==0: break

    #checking if snake runs over itself
    if snake[0] in snake[1:]: break
    
    #bonus
    if bonus==():
        z=randint(1,80)
        if z==5:
            while bonus==():
                bonus=(randint(1,18),randint(1,58))
                if bonus==food: bonus=()
                if bonus in snake: bonus=()
            win.addch(bonus[0],bonus[1],"@")

    if bonus!=():
        if snake[0]==bonus:
            score+=2
            bonus=()
            b+=1
            
    #check if snake has eaten the food
    if snake[0]==food:
        score+=1
        food=()
        while food==():
            food=(randint(1,18),randint(1,58))
            if food in snake:
                food=()
        win.addch(food[0],food[1],"o")
    else:
        #moving the snake
        last=snake.pop()
        win.addch(last[0],last[1]," ")
    win.addch(snake[0][0],snake[0][1],"*")

    

curses.endwin()
print(f"Score={score}")
print(f"Bonuses collected={b}")
