# 이제부터는 면접에서 직접 구현해보라고 하는 구현 방법들입니다.
#
# 병합 정렬은 배열의 앞부분과 뒷부분의 두 그룹으로 나누어 각각 정렬한 후 병합하는 작업을 반복하는 알고리즘입니다.
#
# 예를 들어서
# A 라고 하는 배열이 1, 2, 3, 5 로 정렬되어 있고,
# B 라고 하는 배열이 4, 6, 7, 8 로 정렬되어 있다면
# 이 두 집합을 합쳐가면서 정렬하는 방법입니다.
#
# 우선, 이 두 집합을 어떻게 합쳐서 정렬할 수 있는지 예시로 보면서 이해해보겠습니다.

# 병합정렬 merge


array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge(array_a, array_b))