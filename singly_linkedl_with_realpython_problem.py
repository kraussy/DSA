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
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        
    def remove(self):
        self.head = self.head.next
        return
        
        
    
    #retrieve an element from a specific position: get(i)  
    def get(self, index):
        if index < 0:
            raise Exception("Negative index ain't possible.")
        
        current_index = 0
        for node in self:
            if current_index == index:
                return node.data
            current_index += 1
                
    
    #reverse the linkedlist
    def reverse(self):
        prev_node = None            # ← Start with nothing
        current_node = self.head    # ← Start at head
        
        while current_node is not None: 
            next_node = current_node.next   # ← Save the next one FIRST!
            
            current_node.next = prev_node # Now flip the pointer
            
            prev_node = current_node # ← Remember this node
            current_node = next_node # ← Move to the saved next
        self.head = prev_node  # After loop, update self.head
         
   
            
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

#Create a Queue() object inheriting this article’s linked list with enqueue() and dequeue() methods.
class Queue(LinkedList):
    def __init__(self, nodes = None):
        super().__init__(nodes) 
    
    def enqueue(self, data):
        node = Node(data)
        self.add_last(node)
      
    def dequeue(self):
        self.remove()
    
        
skyfall = LinkedList(['a', 'b', 'c', 'd'])
print(skyfall)


print(skyfall.get(3))

skyfall.reverse()
print(skyfall)

skyfall.add_last(Node('x'))
print(skyfall)

skyfall.remove()

queue = Queue(['a', 'b', 'c', 'd'])
queue.enqueue('e')
print(queue)

queue.dequeue()
print(queue)



