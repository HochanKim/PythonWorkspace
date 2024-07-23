sentence = "the early bird catches the worm."
KeunDae = sentence[0].upper() + sentence[1:]    # 0번째 인덱스 대문자 전환("upper()"), 나머지 문자열은 0번째 인덱스 슬라이싱 적용
print(KeunDae)
print()

sentence = "Actions Speak Louder Than Words."
ToLower = sentence.lower()  # 모든 문자열 소문자로 변환
KeunDae = sentence[0].upper() + ToLower[1:]    # 0번째 인덱스 대문자 전환("upper()"), ToLower 문자열은 0번째 인덱스 슬라이싱 적용후 이어붙이기
print(KeunDae)
print()

sentence = "PRACTICE MAKES PERFECT."
firstUpper = sentence[:1]   # 0번째 인덱스를 제외하고 나머지 슬라이싱 적용
AllLower = sentence.lower() # 변수 sentence 문자열들 소문자로 변환
KeunDae = firstUpper + AllLower[1:]    # 변수 firstUpper + 변수 AllLower 0번째 인덱스 슬라이싱 적용
print(KeunDae)
print()