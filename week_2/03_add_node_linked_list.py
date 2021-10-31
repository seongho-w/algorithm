# Q.  링크드 리스트에서 index번째 원소를 추가하시오.
# 우리가 전에 이야기 했던 화물을 생각하면 됩니다!
#
# # 1. 자갈 칸의 연결고리를 흑연 칸으로 연결하고,
# ["자갈"] -> ["흑연"]   ["밀가루"] -> ["우편"]
#
# # 2. 흑연 칸으로 연결고리를 밀가루 칸으로 연결합니다.
# ["자갈"] -> ["흑연"] -> ["밀가루"] -> ["우편"]
#
# 이 때, 밀가루 칸의 위치를 저장해둬야 # 2 에서 흑연 칸을 밀가루 칸에 연결할 수 있습니다.
# 따라서 next_node 라는 변수에 현재 노드와 연결된 노드를 저장해두고,
# # 1. 현재 노드의 다음 노드를 새로운 노드와 연결합니다.
# # 2. 새로운 노드의 다음 노드를 이전에 저장해둔 노드에 연결합니다.
#
# Tip : 현재 노드를 구하기 위해서는 방금 만든 get_node 를 사용하면 됩니다!


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

    def add_node(self,index,value):
        new_node = Node(value)  # [6]
        if index == 0:
            new_node.next = self.head # [6] -> [5]
            self.head = new_node # head -> [6] ->
            return


        node = self.get_node(index-1) #[5]
        next_node = node.next #[12]
        node.next = new_node #[5] -> [6]
        new_node.next = next_node # [6] -> [12]

        return

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.add_node(1,6)

linked_list.print_all()