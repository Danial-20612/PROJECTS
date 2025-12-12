class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Traverse and print
current = node1
while current:
    print(current.data) 
    current = current.next
