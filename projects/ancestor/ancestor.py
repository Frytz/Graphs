import sys
sys.path.append('..')
from graph.util import Stack

def get_parents(ancestors, starting_node):
    parents = []
    for p, c in ancestors:
        if c == starting_node:
            parents.append(p)
    return parents
def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push([starting_node])
    longest_path = 1
    ancestor = None
    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        if len(path)> longest_path:
            longest_path = len(path)
            ancestor = v
        if len(path) == longest_path and ancestor:
            ancestor = v if v < ancestor else ancestor
        for p in get_parents(ancestors, v):
            path_copy = path.copy()
            path_copy.append(p)
            s.push(path_copy)
    return ancestor if ancestor else -1
    