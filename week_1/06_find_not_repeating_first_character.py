# 반복되지 않는 문자

# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.


# 반복되는지 아닌지를 확인하기 위해서는, 각 알파벳 별로 출현하는 횟수를 저장해야 합니다. 그러면, 가장 많이 나온 알파벳 찾기 에서 사용했던 방법을 다시 사용하면 됩니다!
# alphabet_occurrence_array 배열에 각 빈도수를 저장하고, 그 배열을 돌면서 not_repeating_character_array 라는 배열에 반복되지 않는 문자를 다 집어넣습니다.
# 그리고 다시 한 번 문자열을 돌면서 해당 문자가 발견된다면 그 값을 반환하면 됩니다!
# 이 때, 1의 빈도수를 가진 인덱스를 알파벳으로 변환해서 not_repeating_character_array 에 저장하면 됩니다.
# 그러면 not_repeating_character_array 에는 ["c", "d"]가 담기게 되는데, 그 중 첫 번째인 "c" 를 반환하면 될까요? 그렇지 않습니다!
# 입력된 문자열 내에서 반복되지 않는 첫번째 문자를 찾아서 반환해줘야 하기 때문에 string 을 다시 반복해서 돌면서 첫 번째 반복되지 않는 문자를 찾아 반환해주시면 됩니다!
# 이를 이용해서 해결해봅시다!

# Q. 여기서 퀴즈, 이 함수의 시간 복잡도는 얼마나 걸릴까요?
# 이것도 바로 O(N) 만큼 걸립니다. 함수 구문 하나하나를 보지 않더라도, 1차 반복문이 나왔고, array 의 길이 만큼 반복한다?
# 그러면 O(N) 이겠구나! 생각해주시면 됩니다. 다른 계수는 다 버려버리자구요~!


input = "abadabac"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_character(input)
print(result)
