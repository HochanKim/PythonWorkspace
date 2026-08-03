# 세트명 = {값1, 값2, ...}
my_set = {1, 2, 3, 3, 3}
print(my_set)  # 중복을 허용하지 않으므로 값은 값은 여러 번 넣어도 실제로는 한 번만 저장

other_set = {1, 2, 3, 3, 3, 2, 4, 1, 5}
print(other_set)
print()

# 인원 관리 (세트)
java = {"푸", "피글렛", "티거"}  # 자바 개발자 세트, 중괄호를 활용한 세트 정의
python = set(["푸", "이요르"])  # 파이썬 개발자 세트, set() 함수를 이용하여 세트 생성
print(java)
print(python)
print()

# 교집합(두 세트에 모두 포함된 값)
print(java & python)  # & 연산자를 이용한 교집합
print(java.intersection(python))  # intersection() 함수를 이용한 교집합
print()

# 합집합(두 세트 중 하나에 포함된 값)
print(java | python)  # | 연산자를 이용한 합집합
print(java.union(python))  # union() 함수를 이용한 합집합
print()

# 차집합(한 세트에는 포함되지만 다른 세트에는 포함되지 않은 값)
print(java - python)  # - 연산자를 이용한 차집합
print(java.difference(python))  # difference() 함수를 이용한 차집합
print()

# 세트에 값 추가 (파이썬 개발자 세트에 값 추가)
python.add("피글렛")  # add() 함수를 이용한 값 추가
print(python)  # 기존 파이썬 가능 개발자: 푸, 이요르
print()

# 세트에 값 제거 (자바 개발자 세트에서 값 제거)
java.remove("피글렛")  # remove() 함수를 이용한 값 제거
print(java)  # 기존 자바 가능 개발자: 푸, 피글렛, 티거
