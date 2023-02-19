N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]

minus_sum=0
zero_sum=0
plus_sum=0

def paper(x,y,n):
    global minus_sum, zero_sum, plus_sum
    first=board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != first:
                for k in range(3):
                    for m in range(3):
                        paper(x+k*n//3,y+m*n//3,n//3)
                return 

    if first==-1:
        minus_sum+=1
    elif first==0:    
        zero_sum+=1
    elif first==1:
        plus_sum+=1




paper(0,0,N)
print(f'{minus_sum}\n{zero_sum}\n{plus_sum}\n')


"""
#다른예시
import sys
input = sys.stdin.readline

n = int(input())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

papers = []
for _ in range(n):
    row = list(map(int, input().rsplit()))
    papers.append(row)


def check(row, col, n):
    global minus_cnt, zero_cnt, plus_cnt
    curr = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n)  # 1
                check(row, col + next_n, next_n)  # 2
                check(row, col + (2 * next_n), next_n)  # 3
                check(row + next_n, col, next_n)  # 4
                check(row + next_n, col + next_n, next_n)  # 5
                check(row + next_n, col + (2 * next_n), next_n)  # 6
                check(row + (2 * next_n), col, next_n)  # 7
                check(row + (2 * next_n), col + next_n, next_n)  # 8
                check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
                return

    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1
    return


check(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
"""