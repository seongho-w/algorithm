# 팩토리얼
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

def fact(num):
    if num ==0:
        return 1
    return num * fact(num - 1)

n = int(input())
print(fact(n))