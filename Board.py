__author__ = 'Mihoc Alex'
from Tkinter import *
import time
import random

window = Tk()
window.title("Lee's Algorithm - Pathfinding in a matrix - BFS INSPIRED")

size = input('Size of matrix:')
Walls = [(1, 2), (1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
rows = size
cols = size
player = (0,0)
end = (cols-2,rows-2)

for i in range(cols):
    for j in range(1,rows):
        if random.randint(0,9)<3:
            if (i != end[0]) and (j != end[1]):
                Walls.append((i,j))


Width = 700/rows


platform = Canvas(window, width = cols*Width, height = rows*Width)
platform.pack()

def render_grid():
    global rows, cols, Width, player, end
    for i in range(cols):
        for j in range(rows):
            platform.create_rectangle(i*Width, j*Width,(i+1)*Width, (j+1)*Width, fill="green", width = 1)

    platform.create_rectangle(player[0]*Width, player[1]*Width,(player[0]+1)*Width, (player[1]+1)*Width, fill="blue", width = 1)
    platform.create_rectangle(end[0]*Width, end[1]*Width,(end[0]+1)*Width, (end[1]+1)*Width, fill="yellow", width = 1)

    for (i,j) in Walls:
        platform.create_rectangle(i*Width, j*Width,(i+1)*Width, (j+1)*Width, fill="red", width = 1)

render_grid()

def render_path(path):
    global Width
    for (i,j) in path:
        platform.create_rectangle(i*Width, j*Width,(i+1)*Width, (j+1)*Width, fill="purple", width = 1)
        time.sleep(0.1)

def render_block(block, color):
    global Width
    platform.create_rectangle(block[0]*Width, block[1]*Width,(block[0]+1)*Width, (block[1]+1)*Width, fill=color, width = 1)


def start_game():
    window.mainloop()
