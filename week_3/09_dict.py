# 해쉬
# 컴퓨팅에서 키를 값에 매핑할 수 있는 구조인, 연관 배열 추가에 사용되는 자료 구조이다.
# 해시 테이블은 해시 함수를 사용하여 색인(index)을 버킷(bucket)이나 슬롯(slot)의 배열로 계산한다.
# 데이터를 다루는 기법 중에 하나로 데이터의 검색과 저장이 아주 빠르게 진행된다.

# 엇 그러면 이 값들을 이용해서 어떻게 배열에 넣을까요??
#
# 마이너스 값도 있고, 무지막지하게 큰 값도 있는데..
#
# 바로, 배열의 길이로 나눈 나머지 값을 쓰면 됩니다.
#
# 예를 들어 배열의 길이가 8이라면,
# 8로 나눈 나머지는 0~7이기 때문에
# 무조건 배열 내부의 인덱스로 연결될 것이라는 걸 알 수 있습니다!
#
# 그럼 이 개념을 가지고 한 번 간단하게 딕셔너리를 구현해보겠습니다.
# 딕셔너리에는 put과 get 함수가 필요합니다!
#
# put(key, value) : key 에 value 저장하기
# get(key) : key 에 해당하는 value 가져오기


class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!