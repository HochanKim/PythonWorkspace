# 딕셔너리 → key와 value가 한 쌍으로 이루어진 각 값은 리스트와 마찬가지로 쉼표로 구분
empty_dict = {}
cabinet = {3: "푸", 100: "피글렛"}  # dic = {key: value}
print(cabinet[3])
print(cabinet[100])
print("=================")
print(cabinet.get(3)) # get()함수를 사용하여 해당 key의 value값을 가져오기
print("=================")
# print(cabinet[1]) => 오류로 바로 프로그램 종료
print(cabinet.get(1))   # get()함수로 없는 key를 불러오면 'None'
print()
print("=================")
print("=================")
cabinet = {"A-3": 'MSFT', "B-100": 'META'}
print(cabinet)
print()
print("=================")
# 값 변경/추가
cabinet["A-3"] = "NVDA"
cabinet["C-20"] = "GOOGL"
print(cabinet)
print()
print("=================")
# 딕셔너리는 'del'을 활용해 key에 할당된 value값을 삭제
del cabinet["B-100"]
print(cabinet)
