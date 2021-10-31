# Q.  링크드 리스트에서 index번째 원소를 제거하시오.
# 우리가 전에 이야기 했던 화물을 생각하면 됩니다!
#
# # 1. 흑연 칸의 연결고리를 떼서
# ["자갈"] → ["흑연"]     ["밀가루"] → ["우편"]
#
# # 2. 우편 칸으로 연결하면 됩니다!
# ["자갈"] -> ["흑연"]          ->             ["우편"]
#                                     ["밀가루"]
#
# 흑연 칸의 포인터를 다음 다음 칸으로 연결하면 됩니다.
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

    def delete_node(self, index):
        if index ==0:
            self.head = self.head.next
            return

        node = self.get_node(index -1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0,3)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()