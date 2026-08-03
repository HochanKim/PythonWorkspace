# continue와 break 예시
absent = [2, 5]  # 결석한 학생 번호
no_book = [7]  # 책을 깜빡한 학생 번호

for student in range(1, 11):  # 1부터 10까지 학생 번호 생성
    if student in absent:  # 결석한 학생이면
        continue  # 다음 반복으로 넘어감
    # elif student in no_book:  # 책을 깜빡한 학생이면
    #     print("오늘 수업 여기까지. {0}번 학생은 교무실로 따라와".format(student))
    #     break  # 반복문 종료
    print("{0}번 학생, 출석 체크".format(student))  # 출석 체크
