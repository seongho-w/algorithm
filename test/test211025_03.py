# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어,
# 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다.
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다.
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.


# 첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.

# a = int(input())
# num = []
# # num1 = []
# # num2 = []
#
#
#
# for n in range(1,4000):
#     if n % 4 == 0 and n % 100 != 0 or n % 400 ==0):
#         print('1')
#     else:
#         print('0')


# for r in range(1,4000):
#     if r % 100 == 0:
#         q = r
#         num1.append(q)
#         print(num1)
#
# for k in range(1,4000):
#     if k % 400 == 0:
#         s = k
#         num2.append(s)
#         print(num2)
#
# if a(int) == num and num2:
#     print(True)

# and != n % 100 ==0:


# for r in range(1,4000):
#     if r % 4 == 0:
#         r % 400 == 0
#
#         print(r)


n = int(input())

if ((n%4 == 0)and(n%100 != 0)) or (n%400 == 0):
    print('1')
else:
    print('0')