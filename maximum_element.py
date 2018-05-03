
class Stack:
     def __init__(self):
         self.items = []

   


     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[self.size()-1]

     def size(self):
         return len(self.items)


    



n=int(input())

main_stack=Stack()
track_stack=Stack()


for i in range(n):
    query=list(map(int,input().split(" ")))
    #print(query)
    
   # print("Stack:",track_stack.items)
    
   # if len(query)>1:
      #  print(query[0],query[1],stack.items,"max:",curMax)
        
   
   # else:
 #       print(query[0],stack.items,"max:",curMax)
    
    if query[0]==1:
        if main_stack.items==[]:
            
            #print("gg")
            main_stack.push(query[1])
            track_stack.push(query[1])
            
        else:
            main_stack.push(query[1])
            
            
            if query[1] > track_stack.peek():
                track_stack.push(query[1])
                
            else:
                track_stack.push(track_stack.peek())
             
        
    elif query[0]==2:
        main_stack.pop()
        track_stack.pop()

            
                
            
       
            
        
    elif query[0]==3:
        print(track_stack.items[len(track_stack.items)-1])
        
    
