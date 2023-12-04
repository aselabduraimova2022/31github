def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Проверка по горизонтали и вертикали
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ' or \
           board[0][i] == board[1][i] == board[2][i] != ' ':
            return True

    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input("Введите номер строки (0, 1, 2): "))
        col = int(input("Введите номер столбца (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f'Игрок {current_player} победил!')
                break
            elif is_board_full(board):
                print_board(board)
                print('Ничья!')
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Эта ячейка уже занята. Выберите другую.")

    tic_tac_toe()
