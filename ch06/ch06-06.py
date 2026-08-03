# 실습문제
# from random import *

# customers = range(1, 51)  # 1부터 50까지 손님 번호 생성
# drive_times = [randint(5, 50) for _ in customers]  # 5~50분 사이의 난수 생성
# choice = randint(0, 1)  # 0 또는 1 난수 생성
# i = 0  # 손님 매칭 횟수

# if choice == 0:
#     drive_times = "[]"  # 손님 매칭이 안됨
# else:
#     drive_times = "[0]"  # 손님 매칭이 됨
#     i += 1  # 손님 매칭 횟수 증가

# if drive_times:
#     for customer, drive_time in zip(customers, drive_times):
#         if choice == 1:
#             print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, drive_time))
#         else:
#             print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, drive_time))

# print("총 탑승객 : {0}명".format(i))  # 5~50분 사이의 손님 수 출력

from random import *  # 랜덤 모듈 호출

cstm = 0  # 탑승객 수

for num in range(1, 51):  # 1부터 50까지 반복(손님 순서 번호)
    time = randrange(5, 51)  # 5분 단위로 5분~50분 사이의 난수(랜덤) 생성
    if 5 <= time <= 15:  # 5~15분 사이에 손님이 매칭된 경우 (탑승 O)
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(num, time))
        cstm += 1  # 탑승객 수 증가
    elif 15 < time:  # 15분이 초과되어 손님이 매칭된 경우 (탑승 X)
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(num, time))
    else:
        break  # 5~50분 사이의 난수(랜덤) 생성이 아닌 경우 반복문 종료

print("총 탑승객 : {0}명".format(cstm))  # 총 탑승객 수 출력
