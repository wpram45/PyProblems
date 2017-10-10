s="azcbobobegghakl" #You can change string for test all cases

i=0
sayac=0
maks=0
index=0
while i < len(s)-1:
    if ord(s[i]) < ord(s[i+1]) or ord(s[i]) == ord(s[i+1]):
        sayac+=1
        
        i+=1
        

    else:
        #print(i,"girdi")
       
        sayac=0
        i+=1


    if sayac > maks:
        maks=sayac
        index=i
    #print(sayac)



print("toplam",maks,index)

print(s[index-maks:index+1])


    
