#s = set("Hacker")
#print(s.symmetric_difference("Rank"))
#print(s.symmetric_difference(set(['R','a','n','k'])))
#print(s.symmetric_difference(['R','a','n','k']))
#print(s.symmetric_difference(enumerate(['R','a','n','k'])))
#print(s.symmetric_difference({"Rank":1}))
#print(s^set("Rank"))

if __name__ == '__main__':
    n_english = int(input())
    english = set(input().split())
    n_french = int(input())
    french = set(input().split())

    print(len(english.symmetric_difference(french)))