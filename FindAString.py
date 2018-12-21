def count_substring(string, substring):
    qnt = sum([1 for i in range(len(string) - len(substring) + 1) if string[i:i + len(substring)] == substring])
    return qnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)