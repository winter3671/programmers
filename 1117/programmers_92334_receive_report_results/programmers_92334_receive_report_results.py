'''
1. 문제 분석
한 유저가 여러명을 신고할 수 있지만, 한명을 여러번 신고한것은 1회 신고로 처리
k번 이상 신고된 유저는 게시판 이용이 정지. 그 유저를 신고한 사람들에게 정지 사실을 메일로 보냄
각 유저가 몇번 메일을 받았는지를 결과로 출력

2. 풀이 방법 고안
신고자와 피신고자의 정보를 모두 알고 있어야함
report의 두 이름을 split으로 나누어서 각각 받은 후, 피신고자의 idx에 맞게 신고자의 이름을 넣고, 길이를 측정

딕셔너리로 사용해도 되지 않을까?
defaultdict를 사용해서 key값이 피신고자, value값이 []인 딕셔너리를 만들고, 신고자의 이름을 value에 하나씩 추가하자

중복을 제거해야하므로 report를 set으로 바꾸어 중복 제거 후 실행한다
'''

def solution(id_list, report, k):
    from collections import defaultdict

    answer = [0] * len(id_list)
    report_dict = defaultdict(list)
    for name in id_list:
        report_dict[name]

    report = set(report)

    for names in report:
        user, reported_user = names.split(" ")
        report_dict[reported_user].append(user)

    for name in id_list:
        if len(report_dict[name]) >= k:
            for reporter in report_dict[name]:
                answer[id_list.index(reporter)] += 1

    return answer

    # return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))
