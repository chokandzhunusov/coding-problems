"""
Time complexity: O(nm)
Space complexity: O(nm) can be optimized!
"""


def levenshtein_distance(str_1, str_2):
    edits = [[x for x in range(len(str_1) + 1)] for y in range(len(str_2) + 1)]
    for i in range(1, len(str_2) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    
    for i in range(1, len(str_2) + 1):
        for j in range(1, len(str_1) + 1):
            if str_2[i - 1] == str_1[j-1]:
                edits[i][j] = edits[i - 1][j-1]
            else:
                edits[i][j] = 1 + min(edits[i-1][j-1], edits[i-1][j], edits[i][j-1])
    
    return edits[-1][-1]


def main() -> None:
    str_1 = 'abc'
    str_2 = 'yabd'
    print(levenshtein_distance(str_1, str_2))
    return


if __name__ == '__main__':
    main()