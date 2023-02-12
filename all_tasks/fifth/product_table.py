def product_table() -> iter:
    LOWER_LIMIT = 2
    UPPER_lIMIT = 10
    COLUMN = 4

    for i in range(LOWER_LIMIT, UPPER_lIMIT, COLUMN):
        for j in range(LOWER_LIMIT, UPPER_lIMIT + 1):
            for k in range(i, i + COLUMN):
                if j == UPPER_lIMIT and k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n\n', end='')
                elif k == i + COLUMN - 1:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\n', end='')
                else:
                    print(f'{k:>} x {j:>2} = {k * j:>2}\t\t', end='')
