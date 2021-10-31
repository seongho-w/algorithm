# 이진탐색 VS 순차탐색

# 답을 맞춰볼 수 있는 기회를 7번 드리는데 숫자의 범위는 1~100 입니다!
# 7번 안에 맞춰야 된다면, 여러분은 어떻게 맞추실 건가요?
#
# 내가 제일 좋아하는 숫자 21 을 시도한다?
# 아니면 강사의 생일이 9/3 이니까 93을 시도한다..?
# 인생은 차근차근 1부터 하나씩 천천히 맞춰본다..?


# Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다. 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min  <= current_max:
        if array[current_guess] == target:

            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)