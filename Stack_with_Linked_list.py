# Node를 만들어줍니다.

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack 을 만들어 줍니다.
class Stack:

    # Head를 만들고
    def __init__(self):
        self.head = None

    # Stack 쌓아줍니다.
    def push(self, data):

        # Stack 이 비어있을 때
        if self.head is None:
            self.head = Node(data)

        # Stack 이 비어있지 않을 때
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # Stack 빼주는 것들
    def pop(self):

        # Stack 이 비었을 때
        if self.head is None :
            return Node

        # Stack에 데이터가 없을 때
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

s= Stack()

s.push("a") # ["a"]
s.push("b") # ["a", "b"]
s.push("c") # ["a", "b", "c"]
s.push("d") # ["a", "b", "c", "d"]
s.push("e") # ["a", "b", "c", "d", "e"]

print(s.pop()) # e
print(s.pop()) # d
print(s.pop()) # c
print(s.pop()) # b
print(s.pop()) # a
