"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    curA=headA
    curB=headB
    
    while curA!=curB:
        if curA.next==None:
            curA=headB
        else:
            curA=curA.next
           
        
        if curB.next==None:
            curB=headA
        else:
            curB=curB.next
            
  
  
    return curB.data
  
  
  
  
  
  
  
