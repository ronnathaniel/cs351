



def hill_cipher_encrypt(*row, key: tuple = None):
    DEBUG = False

    if not key:
        key = (
            (9, 4),
            (5, 7)
        )

    if len(row) != len(key):
        print('Lengths dont match')
        print('row: ', row)
        print('key: ', key)

    mult = []

    for i, k in enumerate(key):
        spot = 0
        for j, r in enumerate(row):
            if DEBUG:
                print('r', r)
                print('k', key[j][i])
            spot += r * key[j][i]
            spot %= 26
        mult.append(spot)

    return mult


if __name__ == '__main__':
    print(
        hill_cipher_encrypt(2, 10)
    )


