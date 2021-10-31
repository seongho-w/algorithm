# input = [3, 5, 6, 1, 2, 4]
#
#
# def find_max_num(input):
#     # 이 부분을 채워보세요!
#
#
#     for x in input:
#         # 3  < 3 , 5 브레이크
#         # 5  < 3 , 5 , 6 브레이크
#         # 6  < 3
#         # 1  < 3
#         # 2  < 3
#         # 4  < 3
#
#         for v in input:
#             if x < v :
#                 break
#         else:
#             return x
#
#
# #         for else문 for문이 다 끝날때까지 브레이크가 안나왔다면 실행
#
#
#
# result = find_max_num(input)
# print(result)




input = [3, 5, 6, 1, 2, 4]


def find_max_num(intput):
    # 이 부분을 채워보세요!

    a = input[0]

    for x in input:
        if x > a:
            a = x
    return a


result = find_max_num(input)
print(result)