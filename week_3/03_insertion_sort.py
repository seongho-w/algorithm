# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 삽입 정렬을 이용해서 정렬하시오.
# 삽입정렬
# 삽입 정렬은 전체에서 하나씩 올바른 위치에 "삽입" 하는 방식
# 삽입 정렬은 필요할 때만 위치를 변경하므로 더 효율적인 방식입니다!

# Q. 여기서 퀴즈, 이 함수의 시간 복잡도는 얼마나 걸릴까요?
# 이것도 바로 O(N^2) 만큼 걸립니다.

input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

insertion_sort(input)
print(input)