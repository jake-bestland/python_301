# Build a custom `Stack` similar to the `Queue` you built

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.length = 0

    def is_empty(self):
        return self.bottom is None

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.bottom = new_node
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            self.length -= 1
            if self.is_empty():
                self.bottom is None
            return popped_node.value


cards = Stack()
cards.push("Ace of Hearts")
cards.push("Jack of Diamonds")
cards.push("4 of clubs")

draw_card = cards.pop()
peek = cards.peek()
print(f"Player draws: {draw_card}.  Player looks at the next card and it is: {peek}")