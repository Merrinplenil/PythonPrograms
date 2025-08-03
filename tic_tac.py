import random

board = [' ']*9  # stored as a list

def show():
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")

def check_winner():
    # All possible winning combinations
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

# Main game loop
while True:
    show()
    
    # Determine current player (random X or O)
    current_player = random.choice(['X', 'O'])

    # Get valid move
    while True:
        try:
            pos = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
            if 0 <= pos <= 8 and board[pos] == ' ':
                board[pos] = current_player
                break
            print("Invalid move! Try again.")
        except:
            print("Please enter a number 1-9")
    
    # Check for winner
    winner = check_winner()
    if winner:
        show()
        print(f"Player {winner} wins!")
        break
    
    # Check for tie
    if ' ' not in board:
        show()
        print("It's a tie!")
        break