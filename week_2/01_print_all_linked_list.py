# 따라서 LinkedList 라는 클래스를 한 번 만들어볼게요!
# LinkedList 는 head node 만 딱 들고 있습니다.
#
# 기차를 다시 떠올려보면, 맨 앞 칸만 저장해두는 거에요.
# 다음 칸을 보기 위해서는 next를 통해서 다음 노드에 접근해야 합니다!
#
# 정리하면,
# 1) LinkdList 는 self.head 에 시작하는 노드를 저장한다.
# 2) 다음 노드를 보기 위해서는 각 노드의 next 를 조회해서 찾아가야 한다.
#
# 그럼 이제 한 번 만들어보겠습니다!

# 이번에는,
# LinkedList 의 맨 뒤에 새로운 Node 를 붙이는 **append** 함수를 만들어보겠습니다!
# 현재 있는 노드의 가장 맨 뒤에 새로운 값을 가진 노드를 추가해주시면 됩니다!
# 그러기 위해서는 **가장 맨 뒤의 노드까지** 가야 합니다.
#
# **맨 뒤의 노드까지** 가기 위해서는 어떻게 해야 할까요?
# 현재 링크드 리스트는 다음과 같다고 합니다.
# head
# [3] → [5] → [6] → [8]
#
# 바로, head 를 따라서 계속 이동해야 합니다!
# head 를 변경시킬 수는 없으니, cur 이라는 변수를 이용해볼게요
#
# cur = this.head 에 넣으면 아래와 같이 되고,
#
# cur
# [3] → [5] → [6] → [8]
#
# cur = cur.next 을 하면 다음과 같이 한 칸 이동합니다.
#
#           cur
# [3] → [5] → [6] → [8]
#
# cur = cur.next 또 하면?
#
#                      cur
# [3] → [5] → [6] → [8]
#
# 이걸 언제까지 반복할까요?
# **맨 뒤의 노드까지 라는 소리는** `cur.next 가 None` 이라는 것을 의미합니다.
# 맨 마지막 노드는 다음 노드가 없으니까 아무것도 가리키지 않을테니까요!
#
# 그럼 이제 코드로 한 번 만들어보겠습니다!

# Q.  링크드 리스트의 모든 원소를 출력하시오.

# 노드를 따라가면서 값을 출력해야 합니다.
# head에 저장되어있는 노드를 cur 라는 변수에 담고,
# cur 의 data를 출력합니다.
# 그리고 cur의 next 값을 cur 에 대입하고 그 값을 출력합니다.
# 이 과정을 cur 이 None 이 아닐때까지 반복하면 됩니다!

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

