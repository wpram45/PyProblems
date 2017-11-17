
class Node(object):
 
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node




def GetNode(head, position):
    size=0
    iter1=head
    
    while iter1!=None:
        size+=1
        iter1=iter1.next
    
    away=size-position
    
    while away > 1:
        
        head=head.next
        
        away-=1
    head.next=None    
    
    return head.data
