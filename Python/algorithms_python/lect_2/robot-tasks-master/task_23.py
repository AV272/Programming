#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    k=1
    if wall_is_on_the_right():
        return 0;
    move_right()
    while wall_is_on_the_right()==False:
        if wall_is_above()==False:
            n=1
            move_up()
            fill_cell()
            while wall_is_above()==False:
                move_up()
                fill_cell()
                n+=1
            move_down(n)
                
        move_right()
        k+=1
    else:
        if wall_is_above()==False:
            n=1
            move_up()
            fill_cell()
            while wall_is_above()==False:
                move_up()
                fill_cell()
                n+=1
            move_down(n)
    
    move_left(k)


if __name__ == '__main__':
    run_tasks()
