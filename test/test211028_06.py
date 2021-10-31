# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

a = int(input())

b = []

for r in range(1,a+1):
    b.append(int(r))

b.reverse()
for k in b:
    print(k)
