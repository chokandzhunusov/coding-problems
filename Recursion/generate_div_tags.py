"""
Time complexity: O(
    2n!
   ------
   n!(n+1)
) where n => is the input number.

Space complexity: O(
     2n!
   ------
   n!(n+1)
)

USED CATALAN NUMBERS FORMULA TO DEFINE THE COMPLEXITY
"""


def generate_div_tags_from_prefix(opening_tags_needed, closing_tags_needed, prefix, result):
    if opening_tags_needed > 0:
        new_prefix = prefix + '<div>'
        generate_div_tags_from_prefix(opening_tags_needed-1, closing_tags_needed, new_prefix, result)
    
    if opening_tags_needed < closing_tags_needed:
        new_prefix = prefix + '</div>'
        generate_div_tags_from_prefix(opening_tags_needed, closing_tags_needed-1, new_prefix, result)
    
    if closing_tags_needed == 0:
        result.append(prefix)


def generate_div_tags(number_of_tags):
    matched_div_tags = []
    generate_div_tags_from_prefix(number_of_tags, number_of_tags, '', matched_div_tags)
    return matched_div_tags      


def main() -> None:
    num_of_tags = 3
    assert generate_div_tags(num_of_tags) == ['<div><div><div></div></div></div>', '<div><div></div><div></div></div>', '<div><div></div></div><div></div>', '<div></div><div><div></div></div>', '<div></div><div></div><div></div>']
    

if __name__ == '__main__':
    main()
