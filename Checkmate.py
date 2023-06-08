def is_queen_attacking_king(board):
    king_position = None
    queen_positions = []

    # Find the positions of the king and queens
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_position = [i, j]
            elif board[i][j] == 'Q':
                queen_positions.append([i, j])

    # Check if any of the queens can capture the king
    attacking_queens = []
    for queen in queen_positions:
        if is_queen_attacking(queen, king_position, board):
            attacking_queens.append(queen)

    # Sort the attacking queens' positions
    attacking_queens = sorted(attacking_queens, key=lambda x: x[1], reverse=True)

    # Print the positions of the attacking queens or the message if the king is safe
    if len(attacking_queens) == 0:
        print("The king is safe!")
    else:
        for queen in attacking_queens:
            print(queen)

def is_queen_attacking(queen, king, board):
    row_diff = abs(queen[0] - king[0])
    col_diff = abs(queen[1] - king[1])

    # Check if the queen and king are on the same row or column
    if queen[0] == king[0] or queen[1] == king[1]:
        # Check if there are any obstacles between the queen and king
        for i in range(min(queen[1], king[1]) + 1, max(queen[1], king[1])):
            if board[queen[0]][i] != '.':
                return False
        for i in range(min(queen[0], king[0]) + 1, max(queen[0], king[0])):
            if board[i][queen[1]] != '.':
                return False
        return True

    # Check if the queen and king are on the same diagonal
    if row_diff == col_diff:
        # Check if there are any obstacles between the queen and king
        row_step = 1 if queen[0] < king[0] else -1
        col_step = 1 if queen[1] < king[1] else -1
        row = queen[0] + row_step
        col = queen[1] + col_step
        while row != king[0] and col != king[1]:
            if board[row][col] != '.':
                return False
            row += row_step
            col += col_step
        return True

    return False

# Input the board state
board = []
for _ in range(8):
    row = input().split()
    board.append(row)

# Call the function
is_queen_attacking_king(board)
