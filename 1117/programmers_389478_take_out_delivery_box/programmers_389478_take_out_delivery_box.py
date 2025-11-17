'''
1. 문제 분석
상자를 뱀 모양으로 좌우 반복으로 쌓음
그중 한개의 상자를 꺼낼때, 위에 몇개의 상자가 놓여있는지 + 1을 구하시오

2. 풀이 방법 고안
직접 만들 필요 x
n을 w로 나눈 몫과 나머지를 구하고, 몫이 홀수인지, 짝수인지를 구함
몫이 홀수이면, 남은 상자들은 오른쪽부터 쌓여있을것
몫이 짝수이면, 남은 상자들은 왼쪽부터 쌓여있을것
상자의 층수는 num // w + 1층
위에 있는 상자의 개수는 몫 - 상자의 층수 + 나머지에 따른 1 or 0
마지막으로 +1으로 마무리

너무 복잡하다....
[0] * w의 빈 리스트를 만들고, 각 층의 상자의 개수를 넣어서 간단하게 해보자
총 상자의 개수를 알고, 목표 상자의 idx 위치와 층수를 알면 구하기 쉽지 않을까
'''
# def solution(n, w, num):
#     Q = n // w
#     R = n % w
#     floar = (num-1) // w + 1
#     result = Q - floar
#
#     if (num // w) % 2 == 0:
#         idx = num % w  # 목표 상자의 idx(1부터 시작)
#     else:
#         idx = w - num % w + 1
#
#     if Q % 2 == 0:
#         all_idx = R
#         if all_idx >= idx:
#             result += 1
#     else:
#         all_idx = w - R + 1
#         if all_idx <= idx:
#             result += 1
#
#     result += 1
#
#     return result
#
def solution(n, w, num):
    boxes = [n // w] * w
    if (n // w) % 2 == 1:
        for i in range(n % w):
            boxes[-1-i] += 1
    else:
        for i in range(n % w):
            boxes[i] += 1

    floar = (num - 1) // w       # 목표 상자 아래에 있는 상자 수

    if ((num - 1) // w) % 2 == 1:
        box_idx = w - (num-1) % w - 1
    else:
        box_idx = (num-1) % w

    answer = boxes[box_idx] - floar
    return answer

n = 13
w = 3
num = 6
print(solution(n, w, num))

