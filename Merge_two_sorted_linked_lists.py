
 
class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node




def MergeLists(headA, headB):
    my_arr=[]
    if headA==None and headB==None:
        return None
    else:
        while headA!=None:
            my_arr.append(headA.data)
            headA=headA.next
            
        while headB!=None:
            my_arr.append(headB.data)
            headB=headB.next
        
        counter=len(my_arr)
        head=Node()
        iter1=head
        my_arr.sort()
        my_arr.reverse()
        #print(len(my_arr))
        while counter > 0:
            new_node=Node(my_arr[counter-1])
            iter1.next=new_node
            iter1=iter1.next
            counter-=1
        head=head.next
        
        return head
        #while head!=None:
           # print(head.data)
           # head=head.next
        
        
        
  
  
  
  
  
  
  
  
  
  
