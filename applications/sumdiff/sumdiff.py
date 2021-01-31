"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def sum_diff(values:{int}):
    sums = {}
    diffs = {}
    for x in q:
        for y in q:
            sum = f(x) + f(y)
            diff = f(x) - f(y)
            if sum not in sums:
                sums[sum] = {(x,y)}
            else:
                sums[sum].add((x,y))
            if diff not in diffs:
                diffs[diff] = {(x,y)}
            else:
                diffs[diff].add((x,y))

    for val in sums:
        if val in diffs:
            for sum_pairs in sums[val]:
                for diff_pairs in diffs[val]:
                    print(f'f({sum_pairs[0]}) + f({sum_pairs[1]})', end=' = ')
                    print(f'f({diff_pairs[0]}) - f({diff_pairs[1]})', end='\t')
                    print(f'{f(sum_pairs[0])} + {f(sum_pairs[1])}', end=' = ')
                    print(f'{f(diff_pairs[0])} + {f(diff_pairs[1])}')

sum_diff(q)
