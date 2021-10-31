# 최빈값 찾기
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

# 위의 문제에서 알파벳 빈도수 세기 작업 코드

# 문자인지 확인하는 방법 : 파이썬의 내장 함수 str.isalpha() 를 이용하면 해당 문자열이 알파벳인지 확인할 수 있습니다!
# 아스키 (ASCII) 코드를 사용해야 합니다. 컴퓨터는 0과 1 숫자 밖에 모르기 때문에 문자도 숫자로 기억
# 구글링 해보겠습니다! "python char to ascii code" 라고 검색하면, ord 함수를 사용하라고 나옵니다! 그러면 앞으로 ord 함수를 이용




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