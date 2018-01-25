
import sys

def leftRotation(a, d):
    print(a,d)
    a.extend([x for x in a[:d]])
    return a[d:]
    


n, d = input().strip().split(' ')
n, d = [int(n), int(d)]
a = list(map(int, input().strip().split(' ')))
result = leftRotation(a, d)
print (" ".join(map(str, result)))




