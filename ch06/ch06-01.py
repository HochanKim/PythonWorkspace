# 조건문 - if-elif-else 구문
weather = input("오늘 날씨는 어때요? : ")

if weather == "비" or weather == "눈" or weather == "소나기":
    print("우산을 챙기세요")
elif weather == "미세먼지" or weather == "황사":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")
