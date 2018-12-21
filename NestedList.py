lista = []
for _ in range(0,int(input())):
    lista.append([input(), float(input())])

segundo = sorted(list(set([marks for name, marks in lista])))[1]
print('\n'.join([a for a,b in sorted(lista) if b == segundo]))