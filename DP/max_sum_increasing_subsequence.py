"""
Time complexity: O(n^2)
Space complexity: O(n)
"""


def max_sum_increasing_subsequence(array):
    sequences = [None for x in array]
    sums = [num for num in array]
    max_sum_idx = 0
    for i in range(len(array)):
        current_num = array[i]
        for j in range(0, i):
            other_num = array[j]
            if other_num < current_num and sums[j] + current_num >= sums[i]:
                sums[i] = sums[j] + current_num
                sequences[i] = j
        if sums[i] >= sums[max_sum_idx]:
            max_sum_idx = i
    return [sums[max_sum_idx], build_sequence(array, sequences, max_sum_idx)]


def build_sequence(array, sequences, current_idx):
    sequence = []
    while current_idx is not None:
        sequence.append(array[current_idx])
        current_idx = sequences[current_idx]
    return list(reversed(sequence))


def main() -> None:
    print(max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 80]))
    return


if __name__ == '__main__':
    main()