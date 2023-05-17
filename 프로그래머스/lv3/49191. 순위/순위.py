def solution(n, results):
    wins = {x: set() for x in range(1, n + 1)}
    loses = {x: set() for x in range(1, n + 1)}
    
    for winner, loser in results:
        wins[winner].add(loser)
        loses[loser].add(winner)
    
    for player in range(1, n + 1):
        for winner in loses[player]:
            wins[winner].update(wins[player])
        for loser in wins[player]:
            loses[loser].update(loses[player])
    
    return len([player for player in range(1, n + 1) if len(wins[player]) + len(loses[player]) == n - 1])