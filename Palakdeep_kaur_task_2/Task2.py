import random
l=["python", "machine", "learning", "data", "science"]
word=random.choice(l)
n=6
while(n>0):
    found=False
    pos=0
    a=str(input("guess the letter")).lower()
    for j in word:
        pos+=1
        if a==j:
            print("correct")
            print("position:",pos)
            found=True
            break
    if not found:
        n-=1
        print('wrong attempts left:',n)
    if n==0:
        print("Game over! The word was:", word)
        break