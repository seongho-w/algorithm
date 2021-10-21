class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
first_node =Node(4)
node.next = first_node
print(node.next.data)
print(node.data)

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)

    def append(self,data):
        self.head.next = Node(data)

    def print_all(self):
        print("hihihihi")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur =cur.next



Linked_List = LinkedList(3)
print(Linked_List.head.next)

