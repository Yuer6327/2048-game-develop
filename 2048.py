import random
# 初始化游戏面板
def init_board():
    board = [[0 for i in range(4)] for j in range(4)]
    for i in range(2):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while board[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        board[x][y] = 2
        return board
# 打印游戏面板
def print_board(board):
    for i in range(4):
        for j in range(4):
            print(board[i][j], end='\t')
        print()
# 合并相同数字
def merge(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
    return board
# 移动操作
def move(board, direction):
    if direction == 'a':
        for i in range(4):
            board[i] = [x for x in board[i] if x != 0] + [0] * board[i].count(0)
    elif direction == 'd':
        for i in range(4):
            board[i] = [0] * board[i].count(0) + [x for x in board[i] if x != 0][::-1]
    elif direction == 'w':
        for j in range(4):
            col = [board[i][j] for i in range(4)]
            col = [x for x in col if x != 0] + [0] * col.count(0)
            for i in range(4):
                board[i][j] = col[i]
    elif direction == 's':
        for j in range(4):
            col = [board[i][j] for i in range(4)][::-1]
            col = [0] * col.count(0) + [x for x in col if x != 0]
            for i in range(4):
                board[i][j] = col[3-i]
    return board
# 判断游戏是否结束
def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True
# 主函数
def main():
    board = init_board()
    print_board(board)
    while not is_game_over(board):
        direction = input('请输入移动方向（a/d/w/s）：')
        board = move(board, direction)
        board = merge(board)
        board = move(board, direction)
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        while board[x][y] != 0:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        board[x][y] = 2
        print_board(board)
    print('游戏结束！')
if __name__ == '__main__':
    main()