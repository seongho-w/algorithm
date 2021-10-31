# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 버블 정렬을 이용해서 정렬하시오.
# 버블 정렬
# 버블 정렬은 첫 번째 자료와 두 번째 자료를, 두 번째 자료와 세 번째 자료를, 세 번째와 네 번째를, … 이런 식으로
# (마지막-1)번째 자료와 마지막 자료를 비교하여 교환하면서 자료를 정렬하는 방식

# # Swap 하는 방법
# #
# # 두 변수의 값을 교체 하려면 어떻게 할 수 있을까요?
# # a, b = b, a 라고 작성하시면 됩니다!

# Q. 여기서 퀴즈, 이 함수의 시간 복잡도는 얼마나 걸릴까요?
# 이것도 바로 O(N^2) 만큼 걸립니다. 함수 구문 하나하나를 보지 않더라도, 2차 반복문이 나왔고, array 의 길이 만큼 반복한다? 그러면 O(N^2) 이겠구나!
# 생각해주시면 됩니다. 다른 계수는 다 버려버리자구요~!

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

bubble_sort(input)
print(input)