#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    n=0
    check = False
    while wall_is_on_the_left()==False:
        if wall_is_above()==False:
            move_up()
            check = True
            break
        elif wall_is_beneath()==False:
            move_down()
            check = True
            break
        move_left()
        n+=1
    else:
        if wall_is_above()==False:
            move_up()
            check = True
        elif wall_is_beneath()==False:
            move_down()
            check = True
        
    if check==False:
        if n != 0:
            move_right(n)
        while wall_is_on_the_right()==False:
            if wall_is_above()==False:
                move_up()
                check = True
                break
            elif wall_is_beneath()==False:
                move_down()
                check = True
                break
            move_right()
        else:
            if wall_is_above()==False:
                move_up()
                check = True
            elif wall_is_beneath()==False:
                move_down()
                check = True
            
    while wall_is_on_the_left()==False:
        move_left()
    while wall_is_above()==False:
        move_up()


if __name__ == '__main__':
    run_tasks()
