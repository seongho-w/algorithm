# Q.  링크드 리스트에서 index번째 원소를 반환하시오.
# 노드를 따라가면서 값을 찾아야 합니다.
# head에 저장되어있는 노드를 node 라는 변수에 담고,
# count 라는 인덱스를 저장하기 위한 변수를 저장합니다.
#
# 그리고 count 가 index 가 될 때까지
# (이 때, while 문 내부에서 1씩 더해주니까 작을때까지로 조건을 넣습니다)
# node의 next 값을 node 에 대입하고 count 를 증가합니다.
# 이 과정을 count 가 index가 아닐때까지 반복하면 됩니다!
#
# 그리고 node 를 반환해줍니다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(0).data) # -> 5를 들고 있는 노드를 반환해야 합니다!