#  재귀
# 팩토리얼
# 재귀함수와 관련되어 나오는 대표적인 문제인 팩토리얼! 에 대해서 배워보겠습니다.
#
# 팩토리얼은 1부터 어떤 양의 정수 n까지의 정수를 모두 곱한 것을 의미합니다.
#
# 예를 들면 아래와 같습니다!
# 3! 은 3 * 2 * 1 = 6,
# 4! 는 4 * 3 * 2 * 1 = 4 * 3! = 24

# Factorial(n) = n * Factorial(n - 1)
# Factorial(n - 1) = (n - 1) * Factorial(n - 2)
# ....
# Factorial(1) = 1


# 5 * factorial(4)
# 5 * 4 factorial(3)


# 5 * 4 * 3 * 2 * 1


def factorial(n): # 5
    if n == 1:      # 5 == 1 X
        return 1
    return n * factorial(n - 1)  # 5 * factorial(4)


print(factorial(5))