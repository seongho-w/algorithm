# 셀프넘버 = 셀프 넘버란 생성자 없이 존재하는 수
# 숫자 2는 1을 통해 만들어지고, 숫자 4는 2를 통해 만들어지기에 셀프 넘버가 아니다
# 10 이하의 수에서는 1, 3, 5, 7, 9가 대표적인 셀프 넘버

# 셀프넘버 X
# 1 +1 = 2, 2 +2 = 4, 12 +1+2, = 15, 57 +5+7 = 69, 123 +1+2+3 = 129, 8888 +8+8+8+8 = 8920


def d(num):
    return num + sum(map(int, str(num)))

num_list = []

for i in range(1, 10001):
    num_list.append(d(i))

for i in range(1, 10001):
    if i not in num_list:
        print(i)



