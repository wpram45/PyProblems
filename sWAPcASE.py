def swap_case(s):
    my_dict={} #dict for index and values
    my_list=[] # we will use this list at final  convert our values to str
    for i in range(len(s)):#control each element in the formal parameter  list (s)
        if s[i].isupper():#if element is upper
            my_dict[i]=s[i].lower()#then add our dict with index
        
        
        elif s[i].islower():
            my_dict[i]=s[i].upper()
        
        else:#if empty or number whatever
            my_dict[i]=s[i]
            
   
    
    for i in my_dict:
        
        my_list.append(my_dict[i])#append to our list every values which is in our dict
    
    return("".join(my_list))#return str to main func



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
