#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n=1
    k=13
    move_right()
    move_down()
    for j in range(k):
        for i in range(n):
            fill_cell()
            move_right()
        move_left(n)
        move_down()
        n+=1

if __name__ == '__main__':
    run_tasks()
