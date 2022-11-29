'''
Sequence Alignment Problem
'''

import numpy as np


def get_min_penalty_string(x, y, pxy, pgap):
    '''
    Find the minimum penalty.

    Args:
        x (str)
        y (str)
        pxy (int)
        pgap (int)

    Returns:
        int
    '''

    m, n = len(x), len(y)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    dp[0: (m+1), 0] = [i * pgap for i in range(m + 1)]
    dp[0, 0: (n+1)] = [i * pgap for i in range(n + 1)]

    i = 1
    while i <= m:
        j = 1
        while j <= n:
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + pxy, dp[i - 1]
                               [j] + pgap, dp[i][j - 1] + pgap)
            j += 1
        i += 1

    x_align, y_align = np.zeros(
        (m + n), dtype=str), np.zeros((m + n), dtype=str)

    i, j = m, n

    while not (i == 0 and j == 0):
        if dp[i][j] == dp[i - 1][j - 1] + (0 if x[i - 1] == y[j - 1] else pxy):
            x_align[i + j - 1] = x[i - 1]
            y_align[i + j - 1] = y[j - 1]
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + pgap:
            x_align[i + j - 1] = x[i - 1]
            y_align[i + j - 1] = '-'
            i -= 1
        else:
            x_align[i + j - 1] = '-'
            y_align[i + j - 1] = y[j - 1]
            j -= 1

    return dp[m][n], ''.join(x_align), ''.join(y_align)


def main():
    x = 'AGGGCT'
    y = 'AGGCA'
    pxy = -3
    pgap = -2

    penalty, x_align, y_align = get_min_penalty_string(x, y, pxy, pgap)

    print(penalty)
    print(x_align)
    print(y_align)


if __name__ == '__main__':
    main()
