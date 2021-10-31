# 피보나치 수열
# 수학에서, 피보나치 수(영어: Fibonacci numbers)는 첫째 및 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열이다.
# 처음 여섯 항은 각각 1, 1, 2, 3, 5, 8이다. [위키백과]
# 즉, n번째 피보나치 수를 Fibo(n)라고 표현한다면,
# Fibo(1) 은 1이고,
# Fibo(2) 도 1입니다! (첫째 및 둘째 항을 1이라고 정했대요!)
#
# Fibo(3) 부터는 이전 값과 이전 이전 값의 합입니다!
# 즉, Fibo(3) = Fibo(1) + Fibo(2) = 1 + 1 = 2 입니다.
#
# 그러면
# Fibo(4) = Fibo(3) + Fibo(2) = 2 + 1 = 3
# Fibo(5) = Fibo(4) + Fibo(3) = 3 + 2 = 5
# Fibo(6) = Fibo(5) + Fibo(4) = 5 + 3 = 8 .....
# Fibo(n) = Fibo(n - 1) + Fibo(n-2) 라고 표현할 수 있습니다!



# Q. 피보나치 수열의 20번째 수를 구하시오.


input = 20


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765