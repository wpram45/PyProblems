def decodeHuff(root , s):
   
    result=""
    iterim=root
    #print(iterim.right.data)
    i=0
    
    
    
    end=False
    while end==False:
        try:
            current=s[i]
            
           # print("current",current)
        
            if current[len(current)-1]=="1":
                iterim=iterim.right
            elif current[len(current)-1]=="0":
                iterim=iterim.left
            
            if iterim.data=='\0':
                current+=s[i]
                
    
            else:
                
                sys.stdout.write(iterim.data)
 
                sys.stdout.flush()
                current=""
                iterim=root
            i+=1
        except:
            end=True
            break
