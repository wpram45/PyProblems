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
        



def basaekle(root,veri):

    if root==None:
        yeni=Node()

        yeni.veri=veri

        return yeni

    else:
        yeni=Node()

        yeni.veri=veri

        yeni.sonraki=root

        return yeni

root=None

root=basaekle(root,6)
root=basaekle(root,10)
root=basaekle(root,"c")






yazdir(root)
