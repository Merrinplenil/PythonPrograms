import random
print("\nGuess the movie")
movie = ['hello','avesham','thudarum']
g = random.choice(movie)
guess=['_']*len(g)
# print(g)
chance = 10
while chance>0:
    print("word:",' '.join(guess))
    print("Chance left:",chance)
    n =input('\nEnter the character').lower()
    for j in range(len(g)):
        found = False
        if g[j]==n:
            guess[j] = n
            found = True
    if found:
        print("Correct guess")
    else:
        chance =chance - 1
        print("Wrong")
    if '_' not in guess:
        break
if '_' not in guess:
    print('You Win,the movie is',g)
        
else:
    print("You lost")
    

            
            
    
        

