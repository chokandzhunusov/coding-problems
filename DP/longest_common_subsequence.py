"""
Time complexity: O(nm)
Space complexity: O(nm) can be optimized!
"""


def longest_common_subsequence(s1, s2):
    lcs = [[[None, 0, None, None] for x in range(len(s1) + 1)] for y in range(len(s2) + 1)]
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i-1] == s1[j-1]:
                lcs[i][j] = [s2[i-1], lcs[i-1][j-1][1] + 1, i-1, j-1]
            else:
                if lcs[i-1][j][1] > lcs[i][j-1][1]:
                    lcs[i][j] = [None, lcs[i-1][j][1], i-1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j-1][1], i, j-1]
    return build_sequence(lcs)


def build_sequence(lcs):
    sequence = []
    i = len(lcs) - 1
    j = len(lcs[0]) - 1
    while i != 0 and j != 0:
        current_entry = lcs[i][j]
        if current_entry[0] != None:
            sequence.append(current_entry[0])
        i = current_entry[2]
        j = current_entry[3]
    return list(reversed(sequence))


def main() -> None:
    s1 = 'ZXVVYZW'
    s2 = 'XKYKZPW'
    print(longest_common_subsequence(s1, s2))
    return


if __name__ == '__main__':
    main()