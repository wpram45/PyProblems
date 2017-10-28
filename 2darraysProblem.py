#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


temp_sum=0
max_sum=0
for i  in range(4):
    for j in range(4):
        temp_sum = 0
            # top row
        temp_sum += arr[i][j]
        temp_sum += arr[i][j+1]
        temp_sum += arr[i][j+2]
            #middle 
        temp_sum += arr[i+1][j+1]
            #bottom row
        temp_sum += arr[i+2][j]
        temp_sum += arr[i+2][j+1]
        temp_sum += arr[i+2][j+2]
        if(temp_sum > max_sum or i == 0 and j == 0):
            max_sum = temp_sum

print(max_sum)