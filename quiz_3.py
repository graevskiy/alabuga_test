

def main():
    n, m, q = map(int, input().split())
    cols = input().split()
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    sign_f = {
        '>': max,
        '<': min
    }

    sign_i = {
        '>': 1,
        '<': 0
    }


    qs = {c: [None, None] for c in cols}
    for i in range(q):
        c, sign, val = input().split()
        val = int(val)
        ind = sign_i[sign]
        _func = sign_f[sign]
        qs[c][ind] = _func(qs[c][ind], val) if qs[c][ind] is not None else val

    rows = set(range(len(matrix)))
    for c_i, col in enumerate(cols):
        _min, _max = qs[col]
        rows_to_remove = set()
        for i in rows:
            if (_min and matrix[i][c_i] >= _min) or (_max and matrix[i][c_i] <= _max):
                rows_to_remove.add(i)
        rows -= rows_to_remove

    res = 0
    for r in rows:
        res += sum(matrix[r])

    return res

if __name__ == "__main__":
    print(main())