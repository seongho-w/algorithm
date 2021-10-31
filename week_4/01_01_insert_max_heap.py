# 힙 -> 힙은 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
# 힙의 규칙
# 힙은 항상 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있어야 합니다.
# 은 항상 지켜져야 합니다.




# Q. 맥스 힙은 원소를 추가한 다음에도 맥스 힙의 규칙을 유지해야 한다.
# 맥스 힙에 원소를 추가하시오.

class MaxHeap:
    def __init__(self):
        self.items = [None]
    # 1. 새 노드를 맨 끝에 추가한다.
    # 2. 지금 넣은 새노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
    # 3. 이과정을 꼭대기까지 반복한다.

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!