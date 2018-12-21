#H = set("Hacker")
#R = set("Rank")
#H.update(R)
#print(H)

#H = set("Hacker")
#R = set("Rank")
#H.intersection_update(R)
#print(H)

#H = set("Hacker")
#R = set("Rank")
#H.difference_update(R)
#print(H)

#H = set("Hacker")
#R = set("Rank")
#H.symmetric_difference_update(R)
#print(H)

if __name__ == '__main__':
    n_A = int(input())
    conjunto_A = set(input().split())

    N = int(input())

    for i in range(N):
        (operacao, n_Conjunto) = input().split()
        outro_conjunto = set(input().split())

        if operacao == 'intersection_update':
            conjunto_A.intersection_update(outro_conjunto)
        elif operacao == 'update':
            conjunto_A.update(outro_conjunto)
        elif operacao == 'symmetric_difference_update':
            conjunto_A.symmetric_difference_update(outro_conjunto)
        elif operacao == 'difference_update':
            conjunto_A.difference_update(outro_conjunto)
        else:
            assert False

    print(sum(map(int, conjunto_A)))

