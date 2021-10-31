# 큐
# 한쪽 끝으로 자료를 넣고, 반대쪽에서는 자료를 뺄 수 있는 선형구조.

# 큐라는 자료 구조에서 제공하는 기능은 다음과 같습니다!
#
# enqueue(data) : 맨 뒤에 데이터 추가하기
# dequeue() : 맨 앞의 데이터 뽑기
# peek() : 맨 앞의 데이터 보기
# isEmpty(): 큐가 비었는지 안 비었는지 여부 반환해주기
#
# 한 번, 직접 구현해볼까요?
#
# 그 전에! 과연 큐는 뭘로 구현하면 좋을까요?
# 데이터 넣고 뽑는 걸 자주하는 자료 구조입니다!
#
# 그렇습니다. 스택과 마찬가지로 링크드 리스트와 유사하게 구현할 수 있습니다!
# 아래 코드를 기반으로 한 번 같이 구현해보겠습니다!
#
# 이 때, 스택과 다르게 큐는 끝과 시작의 노드를 전부 가지고 있어야 하므로,
# # self.head 와 self.tail 을 가지고 시작합니다!

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
            new_node = Node(value)
            if self.is_empty():  # 만약 비어있다면,
                self.head = new_node  # head 에 new_node를
                self.tail = new_node  # tail 에 new_node를 넣어준다.
                return

            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"  # 만약 비어있다면 에러!

        delete_head = self.head  # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next  # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head.data  # 그리고 제거할 node 반환
        # 어떻게 하면 될까요?


    def peek(self):
        if self.is_empty():
            return "Queue is empty!"

        return self.head.data
        # 어떻게 하면 될까요?


    def is_empty(self):
        return self.head is None
        # 어떻게 하면 될까요?

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())