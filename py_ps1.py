import string
def score(word, f):
    my_dict={}
    my_dict_2={}
    max_lists=[]
    for i in string.ascii_lowercase:
        my_dict[i]=ord(i)-96

    
    
    
    for k in range(len(word)-1,-1,-1):
        if word[k] not in my_dict_2:
            my_dict_2[word[k]]=k*my_dict[word[k].lower()]
        

    max_lists=sorted(my_dict_2.values(), reverse=True)
    return f(max_lists[0],max_lists[1])
def f(first_highest,second_highest):
    
    return first_highest+second_highest

