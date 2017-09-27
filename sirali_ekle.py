class Node:
    def __init__(self,veri=None,sonraki=None):
        self.veri=veri

        self.sonraki=sonraki

    def __str__(self):
        return str(self.veri)


def yazdir(root):
    
    while(root!=None):
        
        print(root)

        root=root.sonraki
        



def sirali_ekle(root,veri):


    
    if root==None:
        
        yeni=Node()

        yeni.veri=veri
        yeni.sonraki=None
        
        return yeni

    else:
       
        if veri < root.veri:
            
            yeni=Node()

            yeni.veri=veri

            yeni.sonraki=root

            return yeni

        else:
            
            iter_im=root
            while( iter_im.sonraki!=None and iter_im.sonraki.veri < veri):
                iter_im=iter_im.sonraki

            yeni=Node()

            yeni.veri=veri

            yeni.sonraki=iter_im.sonraki

            iter_im.sonraki=yeni

            return  root

            
        
    

root=None


root=sirali_ekle(root,50)
root=sirali_ekle(root,20)
root=sirali_ekle(root,100)
root=sirali_ekle(root,1)
root=sirali_ekle(root,200)
root=sirali_ekle(root,30)



yazdir(root)






