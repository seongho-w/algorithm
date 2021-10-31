# 최대값 찾기 - 두번째
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.



# 시간복잡도 : 입력값과 문제를 해결하는 데 걸리는 시간과의 상관관계를 말합니다! 입력값이 2배로 늘어났을 때 문제를 해결하는 데 걸리는 시간은 몇 배로 늘어나는지를 보는 것
# 1. max_num 대입 연산 1번
# 2. array의 길이 X (비교 연산 1번 + 대입 연산 1번)
# 이 함수는 2N+1 만큼의 시간

# 1.  N 과 N제곱은 N 이 커질수록 더 큰 차이가 나는구나!
# 2.  N의 지수를 먼저 비교하면 되겠구나.




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


