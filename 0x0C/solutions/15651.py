# 중복허용 순열
#--- 입력 파트 ---#
N, M = map(int, input().split())

#--- 로직 파트 ---#
def permu(items):
    if len(items) == M:
        for item in items:
            print(item, end=" ")
        print()
    else:
        for i in range(N):
            item = i+1
            permu(items + [item])

#--- 출력 파트 ---#
permu([])