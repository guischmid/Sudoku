import random
import copy

# Define the size of the Sudoku board (9x9)
BOARD_SIZE = 9

# Function to print the Sudoku board in a readable format
def print_board(board):
    for i in range(BOARD_SIZE):
        if i % 3 == 0 and i != 0:  # Print horizontal separator every 3 rows
            print("-" * 21)
        for j in range(BOARD_SIZE):
            if j % 3 == 0 and j != 0:  # Print vertical separator every 3 columns
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")  # Print cell value or dot
        print()

# Function to check if placing a number in a cell is valid
def is_valid(board, row, col, num):
    # Check row, column, and 3x3 subgrid for the number
    for i in range(BOARD_SIZE):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

# Function to solve the Sudoku board using backtracking
def solve_board(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number
                        if solve_board(board):  # Recursively solve the board
                            return True
                        board[row][col] = 0  # Backtrack if solution fails
                return False  # No valid number found for this cell
    return True  # Board is solved

# Function to generate a fully solved Sudoku board
def generate_full_board():
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]  # Initialize empty board
    numbers = list(range(1, 10))  # List of numbers 1-9
    for i in range(0, BOARD_SIZE, 3):  # Fill each 3x3 subgrid
        for j in range(0, BOARD_SIZE, 3):
            random.shuffle(numbers)  # Shuffle numbers for randomness
            for k in range(9):
                row = i + k // 3
                col = j + k % 3
                board[row][col] = numbers[k]
    solve_board(board)  # Ensure the board is solvable
    return board

# Function to remove numbers from the board to create a puzzle
def remove_numbers(board, difficulty=40):
    puzzle = copy.deepcopy(board)
    removed = 0
    while removed < difficulty:  # Remove numbers until the desired difficulty is reached
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            removed += 1
    return puzzle

# Function to play the Sudoku game
def play_game(puzzle, solution):
    board = copy.deepcopy(puzzle)
    while True:
        print_board(board)
        try:
            # Get user input for row, column, and number
            row = int(input("Row (0-8): "))
            col = int(input("Col (0-8): "))
            num = int(input("Number (1-9): "))
        except ValueError:
            print("Invalid input. Use numbers 0-8 for row/col and 1-9 for number.")
            continue

        if puzzle[row][col] != 0:  # Prevent changing fixed numbers
            print("You can't change a fixed number!")
            continue
        if num == solution[row][col]:  # Check if the number is correct
            board[row][col] = num
        else:
            print("Incorrect number!")

        if board == solution:  # Check if the puzzle is solved
            print_board(board)
            print("Congratulations, you solved the puzzle!")
            break

# Main function to generate a puzzle and start the game
def main():
    print("Generating a Sudoku puzzle...")
    solution = generate_full_board()  # Generate a fully solved board
    puzzle = remove_numbers(solution, difficulty=40)  # Adjust difficulty (20–60)
    play_game(puzzle, solution)  # Start the game

if __name__ == "__main__":
    main()
