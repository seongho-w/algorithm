input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num

    return max_num


# 배열 내에서 가장 큰 수를 찾아야 합니다. 그러면, 가장 큰 수를 저장할 변수를 만들고, 배열을 돌아가면서 그 변수와 비교합니다! 만약 값이 더 크다면, 그 변수에 대입해주면 됩니다!

result = find_max_num(input)
print(result)


