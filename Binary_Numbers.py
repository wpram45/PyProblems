#!/bin/python3

import sys


n = int(input().strip())
my_list=[]
def my_func(sayi):
  
    rem=int(sayi%2)
 
    bolum=(sayi-rem)/2
  
    if sayi == 2 :

        my_list.append(1)
        my_list.append(rem)
      
        
    elif sayi < 2:

        my_list.append(rem)
       
    
    else:
       
        my_list.append(rem)
        my_func(bolum)
        
    
my_func(n)
my_list.reverse() #reverse
print(my_list)

maks=0
counter=1
for i in range (len(my_list)-1):
   
    
    if my_list[i] == my_list[i+1] == 1:
        counter+=1
    else:
        counter=1
        pass

    if counter > maks:
        maks=counter

print(maks)
    
