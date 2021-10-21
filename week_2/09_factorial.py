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