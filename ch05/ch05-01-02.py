# sorted()로 리스트 정렬하기
# 리스트를 정렬할 때 sorted() 함수도 사용할 수 있다.

my_list = [1, 3, 2, 0]
my_list.sort()  # 리스트 정렬 (순서대로 정렬)
print(my_list)  # 객체의 리스트 데이터 순서가 변경됨

print("====================================")

your_list = [7, 5, 4, 6]
new_list = sorted(your_list) # 정렬할 리스트를 소괄호 안에 넣음
print(your_list) # your_list 리스트 데이터는 변경되지 않음
print(new_list) # 정렬된 새로운 리스트