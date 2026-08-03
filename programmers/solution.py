def solution(num_list):
    num_list = [1, 3, 5, 7]
    even = 0
    odd = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]


print(solution(num_list=[1, 3, 5, 7]))
