def lca_with_parents(node1, node2):
    path1 = path_from_root(node1)
    path2 = path_from_root(node2)
    lca  = None
    for n1, n2 in zip(path1, path2):
        if n1 != n2:
            return n1
        lca = n1
    return lca

def path_from_root(node):
    path = []
    while node:
        path.insert(0, node)
        node = node.parent 
    return path
    
