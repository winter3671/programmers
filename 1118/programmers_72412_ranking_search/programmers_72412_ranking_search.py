'''
1. 문제 분석
조건을 만족하는 사람 중, x점 이상의 성적을 가진 사람의 수를 구하시오
info에는 "java backend junior pizza 150"와 같은 값들이 리스트에 들어있고,
query에는 "java and backend and junior and pizza 100"과 같은 값들이 리스트에 들어있음

2. 풀이 방법 고안
info의 값들은 " "를 기준으로 split하면 구분 가능
query의 값들은 어떻게 구분해야하는가?
4개의 문자들까지는 and로 연결되어있고, 마지막에는 숫자가 따로 들어가있음
-> " "으로 split하면 3개의 and를 포함해서 총 8개의 값이 나옴
and를 제외하면, 나머지 값들을 추출 가능

하다보니 2중 for문을 사용하게 되었는데, 이러면 시간초과가 남(50000 * 100000)

전체를 탐색하지 않고 조건을 만족하는 경우의 수를 구하는 방법이 있나?
누가 했는지는 상관없고, 몇명의 지원자가 조건을 만족하는지가 핵심!
지원이력의 가능한 모든 조합을 직접 만들고, 그 수를 먼저 넣고 시작해보자
가능한 조합의 수는 3 * 2 * 2 * 2 = 24
'''
# def solution(info, query):
#     result = [0] * len(query)
#     for req_idx in range(len(query)):
#         lang, and1, job, and2, exp, and3, food, score = query[req_idx].split(" ")
#         print(lang, job, exp, food, score)
#         if lang == '-':
#             lang = ['java', 'cpp', 'python']
#         if job == '-':
#             job = ['backend', 'frontend']
#         if exp == '-':
#             exp = ['junior', 'senior']
#         if food == '-':
#             food = ['chicken', 'pizza']
#
#         for applicant in info:
#             app_lang, app_job, app_exp, app_food, app_score = applicant.split(" ")
#             if app_lang not in lang:
#                 continue
#             if app_job not in job:
#                 continue
#             if app_exp not in exp:
#                 continue
#             if app_food not in food:
#                 continue
#             if int(app_score) < int(score):
#                 continue
#             result[req_idx] += 1
#
#     return result

def solution(info, query):
    def all_product(cases):
        all_cases = []
        for i in range(cases[0]):
            for j in range(cases[1]):
                for k in range(cases[2]):
                    for l in range(cases[3]):
                        all_cases.append((i, j, k, l))

        return all_cases

    requirement = [[] for _ in range(24)]
    lang = ['java', 'python', 'cpp']
    job = ['frontend', 'backend']
    exp = ['junior', 'senior']
    food = ['pizza', 'chicken']
    cases = (3, 2, 2, 2)
    num_of_cases = all_product(cases)
    for applicant in info:
        app_lang, app_job, app_exp, app_food, app_score = applicant.split(" ")

        for case_idx in range(len(num_of_cases)):
            if app_lang == lang[num_of_cases[case_idx][0]] and app_job == job[num_of_cases[case_idx][1]] and app_exp == exp[num_of_cases[case_idx][2]] and app_food == food[num_of_cases[case_idx][3]]:
                requirement[case_idx].append(app_score)

    result = [0] * len(query)
    for req_idx in range(len(query)):
        req_lang, and1, req_job, and2, req_exp, and3, req_food, req_score = query[req_idx].split(" ")
        for req in lang:
            if req_lang == req:
                idx_lang = [lang.index(req)]
        if req_lang == '-':
            idx_lang = [0, 1, 2]
        for req in job:
            if req_job == req:
                idx_job = [job.index(req)]
        if req_job == '-':
            idx_job = [0, 1]
        for req in exp:
            if req_exp == req:
                idx_exp = [exp.index(req)]
        if req_exp == '-':
            idx_exp = [0, 1]
        for req in food:
            if req_food == req:
                idx_food = [food.index(req)]
        if req_food == '-':
            idx_food = [0, 1]

        for i in idx_lang:
            for j in idx_job:
                for k in idx_exp:
                    for l in idx_food:
                        for score in requirement[num_of_cases.index((i, j, k, l))]:
                            if int(score) >= int(req_score):
                                result[req_idx] += 1

    return result


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))

