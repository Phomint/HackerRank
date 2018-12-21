#s = set("Hacker")
#print(s.difference("Rank"))
#print(s.difference(set(['R','a','n','k'])))
#print(s.difference(['R','a','n','k']))
#print(s.difference(enumerate(['R','a','n','k'])))
#print(s.difference({"Rank":1}))
#print(s - set("Rank"))

if __name__ == '__main__':
    n_english = int(input())
    english = set(input().split())
    n_french = int(input())
    french = set(input().split())
    print(len(english.difference(french)))