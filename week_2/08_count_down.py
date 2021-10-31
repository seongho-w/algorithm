# 재귀(Recursion)은 어떠한 것을 정의할 때 자기 자신을 참조하는 것
# 재귀 함수는 바로 자기 자신을 호출하는 함수

# Q. 60에서 0까지 숫자를 출력하시오.


def count_down(number):
    if number < 0:
        return
    print(number)
    # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(3)