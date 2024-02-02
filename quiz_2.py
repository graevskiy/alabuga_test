from collections import Counter

import operator


def main():
    n, m, q = map(int, input().split())

    p1 = Counter(map(int, input().split()))
    p2 = Counter(map(int, input().split()))

    players = {
        'A': p1,
        'B': p2,
    }

    act_player = {
        '1': operator.iadd,
        '-1': operator.isub
    }

    diff_set = set(p1.elements()).symmetric_difference(set(p2.elements()))
    diff = Counter({c: abs(p1[c] - p2[c]) for c in diff_set})

    curr_res = diff.total()
    res = []
    for _ in range(q):
        t, p, c = input().split()
        c = int(c)
        players[p][c] = act_player[t](players[p].get(c, 0), 1)
        card_diff = abs(p1.get(c, 0) - p2.get(c, 0))
        curr_res = curr_res - diff.get(c, 0) + card_diff
        diff[c] = card_diff
        res.append(curr_res)

    return res

if __name__ == "__main__":
    print(*main())
