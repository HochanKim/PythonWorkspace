name = "연탄이" # 변수 "name" 선언, 문자 변수값 "연탄이" 대입
animal = "개"   # "animal" 선언, 문자 변수값 "개" 대입
age = 4        # 변수 "age" 선언, 정수 변수값 "4" 대입
hobby = "산책"  # 변수 "hobby" 선언, 문자 변수값 "산책" 대입
adult = age >= 3    # 변수 "adult" 선언, 불리언 변수값 "age >= 3" 대입

print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 " + animal +"인데, 이름이 "+ name +"예요.")   # 종류, 이름
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요")    # 나이, 취미
# 'str()'은 값의 자료형을 문자열로 바꾸는 기능을 하는 명령어
# str => 'string'(문자열)의 줄임말
# '+'로 연결할때는 모든 자료형이 같아야 한다.
print(name + "는 어른일까요? " + str(adult))    # 나이, 취미

print("===================================================================")

name = "해피"
animal = "고양이"
age = 6
hobby = "낮잠"

print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 ", animal,"인데, 이름이", name,"에요.")
print(name, "는", age, "살이고,", hobby, "을 아주 좋아해요")
# ','로 연결할때는 형변환을 하지 않아도 되고 값과 값 사이에 빈칸을 포함한다.