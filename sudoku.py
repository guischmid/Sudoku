# This code generates a Sudoku puzzle, removes some numbers to create a playable puzzle,
# and allows the user to play the game by filling in the numbers.
# The game checks for validity and provides feedback.
# The solution is also provided for checking the user's input.
# The game ends when the user successfully fills the board.

import random
import copy

BOARD_SIZE = 9

def print_board(board):
    for i in range(BOARD_SIZE):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(BOARD_SIZE):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def is_valid(board, row, col, num):
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

def solve_board(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    numbers = list(range(1, 10))
    for i in range(0, BOARD_SIZE, 3):
        for j in range(0, BOARD_SIZE, 3):
            random.shuffle(numbers)
            for k in range(3):
                for l in range(3):
                    board[i + k][j + l] = numbers[k * 3 + l]
    if solve_board(board):
        return board
    return generate_full_board()

def remove_numbers(board, difficulty=40):
    puzzle = copy.deepcopy(board)
    removed = 0
    while removed < difficulty:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            removed += 1
    return puzzle

def play_game(puzzle, solution):
    board = copy.deepcopy(puzzle)
    while True:
        print_board(board)
        try:
            row = int(input("Row (0-8): "))
            col = int(input("Col (0-8): "))
            num = int(input("Number (1-9): "))
        except ValueError:
            print("Invalid input. Use numbers 0-8 for row/col and 1-9 for number.")
            continue

        if puzzle[row][col] != 0:
            print("You can't change a fixed number!")
            continue
        if num == solution[row][col]:
            board[row][col] = num
        else:
            print("Incorrect number!")

        if board == solution:
            print_board(board)
            print("Congratulations, you solved the puzzle!")
            break

def main():
    print("Generating a Sudoku puzzle...")
    solution = generate_full_board()
    puzzle = remove_numbers(solution, difficulty=40)  # Adjust difficulty (20–60)
    play_game(puzzle, solution)

if __name__ == "__main__":
    main()
