"""
Time complexity: O(n)
Space complexity: O(1)
"""
    

def longest_peak(array: 'list[int]') -> 'int':
    peaks = []
    for i in range(1, len(array) - 1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            peaks.append(i)
    
    longest_peak_len = 0
    
    for peak in peaks:
        left_adjecent_index = peak - 2
        right_adjecent_index = peak + 2
        
        while left_adjecent_index >= 0 and array[left_adjecent_index] < array[left_adjecent_index+1]:
            left_adjecent_index -= 1
        while right_adjecent_index < len(array) and array[right_adjecent_index] < array[right_adjecent_index-1]:
            right_adjecent_index += 1
        
        current_peak_len = right_adjecent_index - left_adjecent_index - 1
        longest_peak_len = max(current_peak_len, longest_peak_len)
        
    return longest_peak_len

    
def main() -> None:
    ans = longest_peak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
    # ans = longest_peak([1, 3, 2])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
