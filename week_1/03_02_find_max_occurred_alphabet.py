# 최빈값 찾기 - 두번째
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.


# 각 알파벳의 빈도수를 alphabet_occurrence_list 라는 변수에 저장합니다.
# 그리고 각 문자열을 돌면서 해당 문자가 알파벳인지 확인하고, 알파벳을 인덱스 화 시켜 각 알파벳의 빈도수를 업데이트 합니다.
# 이후, 알파벳의 빈도수가 가장 높은 인덱스를 찾습니다.

# "아스키 코드 번호"를 "실제 문자"로 변환하려면 chr() 함수를 사용

# 시간복잡도 : 입력값과 문제를 해결하는 데 걸리는 시간과의 상관관계를 말합니다! 입력값이 2배로 늘어났을 때 문제를 해결하는 데 걸리는 시간은 몇 배로 늘어나는지를 보는 것

# # 공간 복잡도 판단하기 : 입력값과 문제를 해결하는 데 걸리는 공간과의 상관관계를 말합니다! 입력값이 2배로 늘어났을 때 문제를 해결하는 데 걸리는 공간은 몇 배로 늘어나는지를 보는 것
# # 1. alphabet_array 의 길이 = 26
# # 2. arr_index, max_occurrence, max_alphabet_index, alphabet_occurrence 변수 = 4
# #  이제 이 함수는 30 만큼의 공간이 사용되었구나!


input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence ->3?
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    print(max_alphabet_index)
    return chr(max_alphabet_index + ord("a"))


        # 이 부분을 채워보세요!



result = find_max_occurred_alphabet(input)
print(result)