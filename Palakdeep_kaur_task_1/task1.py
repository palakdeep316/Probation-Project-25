import random
rand_no = random.randint(1, 100)
for i in range (1,8):
    n=int(input("Guess the number"))
    if n==rand_no:
        print("Correct! User wins")
        break
    elif 7-i==0:
        print("User lost! The number was ",rand_no)
    elif n<rand_no:
        print('Too low! Attempts left:',7-i)
    else:
        print('Too high! Attempts left:',7-i)