import random
import curses
import time
# 初始化curses
s = curses.initscr() # type: ignore
curses.curs_set(0) # type: ignore
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0) # type: ignore
w.keypad(1)
w.timeout(100)

# 初始化游戏板和游戏状态
score = 0
board = [[0 for x in range(4)] for y in range(4)]
board[random.randint(0, 3)][random.randint(0, 3)] = 2
game_over = False

# 定义游戏逻辑
def merge_left():
    global board, score
    for row in range(4):
        for col in range(3):
            if board[row][col] == board[row][col + 1] and board[row][col] != 0:
                board[row][col] *= 2
                score += board[row][col]
                board[row][col + 1] = 0

def merge_right():
    global board, score
    for row in range(4):
        for col in range(3, 0, -1):
            if board[row][col] == board[row][col - 1] and board[row][col] != 0:
                board[row][col] *= 2
                score += board[row][col]
                board[row][col - 1] = 0

def merge_up():
    global board, score
    for col in range(4):
        for row in range(3):
            if board[row][col] == board[row + 1][col] and board[row][col] != 0:
                board[row][col] *= 2
                score += board[row][col]
                board[row + 1][col] = 0

def merge_down():
    global board, score
    for col in range(4):
        for row in range(3, 0, -1):
            if board[row][col] == board[row - 1][col] and board[row][col] != 0:
                board[row][col] *= 2
                score += board[row][col]
                board[row - 1][col] = 0

def place_new_tile():
    global board
    row, col = random.randint(0, 3), random.randint(0, 3)
    while board[row][col] != 0:
        row, col = random.randint(0, 3), random.randint(0, 3)
    board[row][col] = 2

# 游戏主循环
while not game_over:
    
    # 绘制游戏板
    w.clear()
    w.addstr(0, 0, f"Score: {score}")
    for row in range(4):
        for col in range(4):
            w.addstr(row + 1, col * 5, f"{board[row][col]:5}")
        w.refresh()
    direction = input("w/a/s/d")
    if direction == 'a':
         merge_left()
#elif key == curses.KEY_F2:
    if direction == 'd':
        merge_right()
#elif key == curses.KEY_F3:
    if direction == 'w':
        merge_up()
    #elif key == curses.KEY_F4:
    if direction == 's':
        merge_down()
    w.refresh()
    place_new_tile()
# 检查游戏是否结束
    game_over = True
    for row in range(4):
        for col in range(4):
            time.sleep(5)
            #if board[row][col] == 0:
                #game_over = True
                #print('游戏结束！')
                #time.sleep(1)
            if row < 3 and board[row][col] == board[row+1][col] != 0:
                game_over = True
                print('游戏结束1！')
                time.sleep(1)
            if col < 3 and board[row][col] == board[row][col+1] != 0:
                game_over = True
                print('游戏结束2！')
                time.sleep(1)