class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None


def preorder(root):
    if root==None:
        return
    print(root.value,end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root==None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.value,end="")

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value,end="")
    inorder(root.right)

def levelOrder(root):
    q=[root]
    q.append(None)
    

    while len(q)>0:       #check for queve untill length<0
        curr=q.pop(0)   #delete first element

        if curr==None:
            if len(q)==0:
                break
            else:
                print()
                q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                q.append(curr.left)
            if curr.right !=None:
                q.append(curr.right)

def height(root):
    if root==None:
        return 0
    return max(height(root.left),height(root.right))+1
    



if __name__=="__main__":
    root=node(1)     #root node (R)
    #left node(l )
    root.left=node(2)
    #right node(r)
    root.right=node(5)

    root.left.left=node(3)
    root.left.right=node(4)
    
    # root.right.left=node(6)
    root.right.right=node(6)

    root.left.right.left=node(9)
    root.left.right.left.right=node(10)
    root.left.right.left.left=node(14)
    # root.left.right.right=node(10)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.right.right.left.right=node(11)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13)

    # root.right.right.right=node(11)
    # root.left.right.right.left=node(12)
    # root.left.right.right.right=node(13)

    # preorder(root)
    # postorder(root)
    # inorder(root)
    # levelOrder(root)
    print(height(root))