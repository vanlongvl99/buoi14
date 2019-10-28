class node:
    def __init__(self):
        self.count = 0
        self.child = dict()


def addWord(root, s):
    tmp = root
    for ch in s:
        if ch not in root.child:
            tmp.child[ch] = node()
        tmp = tmp.child[ch]
    tmp.count += 1
    # return root

def findWord(root, s):
    tmp = root
    for ch in s:
        if ch not in tmp.child:
            return False
        tmp = tmp.child[ch]
    return tmp.count > 0

def isWord(node):
    return node.count > 0

def isEmpty(node):
    return len(node.child) == 0

def removeWord(root, s, level, len):
    if root == None:
        return False
    if level == len:
        if root.count > 0:
            root.count -= 1
            return True
        return False
    ch = s[level]
    flag = removeWord(root.child[ch], s, level+1, len)
    if flag == True and isWord(root.child[ch]) == False and isEmpty(root.child[ch]):
        del root.child[ch]
        root.child[ch] = None
    return flag

def printWord(root, s):
    if isWord(root):
        print(s)
    for ch in root.child:
        printWord(root.child[ch], s + ch)

if __name__ == "__main__":
    root = node()
    addWord(root, "the")
    addWord(root, "bigo")
    addWord(root, "then")
    print(findWord(root, "the"))
    removeWord(root,"then",0,4)
    print(findWord(root,"the"))  # ???theo em nghĩ kết quả phải trả về True???
    print(findWord(root, "bigo"))
    # print(findWord(root,"then"))  # ??? làm thế nào để kiểm tra mình đã xóa thành công
    # printWord(root,"bigo")  #???lệnh này k in được, nếu bỏ dòng 42 (root.child[ch] = None) thì in ra 2 lần bigo
    # printWord(root, "the  ")  #lệnh này tương tự.

    # em nghĩ phần cài đặt hàm findWord vs hàm remove của e bị sai


        