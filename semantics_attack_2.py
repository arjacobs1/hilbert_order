import math

class Tree:
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
                
    def __repr__(self):
        return self.name
    
    def add_child(self, node):
        self.children.append(node)

    def num_leaves(self, node):
        leaves = 0
        if not len(node.children):
            leaves += 1
        else:
            for child in node.children:
                leaves += Tree.num_leaves(self, Tree(child))
        return leaves

def getN(encMap):
    hmax = 0
    length = len(encMap)
    while length > 0:
        if encMap[length - 1] > hmax:
            hmax = encMap[length - 1]
        length -= 1

    k = 0
    while 2 ** (2 * k) < hmax:
        k += 1
    n = 2 ** (2 * k)
    N = int(0.5 * math.log(n, 2))

    print("N: ", N)

def checkNode(Map, tree, cat, maxCat, x, Nodes):
    if isinstance(Map[x][cat], Tree) and cat < maxCat:
        cat += 1
        checkNode(Map, Tree(Map[x][cat]), cat, maxCat, x, Nodes)
    else:
        Nodes[Map[x][cat]] = Tree(Map[x][cat])
        tree.add_child(Nodes[Map[x][cat]])
        while cat < maxCat:
            cat += 1
            Nodes[Map[x][cat]] = Tree(Map[x][cat])
            Nodes[Map[x][cat - 1]].add_child(Nodes[Map[x][cat]])

def buildTree(Map, Nodes):
    tree = Tree()
    cat = 1
    maxCat = len(Map[0]) - 1
    for x in range(0, len(Map)):
        checkNode(Map, tree, cat, maxCat, x, Nodes)
    return tree
        
def heuristics(Map, MapCat, encMap, encMapCat):
    MapNodes = {}
    MapTree = buildTree(MapCat, MapNodes)
    encNodes = {}
    encMapTree = buildTree(encMapCat, encNodes)
    print(MapTree.num_leaves(encMapTree))
    print(MapTree.num_leaves(encNodes[""]))

Map = [[12, 27], [23, 6], [13, 2], [5, 21], [2, 30], [29, 28]]
MapCat = [["burgerking", "restaurant", "burgers"], ["dairyqueen", "restaurant", "icecream"], ["cooliocafe", "cafe",""]]
encMap = [12, 3, 29, 16, 7, 21]
encMapCat = [["alskjdf", "snalroi", "aklsdf"], ["weifoj", "pijfeois", ""], ["quiofjkl", "xiojlse", "lsakdjf"], ["pweofj", "qpeofj", ""], ["apoiej", "wonweaf", "slkdja"], ["pewfaoi", "godsigsef", ""]]
getN(encMap)
heuristics(Map, MapCat, encMap, encMapCat)
