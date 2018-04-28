"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
from collections import OrderedDict
first_dict=OrderedDict()
second_dict=OrderedDict()

def lca(root , v1 , v2):
    found_v2=False
    found_v1=False
    
    
    
    if v1==root.data or v2==root.data:
        return root
    else:
        iterim=root
        #loop until found v2
        while found_v2==False:
            
            if found_v1==False:
                if v1>iterim.data:
                    first_dict[iterim]=iterim.data
                    if iterim.right!=None:
                        iterim=iterim.right
                        
                elif v1<iterim.data:
                    first_dict[iterim]=iterim.data
                    
                    if iterim.left!=None:
                        iterim=iterim.left
                        
                else:
                    first_dict[iterim]=iterim.data
                    ###v1 found
                    iterim=root
                    found_v1=True
            else:
               ######find v2     
                if v2>iterim.data:
                    second_dict[iterim]=iterim.data
                    if iterim.right!=None:
                        iterim=iterim.right
                        
                elif v2<iterim.data:
                    second_dict[iterim]=iterim.data
                    
                    if iterim.left!=None:
                        iterim=iterim.left
                        
                else:
                    found_v2=True
                        

                    
       # print(iterim.data)
            #v1 found
            #find v2
                #if v2 > iterim.data:
                   # second_dict[iterim]=iterim.data
                  #  iterim=iterim.right
                #elif v2 < iterim.data:
                   # second_dict[iterim]=iterim.data
                   # iterim=iterim.left
               # else:
                   # found_v2=True
                   # break
                    
                    
            
        #print(first_dict)
       # print(second_dict)
    
    
        for key, value in reversed(list(first_dict.items())):
            #print(key,value)
            
            for key2,value2 in reversed(list(second_dict.items())):
                if key==key2:
                   # print(key)
                    return key
   
        #for i in first_dict:
            #for j in second_dict:
              #  if i==j:
                    
                  #  return i
            
  #Enter your code here
