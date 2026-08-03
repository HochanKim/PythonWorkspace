# random 모듈 불러오기
from random import *

id_list = list(range(1, 21))
print(id_list)  # 1부터 20까지의 숫자를 담은 리스트 출력

shuffle(id_list)  # shuffle() 함수를 이용하여 리스트의 값을 무작위로 섞음
print(id_list)  # 무작위로 섞인 리스트 출력

print("-- 당첨자 발표 --")
print(
    "치킨 당첨자 : ", *(sample(id_list, 1))
)  # sample() 함수를 이용하여 리스트에서 1개의 값을 무작위로 추출, *를 이용하여 리스트의 값을 언패킹하여 출력
print(
    "커피 당첨자 : ", sample(id_list, 3)
)  # sample() 함수를 이용하여 리스트에서 3개의 값을 무작위로 추출
print("-- 축하합니다 --")
