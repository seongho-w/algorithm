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

# Q. 여기서 퀴즈, 이 함수의 시간 복잡도는 얼마나 걸릴까요?
# while 문이 len(array1) 과 len(array2)의 길이 만큼 반복하고 있습니다.
# 즉, 최대 len(array1) + len(array2) 만큼의 연산량이 필요한데,
# 이의 최댓값은 O(N) 입니다!
# 왜냐면 array1과 array2 는 결국 array 를 반으로 잘라서 넣은 길이이기 때문입니다!
#
# 그러면 merge 함수의 시간 복잡도는 O(N)
# merge_sort 는 대입 연산과 비교 연산 몇 번밖에 나오지 않으므로
# 상수의 시간 복잡도를 가집니다!
#
# 그러므로 병합 정렬의 총 시간복잡도는 O(N)이라고 말하면 될까요?
#  log_2N  번 반복하게 되면 1이 됩니다.
# 이걸 수식으로 나타내면
# N만큼의 연산을 logN 번 반복한다고 해서
#
# 시간 복잡도는 총 O(Nlog_2N) = O(NlogN) 이 된다! 라고 생각할 수 있습니다


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