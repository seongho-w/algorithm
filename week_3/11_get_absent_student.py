# 해쉬
# Q. 오늘 수업에 많은 학생들이 참여했습니다. 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다.
#
# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때, 출석하지 않은 학생의 이름을 반환하시오.

# Q. 여기서 퀴즈, 이 함수의 시간 복잡도는 얼마나 걸릴까요?
# 바로 O(N) 만큼 걸립니다.
# all_array 의 길이를 N 이라고 하면, 반복문은 몇 개 안 되니까요!
#
# 대신, 공간 복잡도도 O(N) 만큼 걸립니다.
# 모든 학생들을 다 해쉬 테이블 내에 저장할테니까요!
#
# 이처럼, 해쉬 테이블은 시간은 빠르되
# 공간을 대신 사용하는 자료구조라고 생각하시면 됩니다.



all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    dict = {}
    for key in all_array:
        dict[key] = True  # 아무 값이나 넣어도 상관 없습니다! 여기서는 키가 중요한거니까요

    for key in present_array:  # dict에서 key 를 하나씩 없앱니다
        del dict[key]

    for key in dict.keys():  # key 중에 하나를 바로 반환합니다! 한 명 밖에 없으니 이렇게 해도 괜찮습니다.
        return key


print(get_absent_student(all_students, present_students))