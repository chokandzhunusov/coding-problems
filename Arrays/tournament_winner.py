"""
Time complexity: O(n)
Space complexity: O(k) number of teams
"""


def tournament_winner(competitions: "list[list[str]]", results: "list[list[str]]") -> "list[int]":
    scores = {}
    for (i, c) in enumerate(competitions):
        home_team, away_team = c
        if results[i] == 0:
            if not scores.get(away_team):
                scores[away_team] = 3
                continue
            scores[away_team] += 3
        else:
            if not scores.get(home_team):
                scores[home_team] = 3
                continue
            scores[home_team] += 3
    
    return sorted(scores.items(), key=lambda x: x[1])[-1][0]


def main() -> None:
    competitions = [
        ['HTML', 'C#'],
        ['C#', 'Python'],
        ['Python', 'HTML'],
    ]
    results = [0, 0, 1]
    ans = tournament_winner(competitions, results)
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
