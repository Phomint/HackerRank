if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores)/len(scores)
    query_name = input()

    # No site não funcionou por causa da formatação
    print(f'{student_marks[query_name]:.2f}')
    # O mesmo apenas usando função format para rodar no site
    print('{:.2f}'.format(student_marks[query_name]))
