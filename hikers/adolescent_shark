from copy import deepcopy

# 4 x 4 크기의 정사각형에 존재하는 각 물고기의 번호와 방향 값을 담는 테이블
fish_array = [[None] * 4 for _ in range(4)]

for i in range(4):
    fish = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기 번호, 방향]을 저장
        # 단, 주어지는 방향은 1번부터 시작하기 때문에 1을 빼줌
        fish_array[i][j] = [fish[j * 2], fish[j * 2 + 1] - 1]

# 8가지 방향 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8

result = 0  # 최종결과

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None # 잡아 먹혔으면 -1이기 때문에 None 반환


# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None: # 물고기가 안 잡아 먹혔다면
            x, y = position[0], position[1]
            direction = array[x][y][1] # 해당 물고기가 향할 방향을 확인
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4: # 4 x 4 정사각형을 벗어나지 않고,
                    if not (nx == now_x and ny == now_y): # 가고자 하는 방향에 상어가 없다면
                        array[x][y][1] = direction # 방향이 전환 됐다면 해당 방향으로 초기화
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y] # 물고기끼리 자리 바꿈
                        break
                direction = turn_left(direction) # 정사각형을 벗어났거나 상어가 있었다면 방향 전환

# 상어를 이동시키는 함수
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1] # 상어가 향할 방향 확인
    # 현재의 방향으로 계속 이동시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y)) # 물고기가 있는 좌표를 반환
    return positions


# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(array, now_x, now_y, total):
    global result
    array = deepcopy(array)  # 리스트를 통째로 복사
    total += array[now_x][now_y][0]  # 현재 위치의 물고기 먹기

    array[now_x][now_y][0] = -1  # 물고기를 먹었으므로 번호 값을 -1로 변환

    move_all_fishes(array, now_x, now_y)  # 전체 물고기 이동시키기

    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 더 이상 물고기를 먹을 수 없다면
    if len(positions) == 0:
        result = max(result, total)  # 최댓값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(fish_array, 0, 0, 0)
print(result)
