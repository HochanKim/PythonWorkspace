class_subjects = ["자료구조", "알고리즘", "운영체제", "자료구조"]
print(class_subjects)

# 중복 신청 방지를 위해 set()로 변환
class_subjects = set(class_subjects)
print(class_subjects)  # 중복이 제거된 세트 출력
