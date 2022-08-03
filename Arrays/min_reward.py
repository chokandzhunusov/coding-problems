"""
Time complexity: O(n)
Space complexity: O(n)
"""


def min_reward(scores: 'list[int]') -> 'int':
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            rewards[i] = rewards[i-1] + 1
    for j in reversed(range(len(scores) - 1)):
        if scores[j] > scores[j+1]:
            rewards[j] = max(rewards[j], rewards[j+1] + 1)
    return sum(rewards)


def main() -> None:
    ans = min_reward([8, 4, 2, 1, 3, 6, 7, 9, 5])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
