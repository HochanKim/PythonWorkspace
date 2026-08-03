# 자료구조 변환하기
menu = {"커피", "우유", "주스"}
print(menu)
print(type(menu))  # type() 함수를 이용하여 자료형 확인
print()

# 세트 -> 리스트로 변환
menu = list(menu)  # list() 함수를 이용하여 세트를 리스트로 변환
print(menu, type(menu))  # 변환된 자료형 확인
print()

# 리스트 -> 세트로 변환
menu = set(menu)  # set() 함수를 이용하여 리스트를 세트로 변환
print(menu, type(menu))  # 변환된 자료형 확인
print()

# 튜플로 변환
menu = tuple(menu)  # tuple() 함수를 이용하여 세트를 튜플로 변환
print(menu, type(menu))  # 변환된 자료형 확인
print()

my_list = [1, 2, 3, 3, 3]
my_set = set(
    my_list
)  # set() 함수를 이용하여 리스트를 세트로 변환, 여기서 중복된 값이 제거됨(set는 중복을 허용하지 않음)
my_list = list(my_set)  # list() 함수를 이용하여 세트를 리스트로 변환
print(my_list)  # 중복이 제거된 리스트 출력
