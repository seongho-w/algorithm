# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)


# 그리디 알고리즘은 동적 프로그래밍 사용 시 지나치게 많은 일을 한다는 것에서 착안하여 고안된 알고리즘


n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
result = 0

coins = coins[::-1]	# 내림차순으로 정렬
for i in range(n):
    if k // coins[i] > 0:	# 나눌 수 있다면
        result += k // coins[i]	# 나누어 발생한 몫 즉, 동전 갯수
        k = k % coins[i]	# 나머지를 다시 for문으로 계속 나눈다
print(result)


