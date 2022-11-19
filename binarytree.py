class Node():                   
    def __init__(self, data=None, addr=None):
        self.data = data
        self.addr = addr
        self.right = None
        self.left = None
    def insert(self, data, addr):
        if self.data :
            if data < self.data:
                if self.left: self.left.insert(data, addr)
                else: self.left = Node(data, addr)
            else:
                if self.right: self.right.insert(data, addr)
                else: self.right = Node(data, addr)     
        else: 
            self.data = data
            self.addr = addr
    def inorder(self):
        if self.left:self.left.inorder()
        print(self.data,end=' ')
        print(self.addr)

        if self.right:self.right.inorder()
    def __contains__(self, x):
        if x in self:
            print('test success')
        return True


if __name__ == '__main__':
    tree = Node()
    datas = ['Allen','Ellen','Jack','Lisa','Jennie','Curry','Lebron']    
    for data in datas:
        tree.insert(data)
    tree.inorder()
    # 在insert一次
    tree.insert('Luka')
    print("-"*30)
    tree.inorder()
    

    tree2 = Node(2)
    tree2.data = 3 # test
    tree2.inorder()