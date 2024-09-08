n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
# for i in range(n):
#     board.append(list(input()))
chess_board = [row[1:3] for row in board[0:2]]
print(chess_board)