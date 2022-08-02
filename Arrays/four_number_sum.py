"""
Time complexity: O(n^2)
Space complexity: O(n^2)
"""
    

def four_number_sum(array: 'list[int]', target: 'int') -> 'list[int]':
    quadruplets = []
    all_pair_sums = {}
    
    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            current_num = array[i]
            next_num = array[j]
            current_sum = current_num + next_num
            difference = target - current_sum
            if difference in all_pair_sums:
                for pair in all_pair_sums[difference]:
                    quadruplets.append(pair + [current_num, next_num])
        
        for k in range(i):
            current_num = array[i]
            prev_num = array[k]
            current_sum = current_num + prev_num
            if current_sum not in all_pair_sums:
                # Important because other numbers may reulted to same hash key:
                # [5, -5, 2, -2, ...]
                all_pair_sums[current_sum] = [[prev_num, current_num]]
            else:
                all_pair_sums[current_sum].append([current_num, prev_num])
    return quadruplets


def main() -> None:
    # ans = four_number_sum([7, 6, 4, -1, 1, 2], 16)
    # ans = four_number_sum([1, 2, 3, 4, 5, 6, 7], 10)
    ans = four_number_sum([5, -5, -2, 2, 3, -3], 0)
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
