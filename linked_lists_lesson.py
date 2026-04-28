#Implement the Node and LinkedList classes
class Node:
    """
    A single node in a linked list.
    Attributes
    ----------
    data : any
    The value stored in this node.
    next : Node or None
    Reference to the next node, or None if this is the last node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None # by default a new node points nowhere
    
    def __str__(self):
        return f"Node({self.data})"

class LinkedList:
    """
    A singly linked list.
    Maintains a reference to the head node and tracks length.
    The tail reference allows O(1) append.
    """
    def __init__(self):
        self.head = None # first node
        self.tail = None # last node (enables O(1) append)
        self.length = 0 #length tracks number of nodes in the list
    
    def append(self, data):
        """Add a new node containing data at the end of the list."""
        new_node = Node(data)
        if self.head is None: # list is empty
            self.head = new_node
            self.tail = new_node
        else: # list already has nodes
            self.tail.next = new_node # old tail points to new node
            self.tail = new_node # new node becomes the tail
        self.length += 1
    
    def display(self):
        """Display the elements of the linked list"""
        current = self.head
        while current is not None:
            print(current.data, end = "->")
            current = current.next
        print("None")

    def search(self, target):
        """
        Search for a target in a linked list
        
        Returns
        -------
        int
            0-indexed position of the target, -1 if not found
        """
        current = self.head
        position = 0
        while current is not None:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1
    
    def insert_at(self, position, data):
        if position < 0 or position > self.length:
            raise IndexError(f'Position {position} out of range')
        
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is Node:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node
            
            if new_node.next is None:
                self.tail = new_node
        self.length += 1
    
    def delete(self, target):
        if self.head is None:
            return False
        
        if self.head.data == target:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.length -= 1
            return True
        
        current = self.head
        while current.next is not None:
            if current.next.data == target:
                if current.next is self.tail:
                    self.tail = current
                current.next = current.next.next
                self.length -= 1
                return True
            current = current.next
        return False

    def __len__(self):
        return self.length
    
    def __str__(self):
        """Return a human-readable representation: A -> B -> C -> None"""
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        return " -> ".join(parts) + " -> None"
    
#Exercise 1: gene IDs linked list
genes_ll = LinkedList()

for genes in ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC']:
    genes_ll.append(genes)

#Display the linked list
genes_ll.display()

#Search for items in the linked list
genes_ll.search('EGFR')
genes_ll.search('NOTCH1')

#Insert  
genes_ll.insert_at(0, 'PIK3CA')
genes_ll.insert_at(3, 'PTEN')
genes_ll.insert_at(genes_ll.__len__(), 'CDK4')
genes_ll.display()

#Delete
genes_ll.delete('KRAS')
genes_ll.display()

#Exercise 2: music playlist
playlist = LinkedList()
playlist.display()

for songs in ['Bohemian Rhapsody', 'Hotel California', 'Stairway to Heaven', 'Wonderwall', 'Smells like Teen Spirit']:
    playlist.append(songs)
playlist.display()

playlist.insert_at(2, 'Imagine')
playlist.display()

playlist.delete('Wonderwall')
playlist.display()

playlist.insert_at(0, 'Yesterday')
playlist.display()
playlist.__len__()

#Exercise 3: sequence assembly read buffer with a Queue
class Queue:
    """
    A FIFO queue implemented using a singly linked list
    """
    def __init__(self):
        self._list = LinkedList()
    
    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        front_data = self._list.head.data
        self._list.head = self._list.head.next
        if self._list.head is None:
            self._list.tail = None
        self._list.length -= 1
        return front_data
    
    def peek_front(self):
        if self.is_empty():
            raise IndexError("peek at an empty queue")
        return self._list.head.data
    
    def is_empty(self):
        return self._list.length == 0
    
    def size(self):
        return self._list.length
    
    def __str__(self):
        return f"Queue(front -> rear) : {self._list}"

from collections import deque

#Create a queue using deque
reads = deque()

#Enqueue items
reads.append(('R001', 'ATGCGTAAGCTTGAC'))
reads.append(('R002', 'GCGCATGATGCGCGC'))
reads.append(('R003', 'TTAGCGATCGATCGA'))
reads.append(('R004', 'ATCGATCGATCGATA'))
reads.append(('R005', 'CGCGCGCGCGCGCGC'))

#Display the items
reads.__str__()

#Compute the GC content of each read
def gc_content(sequence):
    gc_count = 0
    for base in sequence:
        if base in ["G", "C"]:
            gc_count += 1
    return round((gc_count/len(sequence)) * 100, 2)

dna = 'ATGCGTAAGCTTGAC'
print(gc_content(dna)) 

for read in reads:
    print(gc_content(read[1]))