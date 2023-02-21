"""
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

"""

def middleNode(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # set the slow and fast pointer at the first node
    # loop to the end, fast one is going to hit the end right when the slow one hits the middle
    # because its going twice as fast

    slowPointer = head
    fastPointer = head

    while fastPointer != None and fastPointer.next != None:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    
    return slowPointer

# Uses O(n) since you are keeping track of every single node with the set()
def detectCycle(self, head):
    currentPointer = head
    # can also be written using {}
    lookup = set()
    
    while currentPointer:
        if currentPointer in lookup:
            return currentPointer
        lookup.add(currentPointer)
        currentPointer = currentPointer.next
    return None

# Tortise and Hare Algorithm
def detectCycle(self, head):
    if not head:
        return
    
    slowPointer = head
    fastPointer = head

    while fastPointer.next and fastPointer.next.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if fastPointer == slowPointer:
            break
    
    # No Cycle
    if not fastPointer.next or not fastPointer.next.next:
        return
    
    slowPointer2 = head

    while slowPointer.next:
        if slowPointer == slowPointer2:
            return slowPointer
        slowPointer = slowPointer.next
        slowPointer2 = slowPointer2.next
    
    return
    



    