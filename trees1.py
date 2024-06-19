class node_data:
    def __init__(self,node,hkey):
        self.node=node
        self.hkey=hkey
    def topview(root):
        temp=node_data(root,0)
        q=[temp]
        q.append(None)
        key_dict={}
        while len(q)!=0:
            curr=q.pop(0)
            if curr==None:
                if len(q)==0:
                    break
                else:
                    q.append(None)
            else:
                if curr.hkey not in key_dict.Keys():
                    key_dict[curr.hkey]=curr.node.value
                if curr.node.left!=None:
                    temp=node_data(curr.node.left,curr.hkey-1)
                    q.append(temp)
                if curr.node.right!=None:
                    temp=node_data(curr.node.right,curr.hkey+1)
                    q.append(temp)
        for i in sorted(key_dict):
            print(key_dict[i])
        print(key_dict)

    def leftview(node):
        print(node.data)
        q=[node]
        q.append(None)
        l=[]
        while len(q)>0:
            curr=q.pop(0)
            if curr==None:
                if len(q)==0:
                    break
                else:
                    q.append(None)
                    print(q[0].data)
            else:
                l.append(curr.data)
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)

root=node_data(1)
root.left=node_data(2)
root.right=node_data(3)
root.left.left=node_data(4)
root.left.right=node_data(5)
root.right.left=node_data(6)
root.right.right=node_data(7)

print(node_data.leftview(root))