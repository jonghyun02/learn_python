n,m = map(int,input().split())
board = []
for i in range(n):
    board.append(list(input()))
    
def chess_block_count_BW(chess_board, color):#color = 0은 맨 왼쪽 위 색깔 B, color = 1은 W
    count = 0
    BW = ['B','W']
    for i in range(0,8,2):
        for j in range(0,8,2):
            if chess_board[i][j] != BW[color]:
                count += 1
    for i in range(1,8,2):
        for j in range(1,8,2):
            if chess_board[i][j] != BW[color]:
                count += 1

    for i in range(0,8,2):
        for j in range(1,8,2):
            if chess_board[i][j] != BW[color-1]:
                count += 1
    for i in range(1,8,2):
        for j in range(0,8,2):
            if chess_board[i][j] != BW[color-1]:
                count += 1
    return count

min = n * m
for i in range(n-7):
    for j in range(m-7):
        chess_board = [row[j:j+8] for row in board[i:i+8]]
        tmp = 0
        if chess_block_count_BW(chess_board,0) < chess_block_count_BW(chess_board,1):
            tmp = chess_block_count_BW(chess_board,0)
        else:
            tmp = chess_block_count_BW(chess_board,1)
        if tmp < min:
            min = tmp
print(min)


#CHAT GPT가 개선해준 코드 : 반복문 하나로 통일, 변수에 값 담아서 함수 호출 최소화, 변수 개수 최소화.
n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

def chess_block_count_BW(chess_board, color):
    count = 0
    BW = ['B', 'W']
    for i in range(8):
        for j in range(8):
            expected_color = BW[(i + j + color) % 2]
            if chess_board[i][j] != expected_color:
                count += 1
    return count

# 최소 불일치 수를 큰 값으로 초기화
min_mismatch = n * m

# 보드의 모든 8x8 영역을 검사
for i in range(n - 7):
    for j in range(m - 7):
        # 현재 8x8 서브 보드를 슬라이싱
        chess_board = [row[j:j+8] for row in board[i:i+8]]
        
        # 색상 0 (B가 시작)과 색상 1 (W가 시작) 각각의 경우에 대해 계산
        count_B_start = chess_block_count_BW(chess_board, 0)
        count_W_start = chess_block_count_BW(chess_board, 1)
        
        # 최소값 갱신
        min_mismatch = min(min_mismatch, count_B_start, count_W_start)

print(min_mismatch)


#CHAT GPT 실제 코드 : 애초에 8x8 서브 보드를 생성할 필요 없이 그냥 board에서 시작 지점만 바꿔주면 되는거였다.
def count_changes(board, start_row, start_col, pattern):
    """Calculate the number of changes required to match the pattern in a 8x8 sub-board."""
    changes = 0
    for i in range(8):
        for j in range(8):
            expected_color = pattern[(i + j) % 2]
            if board[start_row + i][start_col + j] != expected_color:
                changes += 1
    return changes

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    board = [data[i + 2] for i in range(N)]
    
    pattern1 = ['W', 'B']
    pattern2 = ['B', 'W']
    
    min_changes = float('inf')
    
    for i in range(N - 7):
        for j in range(M - 7):
            changes_pattern1 = count_changes(board, i, j, pattern1)
            changes_pattern2 = count_changes(board, i, j, pattern2)
            min_changes = min(min_changes, changes_pattern1, changes_pattern2)
    
    print(min_changes)

if __name__ == "__main__":
    main()