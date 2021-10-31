# 회문 검사
# 회문은 똑바로 읽으나 거꾸로 읽으나 똑같은 단어나 문장을 의미

# Q. 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.

# 문자열을 돌면서
# 맨 앞의 문자와 맨 뒤의 문자,
# 맨 앞에서 두번째 문자와 맨 뒤에서 두번째 문자
# ...
# 를 비교하시면 됩니다!

# 문자열 슬라이싱
# 파이썬에서 문자열 자르는 방법은 되게 간단하고, 다양합니다!
#
# 그 방법들에 대해 설명 드리겠습니다.
# 참고로 slice 는 자르다라는 의미가 있습니다.
#
# 예를 들어서, "가나다라마바사" 라는 문자열에서
# "가나다라마" 까지 자르고 싶으면 어떻게 해야 할까요?
#
# 문자열[시작인덱스:끝인덱스] 로 표기하면 됩니다!

input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - i - 1]:
            return False
    return True


print(is_palindrome(input))