class Node:
    def __init__(self,veri=None,sonraki=None):
        self.veri=veri

        self.sonraki=sonraki

    def __str__(self):
        return str(self.veri)


def yazdir(root):
    if root==None:
        print("Bağlantılı listede eleman yok")
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
        
def eleman_sil(root,aranan):
    
    if root==None:
        print("Baglantili liste hatalı")

    else:
        iter_im=root
        if root.veri==aranan:
        

            root=root.sonraki

            return root
        while iter_im.sonraki!=None and iter_im.sonraki.veri!=aranan:
            iter_im=iter_im.sonraki

        if iter_im.sonraki ==None:
            print(aranan,"Sayisi bulunamadi")

            return root

        yeni=iter_im.sonraki

        iter_im.sonraki=iter_im.sonraki.sonraki

        del yeni

        return root
    
    
root=None

root=sirali_ekle(root,30)
root=sirali_ekle(root,230)
root=sirali_ekle(root,90)



root=eleman_sil(root,30)
root=eleman_sil(root,0)
root=eleman_sil(root,230)


yazdir(root)
    
        
