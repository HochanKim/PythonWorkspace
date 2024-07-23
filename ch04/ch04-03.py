python = "Python is Amazing"

print(python.lower())             # print(문자열 or 변수, 함수()), 전체 소문자로 변환
print(python.upper())             # 전체 대문자로 변환
print(python[0].isupper())        # 인덱스 0에 있는 값이 대문자인지 확인
print(python[1:3].islower())      # 인덱스 1부터 2에 있는 값이 소문자인지 확인
print(python.replace("Python", "Java"))     # replace(a,b) : a 문자열을 b로 바꾸기, Python을 Java로 바꾸기
print()

find = python.find("n")     # 처음 발견한 n의 인덱스
print(find)     # 'Python'에서 n(인덱스 5)

find = python.find("n", find + 1)     # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(find)     # ' is Amazing'에서 n(인덱스 15)

find = python.find("Java")     # Java가 없으면 -1을 반환(출력)한 후 프로그램 계속 수행
print(find)
print()

index = python.index("n")   # 처음 발견한 n의 인덱스
print(index)    # 'Python'에서 n(인덱스 5)

index = python.index("n", index + 1)    # 인덱스 6 이후부터 찾아 처음 발견한 n의 인덱스
print(index)    # ' is Amazing'에서 n

index = python.index("n", 2, 6)    # 인덱스 2부터 6 직전까지 찾아 처음 발견한 n의 인덱스
print(index)    # 'thon'에서 n(인덱스 5)   

# index = python.index("Java")    # Java가 없으면 오류가 발생하며 프로그램 종료
# print(index)
print()

print(python.count("n"))
print(python.count("a"))
print(python.count("v"))
print()

print(len(python))