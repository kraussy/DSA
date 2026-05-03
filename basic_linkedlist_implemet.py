class Linkedlist:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
            

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
        
happy = Linkedlist()

node1 = Node('1')
happy.head = node1

print(happy)

node2 = Node('2')
node3 = Node('3')
