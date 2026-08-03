# 반복문 - for문
# for waiting_no in [1, 2, 3, 4, 5]:
#     print("대기번호 : {0}".format(waiting_no))  # {0} 위치에 waiting_no 값이 들어감

# range() 함수 이용
# for i in range(1, 11):  # 1부터 10까지 숫자를 생성
#     print("대기번호 : {0}".format(i))

# 반복문 - while문
customer = "토르"  # 손님 닉네임
index = 5  # 최대 호출 횟수

while index >= 1:  # index가 1 이상일 때 반복
    print("{}님, 커피가 준비됐습니다. ".format(customer))
    index -= 1  # index를 1씩 감소
    print("{}번 남았어요. ".format(index))
    if index == 0:
        print("커피는 폐기처분되었습니다. ")
