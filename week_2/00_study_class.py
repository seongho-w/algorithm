# [Array vs LinkedList]
# 1. Array : 특정원소 조회 O(1), 중간에 삽입 삭제 O(N),
# 데이터 추가 : 데이터 추가 시 모든 공간이 다 차버렸다면 새로운 메모리 공간을 할당받아야 한다, 정리 : 데이터에 접근하는 경우가 빈번하다면 Array를 사용하자
# 2. LinkedList : 특정원소 조회 O(N), 중간에 삽입 삭제 O(1),
# # 데이터 추가 : 모든 공간이 다 찼어도 맨 뒤의 노드만 동적으로 추가하면 된다., 정리 : 삽입과 삭제가 빈번하다면 LinkedList를 사용하는 것이 더 좋다

# 링크드 리스트
# 노드는 아래 두 가지 정보가 필요합니다.
# 1) 칸에 있는 데이터
# 2) 다음 칸이 뭔지


# Python 의 list 는 array 로 구현되어 있습니다!
# 내부적으로 동적 배열이라는 걸 사용해서, 배열의 길이가 늘어나도 O(1) 의 시간 복잡도가 걸리도록 설계했습니다!
# 파이썬의 배열은 링크드 리스트로 쓸 수도 있고,
# 배열로도 쓸 수 있게 만든 효율적인 자료구조다!

#  클래스 : 클래스는 분류. 집합. 같은 속성과 기능을 가진 객체를 총칭하는 개념
#  객체 : 객체는 세상에 존재하는 유일무이한 사물

# 클래스에는 생성자(Constructor)라는 게 있는데 객체를 생성할 때 데이터를 넣어주거나, 내부적으로 원하는 행동을 실행하게 할 수 있습니다!
# 파이썬에서 생성자 함수의 이름은 __init__ 으로 고정되어 있습니다!
# 무조건 생성자 이름의 함수는 __init__ 입니다!
# self가 뭐냐구요? self 는 객체 자기 자신을 가리킵니다!
# 클래스 내부의 함수는 메소드(method) 라고 부릅니다.
# talk 라는 메소드를 만들어 보면,
# 각 객체의 변수를 사용해서 메소드를 구현


#  클래스

class person:
    def __init__(self, param_name):
        print("i am created!",self)
        self.name = param_name

    def talk(self):
        print("안녕하세요, 제 이름은", self.name,"입니다")

    pass

person_1 =person("유재석")
print(person_1.name)
print(person_1)
person_1.talk()
person_2 =person("박명수")
print(person_2)
print(person_2.name)
person_2.talk()