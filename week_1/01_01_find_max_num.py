# 최대값 찾기 - 첫번째
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

# 시간복잡도 : 입력값과 문제를 해결하는 데 걸리는 시간과의 상관관계를 말합니다! 입력값이 2배로 늘어났을 때 문제를 해결하는 데 걸리는 시간은 몇 배로 늘어나는지를 보는 것
# array의 길이 X array의 길이 X 비교 연산 1번
# 만큼의 시간이 필요합니다. 여기서 array(입력값)의 길이는 보통 N이라고 표현합니다. 그러면 위의 시간을 다음과 같이 표현할 수 있습니다.
# N * N
# 그러면 우리는 이제 이 함수는 N제곱 만큼의 시간이 걸렸겠구나 라고 말할 수 있습니다.






input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)


