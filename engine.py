class node:
    def __init__(self):
        self.w = 0
        self.child = dict()

def addWord(root, char, w):
    temp = root
    for x in char:
        if x not in temp.child:
            temp.child[x] = node()
        temp = temp.child[x]
        temp.w = max(w, temp.w)


if __name__ == "__main__":
    n, q = map(int, input().split())
    root = node()
    for i in range(n):
        char, w = input().split()
        addWord(root, char, int(w))
    for i in range(q):
        character = input()
        temp = root
        index = 0
        for x in character:
            index += 1
            if x in temp.child:
                temp = temp.child[x]
            else:
                print(-1)
                break
            if index == len(character):
                print(temp.w) 
                break