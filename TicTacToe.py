import random
# winList = [['X', 'X', 'X'], ['X', 'O', 'O'], ['X', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'X'], ['O', 'O', 'X'],
#            ['X', 'X', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'X'], ['O', 'X', 'O'],
#            ['X', 'X', 'X'], ['O', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'O']]
winList = [
[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

winList.sort()


board = [['---', '---', '---'], ['---', '---', '---'], ['---', '---', '---']]
moves = []
userMove = []
compMove = []
gameOver = False
moveCounter = 1
gameStart = """
\t\tTic Tac Toe Game Playing Instructions
\t\t{}

Enter the row and column number where you want to add an 'X'.
Row numbers and column numbers are between 0 - 2.

\t\t\t\t\t   0   1   2
\n\t\t\t\t\t0 --- --- ---\n\n\t\t\t\t\t1 --- --- ---\n\n\t\t\t\t\t2 --- --- ---

The game starts now\n""".format('-'*len('Tic Tac Toe Game Playing Instructions'))

print(gameStart)
try:
    while not gameOver:
        for i in range(len(board)):
            print('\t'*5, *board[i], '\n')

        """
        Just to remember different possibility to print the list as same as above
        for i in board:
            print(*i)
        """
        # User's turn
        userFilled = False
        if moveCounter % 2 == 1:
            while not userFilled:
                print('', 'Your turn'.center(len('Enter the column number:')), '-'*len('Enter the column number:'), sep='\n')
                row = int(input('Enter the row number: '))
                col = int(input('Enter the column number: '))
                if not userMove in moves:
                    board[row][col] = 'X'.center(3)
                    userMove += [[row, col]]
                    moves += [[row, col]]
                    moveCounter += 1
                    gameOver = False
                    userFilled = True
                    break
                else:
                    print(row, col, " is already filled. ")
                    break
        else:
            # Computer's turn
            # while not isEmpty:
            # Computer makes the first move randomly
            print("Computer's turn".center(len('Enter the column number:')),
                  '-'*len("Enter the column number:"), sep='\n')

            if moveCounter == 2:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                print('Computer played: ',row, col)
                if board[row][col] == '---':
                    board[row][col] = 'O'.center(3)
                    compMove += [[row, col]]
                    moves += [[row, col]]
                    moveCounter += 1
                    computerFilled = True

            else:
                # Developing a simple AI algorithm here
                # Searching for two of the same entry in a row, for every row/column,
                # lines 82-135 searches same sign (X or O) diagonally
                # lines 136-164 searches same sign (X or O) in the same row
                # lines 165-202 searches same sign (X or O) in the same column
                # If found, adding 'O' to the third if it's empty.
                computerFilled = False
                while not computerFilled:
                    if board[0][0] == board[1][1] and \
                            not (board[0][0] == '---' or board[1][1] == '---') and \
                            board[2][2] == '---':
                        board[2][2] = 'O'.center(3)
                        compMove += [[2, 2]]
                        moves += [[2, 2]]
                        moveCounter += 1
                        computerFilled = True
                        print('Computer played: ', '2', '2')
                        break
                    elif board[0][0] == board[2][2] and \
                            not (board[0][0] == '---' or board[2][2] == '---') and \
                            board[1][1] == '---':
                        board[1][1] = 'O'.center(3)
                        compMove += [[1, 1]]
                        moves += [[1, 1]]
                        moveCounter += 1
                        computerFilled = True
                        print('Computer played: ', '1', '1')
                        break
                    elif board[1][1] == board[2][2] and \
                            not (board[2][2] == '---' or board[1][1] == '---') and \
                            board[0][0] == '---':
                        board[0][0] = 'O'.center(3)
                        compMove += [[0, 0]]
                        moves += [[0, 0]]
                        moveCounter += 1
                        computerFilled = True
                        print('Computer played: ', '0', '0')
                        break
                    elif board[0][2] == board[1][1] and \
                            not (board[0][2] == '---' or board[1][1] == '---') and \
                            board[2][0] == '---':
                        board[2][0] = 'O'.center(3)
                        compMove += [[2, 0]]
                        moves += [[2, 0]]
                        moveCounter += 1
                        computerFilled = True
                        print('Computer played: ', '2', '0')
                        break
                    elif board[0][2] == board[2][0] and \
                            not (board[0][2] == '---' or board[2][0] == '---') and \
                            board[1][1] == '---':
                        board[1][1] = 'O'.center(3)
                        compMove += [[1, 1]]
                        moves += [[1, 1]]
                        moveCounter += 1
                        computerFilled = True
                        print('Computer played: ', '1', '1')
                        break
                    elif board[1][1] == board[2][0] and \
                            not (board[2][0] == '---' or board[1][1] == '---') and \
                            board[0][2] == '---':
                        board[0][2] = 'O'.center(3)
                        compMove += [[0, 2]]
                        moves += [[0, 2]]
                        moveCounter += 1
                        computerFilled = True
                        print('Computer played: ', '0', '2')
                        break
                    else:
                        for row in range(2):
                            if board[row][0] == board[row][1] and \
                                    not (board[row][0] == '---' or board[row][1] == '---') and \
                                    board[row][2] == '---':
                                board[row][2] = 'O'.center(3)
                                compMove += [[row, 2]]
                                moves += [[row, 2]]
                                moveCounter += 1
                                computerFilled = True
                                print('Computer played: ', row, '2')
                                break
                            elif board[row][1] == board[row][2] and \
                                    not (board[row][1] == '---' or board[row][2] == '---') and \
                                    board[row][0] == '---':
                                board[row][0] = 'O'.center(3)
                                compMove += [[row, 0]]
                                moves += [[row, 0]]
                                moveCounter += 1
                                computerFilled = True
                                print('Computer played: ', row, '0')
                                break
                            elif board[row][0] == board[row][2] and \
                                    not (board[row][0] == '---' or board[row][2] == '---') and \
                                    board[row][1] == '---':
                                board[row][1] = 'O'.center(3)
                                compMove += [[row, 1]]
                                moves += [[row, 1]]
                                moveCounter += 1
                                computerFilled = True
                                print('Computer played: ', row, '1')
                                break
                        else:
                            for col in range(2):
                                if board[0][col] == board[1][col] and \
                                        not (board[0][col] == '---' or board[1][col] == '---') and \
                                        board[2][col] == '---':
                                    board[2][col] = 'O'.center(3)
                                    compMove += [[2, col]]
                                    moves += [[2, col]]
                                    moveCounter += 1
                                    computerFilled = True
                                    print('Computer played: ', '2', col)
                                    break

                                elif board[1][col] == board[2][col] and \
                                        not (board[1][col] == '---' or board[2][col] == '---') and \
                                        board[0][col] == '---':
                                    board[0][col] = 'O'.center(3)
                                    compMove += [[0, col]]
                                    moves += [[0, col]]
                                    moveCounter += 1
                                    computerFilled = True
                                    print('Computer played: ', '0', col)
                                    break
                                elif board[0][col] == board[2][col] and \
                                        not (board[0][col] == '---' or board[2][col] == '---') and \
                                        board[1][col] == '---':
                                    board[1][col] = 'O'.center(3)
                                    compMove += [[1, col]]
                                    moves += [[1, col]]
                                    moveCounter += 1
                                    computerFilled = True
                                    print('Computer played: ', '1', col)
                                    break
                            else:
                                while not computerFilled:
                                    row = random.randint(0, 2)
                                    col = random.randint(0, 2)
                                    print('Computer played: ', row, col)
                                    if board[row][col] == '---':
                                        board[row][col] = 'O'.center(3)
                                        compMove += [[row, col]]
                                        moves += [[row, col]]
                                        moveCounter += 1
                                        computerFilled = True
                                        print('Computer played: ', row, col)
                                        break
                                    else:
                                        continue

        print('\n')
        compMove.sort()
        userMove.sort()
        # set(tuple(i) for i in winList[i]).issubset(tuple(i) for i in userMove):
        # for combinations in winList:
        #     for i in combinations:
        #         if set(i).issubset(userMove):
        #             for i in range(len(board)):
        #                 print('\t' * 5, *board[i], '\n')
        #             print("Congrats! You won! :)")
        #             gameOver = True
        #             quit()
        #         elif set(i).issubset(compMove):
        #             for i in range(len(board)):
        #                 print('\t' * 5, *board[i], '\n')
        #             print("Sorry! You lost! :(")
        #             gameOver = True
        #             quit()
        for i in winList:
            if set(tuple(x) for x in i).issubset(tuple(x) for x in userMove):
                for k in range(len(board)):
                    print('\t' * 5, *board[k], '\n')
                print("Congratulations! You won! :)")
                gameOver = True
            if set(tuple(x) for x in i).issubset(tuple(x) for x in compMove):
                for k in range(len(board)):
                    print('\t' * 5, *board[k], '\n')
                print("Sorry, the computer won! :(")
                gameOver = True
        else:
            if moveCounter == 10:
                for k in range(len(board)):
                    print('\t' * 5, *board[k], '\n')
                print("It's a tie! Neither you, nor the computer won. :|")
                gameOver = True

except ValueError:
    print('You have made a wrong entry!')
