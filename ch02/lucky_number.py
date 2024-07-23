import random   # random 모듈의 기능을 가져다 쓰겠다는 의미

lotto = []
rnd_num = random.randint(1, 45) # 1 이상 45 이하의 정수에서 난수 생성

for i in range(6) :
    while rnd_num in lotto :
        rnd_num = random.randint(1, 45)
    lotto.append(rnd_num)
    
lotto.sort()
print("로또번호 : {}".format(lotto))    # 로또번호 6자리 출력