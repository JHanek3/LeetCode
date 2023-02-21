"""
Background Knowledge on LinkedLists
https://realpython.com/linked-lists-python/

Understanding Linked Lists
    Ordered Collection of Objects
    They differ than normal lists in the way that they store elements in memory
    lists use continuous memory block to store references to their data, linked lists store references as part of their own element

Main Concepts
    Each element of a linked list is called a node
        Data contains the value to be stored in the node
        Next contains a reference to the next node on the list
    A linked list is a collection of nodes
        First node is called the head, its the starting point for any iteration
        Last node must have its next reference pointing to None to determine the end of the list

Practical Applications
    Implement queues, stacks, graphs
    Lifecycle management for an os application

Queues or Stacks
    Queue, you use First-In/First-Out
    First element inserted is the first retrieved
    Stack, List-In/First-Out
        Last element inserted in the list is the first to be retrieved

Graphs
    Show relationships between objects or to represent different ypes of networks
        Adjacency list, a list of linked lists where each vertex of the graph is stored alongside a collection of connected vertices

Performance Comparison: Lists vs. Linked Lists
    Python lists are dynamic arrays (memory usage is very similar)

Insertion and Deletion of Elements
    insert() or append(), remove() or pop()
    append() or insert() at the end will have a constant time O(1)
    When you try to insert near the beginning of the list, the average time comlexity will grow along with the size of the list
    Linked Lists, when it comes to insertion and deletion of elements at the beginning or the end, their time complexity is O(1)
    Linked Lists performance advantage for FIFO, since continuously inserted and removed at the beginning of the list.
    Linked Lists perform similary to a list when impementing a stack, since elements are inserted and removed at the end of the list

Retrieval of Elements
    When it comes to element lookup, lists perform much better than linked lists
    Know which element you want to access, list can perform this operation in O(1) time
        Linked Lists take O(n), you need to traverse the whole list
    Searching for a specific element, both lists and linked lists perform very similarly, O(n)
        Iterate through the whole list to find the element you are looking for

Implementing your own linked lists
    Practicing your Python algorithm skills
    Learning about data structure theory
    Preparing for Job Interviews
"""

# How to Create a Linked List
# The only information you need to store for a linked list is where the list starts (head of the list)
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " - > ".join(nodes)

class Node:
    # Two main elements of a node
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # Official string representation of the object
    def __repr__(self):
        return self.data

list1 = LinkedList()
print(list1)

firstNode = Node("a")
list1.head = firstNode
print(list1)

secondNode = Node("b")
thirdNode = Node("c")
firstNode.next = secondNode
secondNode.next = thirdNode
print(list1)
    
    

    
