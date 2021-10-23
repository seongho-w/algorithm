# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
#
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# a = input()
# b = input()


# a, b = map(int,input().split())
#
# c = list(map(int,str(b)))
#
# print(a)
# print(b)
#
# d = (int(a)) * c[0]
# f = (int(a)) * c[2]
# e = (int(a)) * c[1]
#
# print(e)
# print(f)
# print(d)
#
# print(int(a)*int(b))

# 답안지
n1 = int(input())
n2 = str(input())

print(n1 * int(n2[2]))
print(n1 * int(n2[1]))
print(n1 * int(n2[0]))
print(n1 * int(n2))




