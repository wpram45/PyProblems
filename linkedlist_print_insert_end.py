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
        


def sonaekle(root,veri):
    iter_im=root
    if root==None:
        yeni=Node()

        yeni.veri=veri

        return yeni
    
    else:
        while(iter_im.sonraki!=None):
            iter_im=iter_im.sonraki

        yeni=Node()

        yeni.veri=veri

        iter_im.sonraki=yeni

    return root

root=None

root=sonaekle(root,6)
root=sonaekle(root,10)
root=sonaekle(root,"c")




yazdir(root)

