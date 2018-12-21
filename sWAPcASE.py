def swap_case(s):
    str2list = list(s)
    for i in range(len(str2list)):
        if(str2list[i].isupper()):
            str2list[i]= str2list[i].lower()
        elif(str2list[i].islower()):
            str2list[i] = str2list[i].upper()
    s = ''.join(str2list)
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)