# 최빈값 찾기 - 첫번째
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

# 각 알파벳마다 문자열을 돌면서 몇 글자 나왔는지 확인합니다. 만약 그 숫자가 저장한 알파벳 빈도 수보다 크다면,
# 그 값을 저장하고 제일 큰 알파벳으로 저장합니다. 이 과정을 반복하다보면 가장 많이 나왔던 알파벳을 알 수 있습니다.

# 공간 복잡도 판단하기 : 입력값과 문제를 해결하는 데 걸리는 공간과의 상관관계를 말합니다! 입력값이 2배로 늘어났을 때 문제를 해결하는 데 걸리는 공간은 몇 배로 늘어나는지를 보는 것
# 1. alphabet_array 의 길이 = 26
# 2. max_occurrence, max_alphabet, occurrence 변수 = 3
#  이제 이 함수는 29 만큼의 공간이 사용되었구나!


input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_array = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet

    # 이 부분을 채워보세요!
    return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)