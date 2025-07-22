  
import random
import time

# Initialize positions
player_name = input("Enter your name: ")
print(f'Welcome {player_name} to Snake and Ladder')

player_pos = 0
computer_pos = 0
player_start = False
computer_start = False

def roll_dice():
    return random.randint(1, 6)

def check_ladder(position):
    # Example ladder: if you land on 15, climb to 45
    if position == 15:
        print(" Ladder! Climb up to 45")
        return position + 30
    if position == 40:
        print('Ladder climb up to 70')
        return position + 30
    if position == 85:
        print('ladder')
        return position + 10
    return position

def check_snake(position):
    # Example snake: if you land on 50, go down to 20
    if position == 50:
        print("Snake! Slide down to 20")
        return 20
    if position == 64:
        print('Snake')
        return 40
    return position

# Game loop
while True:
    input(f"\n{player_name}'s turn — press Enter to roll")
    dice = roll_dice()
    print(f"{player_name} rolled: {dice}")
    if not player_start:
        if dice==1:
            player_start = True
            print("Your game start")
    if player_start:
        
        player_pos += dice
        player_pos = check_ladder(player_pos)
        player_pos = check_snake(player_pos)

        if player_pos > 100:
            player_pos -= dice  # can't move if exceeds 100
        print(f"{player_name}'s position: {player_pos}")

        if player_pos == 100:
            print(f"🎉 {player_name} wins the game!")
            break

    # Computer's turn
    time.sleep(1)
    print("\nComputer's turn...")
    dice = roll_dice()
    print(f"Computer rolled: {dice}")
    if not computer_start:
        if dice == 1:
            computer_start = True
            print("Computer game start now")
    if computer_start:
    
        computer_pos += dice
        computer_pos = check_ladder(computer_pos)
        computer_pos = check_snake(computer_pos)

        if computer_pos > 100:
            computer_pos -= dice
        print(f"Computer's position: {computer_pos}")

        if computer_pos == 100:
            print("🤖 Computer wins the game!")
            break
