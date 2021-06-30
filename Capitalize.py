def solve(s):
    d = [i[0].upper()+i[1:] if len(i) > 0 else i for i in s.split(' ')]
    return ' '.join(d)


if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)
