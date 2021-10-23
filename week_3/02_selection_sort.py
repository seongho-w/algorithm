# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 선택 정렬을 이용해서 정렬하시오.
# 선택 정렬

input = [4, 6, 2, 9, 1]

def selection_sort(array):
    n = len(array)
    # n = 5
    for i in range(n - 1):
        # 0~3
        min_index = i
        # 0
        for j in range(n - i):
            # 0        0~4
            if array[i + j] < array[min_index]:
                # 4 < 4 -> x
                # 6 < 4 -> x
                # 2 < 4 -> min _index = 0+2
                # 9 < 2 -> x
                # 1 < 2 -> min _index =


                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]
    return array


selection_sort(input)
print(input)