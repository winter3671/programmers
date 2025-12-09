'''
1. 문제 분석
cap개만큼의 택배상자를 한번에 트럭에 실을 수 있음
deliveries의 수는 물류센터데서 집에 배달시켜야 하는 상자 수
pickups의 수는 집에서 가지고 물류센터로 옮겨야 하는 상자 수
가능한 경우의 수 중 가장 짧은 거리를 출력

2. 풀이 방법 고안
역순으로 뒤에서부터 가능한 경우를 탐색해야 함
멀리 갔다 오면서 택배를 배달하고, 택배상자를 픽업해 올 수 있기 때문

deliveries의 역순으로부터, 택배를 싣는 양이 정해짐
cap = 4, deliveries = {1, 0, 3, 0, 3}, pickups = {0, 0, 0, 0, 0}에서는 택배를 4개 가져오면 됨!
택배는 항상 최대치로 가져온다
deliveries = {1, 0, 5, 0, 3}, pickups = {0, 0, 0, 4, 0}이면?
물류센터에서 택배를 3개만 가지고와야 4번째 집까지 처리 가능

아니다. 택배를 4개 가지고와서, 3번째집에 1개를 미리 놔두고, 5번째 집에 3개를 배달하면 됨
이걸 어떻게 구현할 것인가?
택배를 항상 최대치로 가져온다라고 하면, deliveries에서 뒤에서부터 최대치의 택배를 모두 배달함(0, 0, 1, 0, 3)
truck = 4
deliveries[4]으로 truck = 1
pickups[3]으로 truck = 5
truck > cap이므로, deliveries[3], deliveries[2]를 탐색해 truck - cap만큼을 차감
'''

def solution(cap, n, deliveries, pickups):
    cnt = 0

    # n을 줄여가며 탐색범위 설정(뒤에서부터 0이 아닌 지점 탐색)
    while n > 0 and deliveries[n - 1] == 0 and pickups[n - 1] == 0:
        n -= 1

    while n > 0:
        cnt += n * 2    # n만큼 왕복하기 때문에 cnt에 2번 더해줌
        truck = cap

        for i in range(n-1, -1, -1):
            if truck == 0:
                break

            if deliveries[i] != 0:      # 뒤에서부터 truck에 있는 화물을 차례로 적재
                if deliveries[i] - truck >= 0:
                    deliveries[i] -= truck
                    truck = 0

                else:
                    truck -= deliveries[i]
                    deliveries[i] = 0

        truck = 0
        for i in range(n-1, -1, -1):
            if truck == cap:
                break

            if pickups[i] != 0:     # 뒤에서부터 truck에 cap만큼 화물상자가 찰때까지 수거
                gap = cap - truck

                if pickups[i] - gap >= 0:
                    truck += gap
                    pickups[i] -= gap
                else:
                    truck += pickups[i]
                    pickups[i] = 0

        while n > 0 and deliveries[n - 1] == 0 and pickups[n - 1] == 0:
            n -= 1

    return cnt

# cap = 2
# n = 7
# deliveries = [1, 0, 2, 0, 1, 0, 2]
# pickups = [0, 2, 0, 1, 0, 2, 0]
#
# result = solution(cap, n, deliveries, pickups)
# print(result)