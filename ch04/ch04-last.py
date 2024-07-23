url = "https://naver.com"
my_pwd = url.replace("https://", "")    # 문자열 변수 url의 문자 "https://"를 빈값("")으로 대체
my_pwd = my_pwd[0:5]    # 새 변수 my_pwd의 문자 슬라이싱, 0번째부터 4번째 인덱스를 제외한 나머지 인덱스 제거(".com")
password = my_pwd[:3] + str(len(my_pwd)) + str(url.count("e"))+ '!'     # 새 변수 password
# 변수 my_pwd에서 0~2번째 인덱스 슬라이싱(문자열) + my_pwd의 문자열 수(정수) + 변수 url의 문자열 'e'의 개수(정수) + 문자열 "!"
print("{}의 비밀번호는 {}입니다." .format(url, password))
print(url+"의 비밀번호는 "+password+"입니다.")
print()

var = "https://google.com"
goo_url = var.replace("https://", "")   # 빈값으로 대체(replace)
goo_url = goo_url[:6]   # 0~5번째 문자열 남기고 나머지 문자열은 슬라이싱 적용
password = goo_url[:3] + str(len(goo_url)) + str(goo_url.count('o')) + "!"
print(var+"의 비밀번호는 "+password+"입니다.")