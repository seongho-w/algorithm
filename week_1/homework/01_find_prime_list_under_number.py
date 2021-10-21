# input = 20
#
# # 소수는 자기 자신과 1외 에는 아무것도 나눌 수 없다.
# # 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# #  N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# # 수가 수를 나누면 몫이 발생하는데 몫과 나누는 수 둘중 하나는
# # 반드시 N의 제곱근 이하
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number +1 ):  #n 의 범위 2부터 number
#         for i in range(2, n): #i 의 범위는 2부터 n-1까지
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)


# input = 20
#
#
# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1):
#         for i in prime_list:
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
#
# result = find_prime_list_under_number(input)
# print(result)

input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)