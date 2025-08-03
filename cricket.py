import random

def odd_or_even_cricket():
    print("Welcome to Odd or Even Cricket!")
    print("Rules: Choose odd/even. If you win the toss, you choose to bat or bowl first.")
    
    # Toss
    user_choice = input("Odd or Even? (type 'odd' or 'even'): ").lower()
    while user_choice not in ['odd', 'even']:
        user_choice = input("Please type 'odd' or 'even': ").lower()
    
    user_number = int(input("Pick a number (1-6): "))
    comp_number = random.randint(1, 6)
    total = user_number + comp_number
    
    print(f"\nYou chose: {user_number}")
    print(f"Computer chose: {comp_number}")
    print(f"Total: {total} ({'even' if total%2==0 else 'odd'})")
    
    # Determine toss winner
    if (total%2 == 0 and user_choice == 'even') or (total%2 != 0 and user_choice == 'odd'):
        print("\nYou won the toss!")
        decision = input("Choose to 'bat' or 'bowl' first: ").lower()
        while decision not in ['bat', 'bowl']:
            decision = input("Please type 'bat' or 'bowl': ").lower()
    else:
        print("\nComputer won the toss!")
        decision = random.choice(['bat', 'bowl'])
        print(f"Computer chooses to {decision} first")
    
    # Gameplay
    user_score = 0
    comp_score = 0
    innings = 1
    
    while innings <= 2:
        print(f"\n{'Your batting' if (decision=='bat' and innings==1) or (decision=='bowl' and innings==2) else 'Your bowling'} innings")
        
        while True:
            user_play = int(input("Your play (1-6): "))
            while user_play < 1 or user_play > 6:
                user_play = int(input("Please enter 1-6: "))
            
            comp_play = random.randint(1, 6)
            print(f"Computer plays: {comp_play}")
            
            if (decision == 'bat' and innings == 1) or (decision == 'bowl' and innings == 2):
                # User batting
                if user_play != comp_play:
                    user_score += user_play
                    print(f"Your score: {user_score}")
                else:
                    print("OUT! Innings over.")
                    break
            else:
                # Computer batting
                if user_play != comp_play:
                    comp_score += comp_play
                    print(f"Computer score: {comp_score}")
                else:
                    print("OUT! Innings over.")
                    break
        
        innings += 1
    
    # Result
    print("\nFinal Scores:")
    print(f"You: {user_score}")
    print(f"Computer: {comp_score}")
    
    if user_score > comp_score:
        print("You win!")
    elif comp_score > user_score:
        print("Computer wins!")
    else:
        print("It's a tie!")

# Start the game
odd_or_even_cricket()