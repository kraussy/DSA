class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data = elem)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return ' -> '.join(nodes)
    
    #traversing    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    #inserting node at first
    def add_first(self, new):
        new.next = self.head
        self.head = new
    
    #inserting node at last
    def add_last(self, new):
        if self.head is None:
            self.head = new
            return
        for current_node in self:
            pass
        current_node.next = new
        
    #adding node after one node
    def add_after(self, target_node_data, new):
        if self.head is  None:
            raise Exception("dude, list is empty!")
            
        for node in self:
            if node.data == target_node_data:
                new.next = node.next
                node.next = new
                return
            
        raise Exception("Node with data '%s' not found" % target_node_data)
    
    #adding node before one node
    def add_before(self, target_node_data, new):
        if self.head is None:
            raise exception("list is empty")
            
        if self.head.data == target_node_data:
            return self.add_first(new)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new
                new.next = node
                return
            prev_node = node
        
        raise Exceptions("Node with data '%s' not found" %target_node_data)
    
    #removing node
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty!")
        
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        
        raise Exception("Node with data '%s' not found" % target_node_data)
        
       
            
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
        
skyfall = LinkedList(['a', 'b', 'c', 'd'])
print(skyfall)

for elem in skyfall:
    print(elem)
    
skyfall.add_first(Node('x'))

skyfall.add_last(Node('y'))

skyfall.add_after('y', Node('n'))

skyfall.add_before('b', Node('manbadur'))
print(skyfall)

skyfall.remove_node('manbadur')
print(skyfall)



