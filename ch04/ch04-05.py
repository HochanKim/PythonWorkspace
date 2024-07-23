print("백문이 불여일견\n백견이 불여일타")   # "\n" => 줄바꿈 탈출문자
print()

print("저는 '나도코딩'입니다.") # "" 문장 안에 ''
print('저는 "나도코딩"입니다.') # '' 문장 안에 ""
print('저는 \'나도코딩\'입니다.')   # 탈출문자 '\'를 사용하여 문장 안에 쓰여진 ''를 보존하여 출력
print("저는 \"나도코딩\"입니다.")   # 탈출문자 '\'를 사용하여 문장 안에 쓰여진 ""를 보존하여 출력
print()

# print("C:\Users\ghcks\Desktop\PythonWorkspace")
# 유효하지 않는 탈출문자 '\'의 사용으로 오류가 발생한다. 
# => 오류내용 : (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
print("C:\\Users\\ghcks\\Desktop\\PythonWorkspace") # 올바른 구문1, 역슬래시 2개를 사용하여 역슬래시가 포함된 문장을 출력
print(r"C:\Users\ghcks\Desktop\PythonWorkspace") # 올바른 구문2, 출력할 문장 앞에 'r'을 붙여 사용하면 정상적으로 출력
print()

print('Red Apple\rPine')    # 탈출문자 '\r' : 커서를 맨 앞으로 이동, 이동하는 과정에 맨 앞에 있는 기존 문자를 커버하는 효과가 보여진다 
print('Redd\bApple')    # 탈출문자 '\b' : 키보드의 백스페이스와 같은 역할, 앞 글자 하나를 삭제하는 기능
print('Red\tApple')    # 탈출문자 '\t' : Tab키와 같이 여러 칸을 띄어 쓰는 역할 (표시되는 터미널에서는 8칸 기준으로 띄어짐)