# 스택
# 한쪽 끝으로만 자료를 넣고 뺄 수 있는 자료 구조
# 스택 이라는 자료 구조에서 제공하는 기능은 다음과 같습니다!
#
# push(data) : 맨 앞에 데이터 넣기
# pop() : 맨 앞의 데이터 뽑기
# peek() : 맨 앞의 데이터 보기
# isEmpty(): 스택이 비었는지 안 비었는지 여부 반환해주기
#
# 한 번, 직접 구현해볼까요?
#
# 그 전에! 과연 스택은 뭘로 구현하면 좋을까요?
# 데이터 넣고 뽑는 걸 자주하는 자료 구조입니다!
#
# 어, 우리 같이 배웠죠! 그렇습니다. 링크드 리스트와 유사하게 구현할 수 있습니다!
# 아래 코드를 기반으로 한 번 같이 구현해보겠습니다!

# 스택의 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):  # 현재 [4] 밖에 없다면
        new_head = Node(value)  # [3] 을 만들고!
        new_head.next = self.head  # [3] -> [4] 로 만든다음에
        self.head = new_head  # 현재 head의 값을 [3] 으로 바꿔준다.
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():  # 만약 비어있다면 에러!
            return "Stack is empty!"
        delete_head = self.head  # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next  # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head  # 그리고 제거할 node 반환


    def peek(self):
        if self.is_empty():
            return "Stack is empty!"

        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())
print(stack.pop().data)
print(stack.is_empty())
print(stack.peek())