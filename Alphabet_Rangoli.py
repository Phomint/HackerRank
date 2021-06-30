import string


def print_rangoli(size):
    alpha = string.ascii_lowercase
    out = []
    for i in range(size):
        line = '-'.join(alpha[i:size])
        out.append((line[::-1]+line[1:]).center(4*n-3, '-'))
    print('\n'.join(out[:0:-1]+out))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

