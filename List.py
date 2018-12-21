if __name__ == '__main__':
    N = int(input())
    lista=[]
    for i in range(N):
        cmd = input().split()
        if cmd[0] == "insert":
            lista.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "remove":
            lista.remove(int(cmd[1]))
        elif cmd[0] == "append":
            lista.append(int(cmd[1]))
        elif cmd[0] == "sort":
            lista.sort()
        elif cmd[0] == "reverse":
            lista.reverse()
        elif cmd[0] == "pop":
            lista.pop()
        elif cmd[0] == "print":
            print(lista)