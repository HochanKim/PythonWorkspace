# 지하철 칸별로 10명, 20명, 30명 승차
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway)

subway = ["푸", "피글렛", "티거"]
print(subway)

print(subway.index("피글렛"))

print("====================================")

# append(다음 인덱스에 추가할 값)
subway.append("아요르")
print(subway)

# insert(인덱스, 삽입할 값)
subway.insert(1, "루")
print(subway)

print("====================================")

# 지하철 역마다 한 명씩 내림
print(subway.pop()) # 이요르 내림
print(subway)

print(subway.pop()) # 티거 내림
print(subway)

print(subway.pop()) # 피글렛 내림
print(subway)

print("====================================")

# 지하철에서 모두 내림
subway.clear()
print(subway)

print("====================================")

# 같은 이름이 몇 명 있는지 확인
subway = ["푸", "피글렛", "티거", 3]
subway.append("시진핑") # 푸 추가
subway.append("티거") # 푸 추가
print(subway)
print(subway.count("티거"))