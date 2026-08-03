# input + while문
customer = "토르"
person = None  # 손님이 없을 때까지 반복

while person != customer:  # 손님이 토르가 아닐 때 반복
    print("{0}님, 커피가 준비됐습니다. ".format(customer))
    person = input("이름이 어떻게 되세요? ")  # 손님 이름 입력

    if person == customer:  # 손님이 토르일 때
        print("맛있게 드세요. ")
