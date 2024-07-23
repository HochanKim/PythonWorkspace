number = 1 + 2 * 3  # 변수명 "number" 선언, 변수값 '1+2*3 = 7' 대입
print(number)   # 7
# ↓
number += 2 # 왼쪽 number에 2를 더한 후 왼쪽 number에 대입 / 'number = number + 2'와 동일 
print(number)   # 7 + 2 = 9
# ↓
number -= 2 # 왼쪽 number에 2를 뺀 후 왼쪽 number에 대입 / 'number = number - 2'와 동일 
print(number)   # 9 - 2 = 7
# ↓
number *= 2 # 왼쪽 number에 2를 곱한 후 왼쪽 number에 대입 / 'number = number * 2'와 동일 
print(number)   # 7 * 2 = 14
# ↓
number /= 2 # 왼쪽 number에 2를 나눈 후 왼쪽 number에 대입 / 'number = number / 2'와 동일 
print(number)   # 14 / 2 = 7 (7.0)
# ↓
number **= 2 # 왼쪽 number에 두 번 거듭제곱 후 왼쪽 number에 대입 / 'number = number ** 2'와 동일 
print(number)   # 7 ** 2 = 7 * 7 = 49 (7.0 ** 2 = 49.0)
# ↓
number //= 2 # 왼쪽 number에 2를 나눈 후의 몫을 왼쪽 number에 대입 / 'number = number // 2'와 동일 
print(number)   # 49 // 2 = '24' --- 1  (49.0 // 2 = '24.0' --- 1)
# ↓
number %= 2 # 왼쪽 number에 2를 나눈 후의 나머지값을 왼쪽 number에 대입 / 'number = number % 2'와 동일
print(number)   # 24 % 2 = 12 --- '0' (24.0 % 2 = 12.0 --- '0.0')