"""
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists 'list1' and 'list2'.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

We need ti create a head node that allows us to return the head of the merged list
    Two pointers for each linked list
    Compare the value of each pointer and put the smaller value node into the merged linked list, update the pointer to the next
Iterate noth linked list at the same time unitl one reaches the end, then return the head
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Traverse both lists, make a new head node (make separate list)
    # Set the next node as the smaller value between the two nodes

    # Beginner Node
    tempNode = ListNode(0)
    currentNode = tempNode

    # Traverse the list
    while (l1 != None and l2 != None):
        if (l1.val < l2.val):
            currentNode.next = l1
            l1 = l1.next
        else: 
            currentNode.next = l2
            l2 = l2.next
        
        currentNode = currentNode.next

        # Edge cases for catching if the lengths are different

    if l1 != None:
        currentNode.next = l1
        l1 = l1.next
        
    if l2 != None:
        currentNode.next = l2
        l2 = l2.next

    return tempNode.next

"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list
Solution, Iteration
[1,2,3,4,5]
Output: [5,4,3,2,1]
"""

def reverseList(head):
    prev = None

    while(head != None):
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev
