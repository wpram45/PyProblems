dizi=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        tmp_list=[name,score]
        
        dizi.append(tmp_list)
    
    sayilar=[]
   
    for i in  range(len(dizi)):
        
        sayilar.append(dizi[i][1])
    
    mins=[]#minumum secondları tutacak liste
    
    sayilar.sort()
    first=min(sayilar) #  first minimum alındı
    
   

    for i in range(len(sayilar)):
        
        if min(sayilar[i:])==first:
            pass
            
        else:
            second=min(sayilar[i:])
            
            break
    
 
    isimler=[]
    for i  in range(len(dizi)):
        
        if dizi[i][1]==second:
            isimler.append((dizi[i][0]))
        
        else:
            pass
        
           
        
    isimler.sort()
    
    
    
    print(*isimler,sep="\n")
