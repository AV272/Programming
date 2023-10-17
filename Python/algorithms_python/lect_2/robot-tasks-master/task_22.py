#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    check = False
    while check==False:
        while wall_is_on_the_right()==False:
            fill_cell()
            move_right()
        else:
            fill_cell()
            if wall_is_beneath()==False:
                move_down()
            else:
                check = True
        if check:
            break
            
        while wall_is_on_the_left()==False:
            fill_cell()
            move_left()
        else:
            fill_cell()
            if wall_is_beneath()==False:
                move_down()
            else:
                check = True
        if check:
            break
    
    while wall_is_on_the_left()==False:
        move_left()



if __name__ == '__main__':
    run_tasks()
