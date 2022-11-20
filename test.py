data = []
with open('input.txt','r') as f:
    for i in f.readlines():
        data.append(i)
print(data)
class Node():
    def inorder(self, _list: list[str] = None):
        _list = []
        if self.left:self.left.inorder()
        
        _list.append(self.data)
        _list.append(self.addr)

        if self.right:self.right.inorder()
        _list.append(self.data)
        _list.append(self.addr)
        return _list