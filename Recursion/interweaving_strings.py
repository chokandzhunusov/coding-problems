"""
Time complexity: 
    O(2^(n+m)) for the version without cache
    O(nm) cache version
Space complexity: 
    O(n+m) for the version without cache
    O(nm) cache version
"""


def are_interwoven(one: 'str', two: 'str', three: 'str', i: 'int', j: 'int', cache: 'list[list[bool]]'):
    print(cache)
    if cache[i][j]:
        return cache[i][j]
    
    k = i + j  # for index in three => three[k]
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = are_interwoven(one, two, three, i+1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = are_interwoven(one, two, three, i, j+1, cache)
        return cache[i][j]
    
    cache[i][j] = False
    
    return False
    

def interweaving_strings(one: 'str', two: 'str', three: 'str'):
    if len(three) != len(one) + len(two):
        return False

    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]  # note +1
    return are_interwoven(one, two, three, 0, 0, cache)  # 0, 0 are indexes for one[0] and two[0]


# def are_interwoven(one, two, three, i, j):
#     k = i + j  # for index in three => three[k]
#     if k == len(three):
#         return True

#     if i < len(one) and one[i] == three[k]:
#         if are_interwoven(one, two, three, i+1, j):
#             return True

#     if j < len(two) and two[j] == three[k]:
#         return are_interwoven(one, two, three, i, j+1)

#     return False
    

# def interweaving_strings(one: 'str', two: 'str', three: 'str'):
#     if len(three) != len(one) + len(two):
#         return False

#     return are_interwoven(one, two, three, 0, 0)  # 0, 0 are indexes for one[0] and two[0]

    
def main() -> None:
    one = 'algoexpert'
    two = 'your-dream-job'
    three = 'your-algodream-expertjob'
    three_false = 'your-algodream-expertjobbbbb'
    assert interweaving_strings(one, two, three)
    assert not interweaving_strings(one, two, three_false)
    

if __name__ == '__main__':
    main()
