"""
Time complexity: O(4^n*n) n is length of input
    4^n => 4 is for max num of letters per digit, in case of 7(p, q, r, s) or 9(w, x, y, z).
    n => for the join operation when mnemonic was found.
Space complexity: O(O(4^n*n))
"""


DIGIT_LETTERS = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


def helper(idx, phone_number, current_mnemonic, mnemonics_found):
    if idx == len(current_mnemonic):
        mnemonic_to_add = ''.join(current_mnemonic)
        mnemonics_found.append(mnemonic_to_add)
    else:
        digit = phone_number[idx]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            current_mnemonic[idx] = letter
            helper(idx+1, phone_number, current_mnemonic, mnemonics_found)


def phone_number_mnemonics(phone_number):
    current_mnemonic = ['0'] * len(phone_number)
    mnemonics_found = []
    helper(0, phone_number, current_mnemonic, mnemonics_found)
    return mnemonics_found
    

def main() -> None:
    phone_number = "1905"
    assert phone_number_mnemonics(phone_number) == ['1w0j', '1w0k', '1w0l', '1x0j', '1x0k', '1x0l', '1y0j', '1y0k', '1y0l', '1z0j', '1z0k', '1z0l']
    


if __name__ == '__main__':
    main()
