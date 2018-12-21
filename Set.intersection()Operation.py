#s = set("Hacker")
#print(s.intersection("Rank"))
#print(s.intersection(set(['R','a','n','k'])))
#print(s.intersection(['R','a','n','k']))
#print(s.intersection(enumerate(['R','a','n','k'])))
#print(s.intersection({"Rank":1}))
#print(s & set("Rank"))

if __name__ == '__main__':
    n_english = int(input())
    english = set(input().split())

    n_french = int(input())
    french = set(input().split())
    print(len(english.intersection(french)))