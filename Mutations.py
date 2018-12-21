def mutate_string(string, position, character):
    str2list = list(string)
    str2list[position] = character
    string = ''.join(str2list)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)