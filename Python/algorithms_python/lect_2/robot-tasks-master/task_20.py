#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    n=6
    move_right()
    for i in range(n):
        while wall_is_on_the_right()==False:
            fill_cell()
            move_right()
        else:
            move_down()
            move_left()
        while wall_is_on_the_left()==False:
            fill_cell()
            move_left()
        else:
            move_down()
            move_right()


if __name__ == '__main__':
    run_tasks()
