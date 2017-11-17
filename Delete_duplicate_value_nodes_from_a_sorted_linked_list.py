
 
class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node



def RemoveDuplicates(head):
    iter1=head
    iter2=Node(head.data)
    my_arr=[]
    if head==None:
        return None
    
    else:
        while iter1!=None:
            my_arr.append(iter1.data)
            
            if iter1.next!=None:
                if iter1.next.data in my_arr:
                    iter1.next=iter1.next.next
           
            
            iter1=iter1.next
        if head.next!=None:
            if head.next.data==head.data:
                return iter2
            else:
                return head
        else:
            
            
            return head
        
  
  
  
  
  
  
  
  
