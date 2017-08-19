def split_and_join(line):
    my_list=[]
    
    mylist=line.split(" ")#str to list(split)
    
   
    
    return "-".join(mylist)#return string






if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
