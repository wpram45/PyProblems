def Validator(str_main):
    my_dict={0:".isalnum()",1:".isalpha()",2:".isdigit()",3:".islower()",4:".isupper()"}
    
    control_dict={0:False,1:False,2:False,3:False,4:False}
    
   
    for j in range(len(str_main)):
        
        for i in control_dict:
            
            if eval("str_main[j:j+1]" +my_dict[i]):
                control_dict[i]=True
    
    
    
    
                
                
    
    
    for _ in control_dict:
        print(control_dict[_])
    
if __name__ == '__main__':
    s = input()
    
    Validator(s)

    
    
