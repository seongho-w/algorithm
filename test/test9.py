# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.


class Queue():
    def __init__(self):
        self.queue = []

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        if len(self.queue) != 0:
            return self.queue.pop()
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def front(self):
        if len(self.queue) != 0:
            return self.queue[0]
        else:
            return -1
    def back(self):
        if len(self.queue) != 0:
            return self.queue[-1]
        else:
            return -1


queue = Queue()
for i in range(int(input())):

    a = input().split()

    b = a[0]


    if b == 'push':
        queue.push(a[1])
    if b == 'pop':
        print(queue.pop())
    if b == 'size':
        print(queue.size())
    if b == 'empty':
        print(queue.empty())
    if b == 'front':
        print(queue.front())
    if b == 'back':
        print(queue.back())