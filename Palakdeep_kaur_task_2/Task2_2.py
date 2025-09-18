import random
l=["python", "machine", "learning", "data", "science"]
word=random.choice(l)
attempt=6
pos=0
print("words:","_"*len(word))
while attempt>0:
    a=str(input("guess a word:\n"))
    if a==word[pos]:
        print("correct guess")
        pos+=1
    else:
        attempt-=1
        print("wrong guess,chances left:",attempt)
    for i in range(0,len(word)):
        if i<pos:
            print(word[i],end="")
        else:
            print("_",end="")
    print()
    if pos==len(word):
        print("you guessed the word correct")
        break
    if attempt==0:
        print("you lose")
