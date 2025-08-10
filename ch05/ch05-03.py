# 튜플
# 튜플명 = (값1, 값2)
menu = ("돈가스", "치즈돈가스")
print(menu[0])
print(menu[1])
print("===========================")
name = "피글렛"
age = 20
hobby = "코딩"
print(name, age, hobby)
print("===========================")
print("== 튜플 형태로 한 줄에 여러 변수의 값을 정의 ==")
(name, age, hobby) = ("피글렛", 20, "코딩")
print(name, age, hobby)
print("===========================")
(dep, arr) = ("김포", "제주")
print(dep, ">", arr)
(dep, arr) = (arr, dep)
print(dep, ">", arr)