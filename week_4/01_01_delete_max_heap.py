# 힙 -> 힙은 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
# 힙의 규칙
# 힙은 항상 큰 값이 상위 레벨에 있고 작은 값이 하위 레벨에 있어야 합니다.
# 은 항상 지켜져야 합니다.

# 최대 힙에서 원소를 삭제하는 방법은 최댓값, 루트 노드를 삭제하는 것입니다!
# 스택과 같이 맨 위에 있는 원소만 제거할 수 있고, 다른 위치의 노드를 삭제할 수는 없습니다!
# 또한 맥스 힙에 원소를 추가했던 것과 마찬가지로 원소를 삭제할때도 힙의 규칙이 지켜져야 합니다!


# Q. 맥스 힙은 원소를 제거한 다음에도 맥스 힙의 규칙을 유지해야 한다.
# 맥스 힙의 원소를 제거하시오.

# 1. 원소를 맨 마지막에 넣습니다.
# 2. 그리고 부모 노드와 비교합니다. 만약 더 크다면 자리를 바꿉니다.
# 3. 부모 노드보다 작거나 가장 위에 도달하지 않을 때까지 2. 과정을 반복합니다.


class MaxHeap:
    def __init__(self):
        self.items = [None]

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

    # 1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
    # 2. 맨 뒤에 있는 원소를 (원래 루트 노드)를 삭제한다.
    # 3. 변경된 노드와 자식 노드들을 비교합니다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿉니다.
    # 4. 자식 노드 둘 보다 부모 노드가 크거나 가장 바닥에 도달하지 않을 때까지 3. 과정을 반복합니다.
    # 5. 2에서 제거한 원래 루트 노드를 반환합니다.

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()
        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)
print(max_heap.delete())
print(max_heap.items)