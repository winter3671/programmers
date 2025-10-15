'''
1. 문제 해석
격자는 N * N 크기
인형을 뽑게되면, 각 줄의 맨 위의 칸이 0으로 바뀌고, 숫자는 다른 리스트에 저장됨
뽑은 인형이 저장되는 리스트에서, 2개의 인형이 같은 숫자라면 둘다 없어지고, answer += 2

2. 유의사항
인형을 뽑는 과정에서 각 줄의 맨 위칸이 0으로 바뀌는 것을 쉽게하려면 zip과 언패킹을 사용해 배열을 세로로 바꾸는것이 편할것 같음
'''

def solution(board, moves):
    new_board = list(map(list, zip(*board)))  # 각 세로줄당 리스트로 바꾼 형태
                                              # map을 사용하지 않으니 tuple형태로 나와서, map으로 각 요소에 list()을 적용해줌
    answer = 0
    busket = []
    for move in moves:
        for i in range(len(new_board)):
            if new_board[move-1][i] != 0:
                if busket:      # busket에 하나 이상의 숫자가 있으면
                    if busket[-1] == new_board[move-1][i]:      # busket의 마지막 수와 뽑은 인형의 수가 같으면
                        busket.pop()        # busket의 마지막 수를 제거
                        answer += 2         # busket의 마지막 수, 뽑은 인형 총 2개
                    else:
                        busket.append(new_board[move-1][i])     # busket에 인형의 수를 추가
                else:       # busket이 빈 리스트라면
                    busket.append(new_board[move-1][i])
                new_board[move-1][i] = 0
                break

    return answer