#  Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

# 무작위로 정렬되어 있는 배열에서는 이진 탐색을 사용할 수 없습니다!
#
# 이진 탐색이 가능했던 이유는 한 방향으로 정렬되어 있었기 때문입니다.
#
# 즉, 일정한 규칙으로 정렬되어 있는 데이터일때만 이진 탐색이 가능합니다.

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    return 1


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)