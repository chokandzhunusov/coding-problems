"""
Time complexity: O(n) where n is the depth of lower descendant.
Space complexity: O(1)
"""


class AncestralTree:
    def __init__(self, name) -> None:
        self.name = name
        self.ancestor = None


def get_depth(descendant, top_ancestor):
    depth = 0
    while descendant != top_ancestor:
        depth += 1
        descendant = descendant.ancestor
    return depth
    

def backtrack_tree(lower_descendant, higher_descendant, diff):
    while diff > 0:
        lower_descendant = lower_descendant.ancestor
        diff -= 1
    
    while lower_descendant != higher_descendant:
        lower_descendant = lower_descendant.ancestor
        higher_descendant = higher_descendant.ancestor
    
    return lower_descendant
    

def youngest_common_ancestor(top_ancestor, descendant_one, descendant_two):
    depth_one = get_depth(descendant_one, top_ancestor)
    depth_two = get_depth(descendant_two, top_ancestor)

    if depth_one > depth_two:
        return backtrack_tree(descendant_one, descendant_two, depth_one - depth_two)
    else:
        return backtrack_tree(descendant_two, descendant_one, depth_two - depth_one)


def main() -> None:
    a = AncestralTree('A')
    
    b = AncestralTree('B')
    b.ancestor = a
    c = AncestralTree('C')
    c.ancestor = a
    
    d = AncestralTree('D')
    d.ancestor = b
    e = AncestralTree('E')
    e.ancestor = b
    
    h = AncestralTree('H')
    h.ancestor = d
    i = AncestralTree('I')
    i.ancestor = d
    
    ans = youngest_common_ancestor(a, e, i)
    
    print(f'The answer is: {ans.name}')


if __name__ == '__main__':
    main()


"""
- This problem is really simple.
- First you have to tet the depth of each descendant, by tracking them till top ancestor.
- Create fot that a function.
- After you've got the depth of each descendant. There are two cases, one for first depth is lower, another is second lower.
- Create for that another function that will take two descendants and the difference.
- Note that the parameters that are passing should be properly provided. Don't mix them up.
"""