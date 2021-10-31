# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 선택 정렬을 이용해서 정렬하시오.
# 선택 정렬 : 선택! 해서 정렬한다!

# Q. 여기서 퀴즈, 이 함수의 시간 복잡도는 얼마나 걸릴까요?
# 이것도 바로 O(N^2) 만큼 걸립니다. 함수 구문 하나하나를 보지 않더라도, 2차 반복문이 나왔고,
# array 의 길이 만큼 반복한다? 그러면 O(N^2) 이겠구나! 생각해주시면 됩니다. 다른 계수는 다 버려버리자구요~


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