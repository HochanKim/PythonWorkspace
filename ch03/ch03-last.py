from random import *    # random 모듈의 모든 기능을 사용하겠다
offline = randint(4, 28)
# 변수 'offline' 선언, 정수형 변수값 'randint(4, 28)' 대입  
# 최소 일수인 28일까지 날짜를 선정 + 매월 1~3일은 스터디 준비기간으로 제외 (4일 ~ 28일 사이의 날짜 => 4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(offline) + "일로 선정됐습니다.")
# 정수형 변수값 'randint(4, 28)'이 대입된 변수명 'offline'을 str(문자형)으로 감싸서 형변환