# Pick one of the abstract data structures mentioned in this section that you have not yet implemented
# Build a custom Python class that demonstrates its functionality 
# Compare your solution to: https://github.com/david-legend/python-algorithms/tree/main/data-structures/src


class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node({self.value})"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        else:
            current_node = self.get_node(index)
            prior_node = self.get_node(index - 1)
            new_node.prev = prior_node
            new_node.next = current_node
            current_node.prev = new_node
            prior_node.next = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        else:
            post_node = self.get_node(index + 1)
            prior_node = self.get_node(index - 1)
            post_node.prev = prior_node
            prior_node.next = post_node
        self.length -= 1
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)



ll = DoublyLinkedList()

ll.prepend(7)
ll.prepend(5)
ll.prepend(3)
ll.insert(2, 9)
ll.get_node(2)
ll.append(11)
ll.append(13)
print(ll)
ll.remove(3)
ll.remove(2)
print(ll)
print(ll.length)
node = ll.get_node(3)
print(node.value)

print(node.prev)