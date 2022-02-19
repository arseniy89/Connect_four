from itertools import product


def cout():
    [print(f'    {i+1}', end='') for i in range(6)]
    print(s:=(f"\n  {'●━━━━'*6}●"))
    [print(f'{i+1} ┃ {b[i][0]} ┃ {b[i][1]} ┃ {b[i][2]} ┃ {b[i][3]} ┃ {b[i][4]} ┃ {b[i][5]} ┃ {i+1}{s}') 
    for i in range(6)]
    [print(f'    {i+1}', end='') for i in range(6)]
    print()


def possibility(i, j):
    return (i == 5 or b[i+1][j] != '  ') and b[i][j] == '  '


def reading(step):
    while 1:
        try:
            i = int(input('2nd: ' if (step%2) else '1st: ')) - 1
            j = int(input('2nd: ' if (step%2) else '1st: ')) - 1
            if possibility(i, j): return [i, j]
        except: continue


def check():
    for i,j in product(range(6), range(3)):
            if (b[i][j] == b[i][j+1] == b[i][j+2] == b[i][j+3] != '  '):
                return True
    for j,i in product(range(6), range(3)):
            if (b[i][j] == b[i+1][j] == b[i+2][j] == b[i+3][j] != '  '):
                return True   
    for i,j in product(range(3), range(3)):
            if (b[i][j] == b[i+1][j+1] == b[i+2][j+2] == b[i+3][j+3] != '  '):
                return True
    for i,j in product(range(3), range(3, 6)):
            if (b[i][j] == b[i+1][j-1] == b[i+2][j-2] == b[i+3][j-3] != '  '):
                return True
    return False


def main():
    print('Connect Four game:')
    while input('Play? (y) ') == 'y':
        global b; b = [['  ']*6 for _ in range(6)]
        cout()
        for step in range(36):
            [i, j] = reading(step)
            b[i][j] = 'o ' if (step%2) else 'x '
            cout()
            if check(): break
        if check():
            print(('2nd' if (step%2) else '1st') + ' won')
        else:
            print('Friendship won')


main()
