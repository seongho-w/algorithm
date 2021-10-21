# str.isalpha() 를 이용하면 해당 문자열이 알파벳인지 확인
# continue 반복문의 다음 인덱스로 넘어가게 하는 방법
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

        # 이 부분을 채워보세요!
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))