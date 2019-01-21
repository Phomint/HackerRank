n, m = map(int,input().split())
p = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(p + ['WELCOME'.center(m, '-')] + p[::-1]))