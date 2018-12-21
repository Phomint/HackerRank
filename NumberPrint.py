n = int(input())
numbers = [i+1 for i in range(n)]
print(*numbers, sep='',end='\n')