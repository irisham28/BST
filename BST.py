class Tree:
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None 

def inordertraversal(root):# left, root, right
        if root is not None:
            if root.left is not None:
                inordertraversal(root.left)

            print(root.data, end = "-")
            
            if root.right is not None:
                inordertraversal(root.right)

root = Tree(2)
root.left = Tree(1)
root.right = Tree(10)
root.right.left = Tree(4)
root.right.left.left = Tree(3)
root.right.left.right = Tree(5)
root.right.right = Tree(12)


inordertraversal(root)


#inserting new element to the BST
def insert(root,key):
     #if the tree is empty
     if root is None:
          return Tree(key)
     
     if key < root.data:
          root.left = insert(root.left, key)
     else:
        root.right = insert(root.right, key)

     return root
#checking the insert
insert(root, 7)
print()
inordertraversal(root)

#searching an item in the BST
def search(root,key):
     #Base case: root is null or node that youre finding is at the root itself
     if root is None or root.data == key:
          return root
     #key is greater than root
     if key>root.data:
          return search(root.right, key)
     

     return search(root.left, key)

#checking
print()
key = 7
search_node = search(root,key)
if search_node:
     print("we got it")
else:
     print("this node doesn't exist")









