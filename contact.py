class node:
    def __init__(self):
        self.count = 1
        self.child = dict()

def addWord(root, char):
    temp = root
    for x in char:
        if x not in temp.child:
            temp.child[x] = node()
            temp = temp.child[x]
        else:
            temp = temp.child[x]
            temp.count += 1


if __name__ == "__main__":
    n = int(input())
    root = node()
    for i in range(n):
        a, b = input().split()
        if a == "add":
            addWord(root, b)
        else:
            index = 0
            temp = root
            for x in b:
                index += 1
                if x in temp.child:
                    temp = temp.child[x]
                else:
                    print(0)
                    break
                if index == len(b):
                    print(temp.count)
                    break
